"""Create GLSL shaders for Neuroglancer."""

from typing import Any, Iterable, Optional

TAB = "  "


class ShaderBuilder:
    def __init__(self):
        self._shader_pre_main = ""
        self._shader_main_function = ""
        self._shader_controls = {}

    def add_to_shader_controls(self, code: str | Iterable[str]):
        if isinstance(code, str):
            self._shader_pre_main += code
        else:
            self._shader_pre_main += "\n".join(code)
        self._shader_pre_main += "\n"
        return self

    def add_to_shader_main(self, code: str | list[str], indent: int = 1):
        if isinstance(code, str):
            self._shader_main_function += TAB * indent + code
        else:
            self._shader_main_function += "\n".join([TAB * indent + line for line in code])
        self._shader_main_function += "\n"
        return self

    def _make_main(self) -> str:
        return f"void main() {{\n{self._shader_main_function}}}"

    def build_shader(self) -> dict[str, str | dict[str, Any]]:
        return {
            "shader": self._shader_pre_main + "\n" + self._make_main(),
            "shaderControls": self._shader_controls,
        }

    def make_invlerp_component(
        self,
        name: str,
        contrast_limits: tuple[float, float],
        window_limits: tuple[float, float],
    ) -> str:
        controls = self._shader_controls.setdefault(name, {})
        controls["range"] = list(contrast_limits)
        controls["window"] = list(window_limits)
        return f"#uicontrol invlerp {name}"

    def make_invertible_invlerp_component(
        self,
        name: str,
        contrast_limits: tuple[float, float],
        window_limits: tuple[float, float],
    ) -> list[str]:
        invlerp_component = self.make_invlerp_component(name, contrast_limits, window_limits)
        checkbox_part = f"#uicontrol bool invert_{name} checkbox(default=false)"
        data_value_getter = f"float {name}_get() {{ return invert_{name} ? 1.0 - {name}() : {name}(); }}"
        return [invlerp_component, checkbox_part, data_value_getter]

    def make_slider_component(
        self,
        name: str,
        min_value: float = 0.0,
        max_value: float = 1.0,
        default_value: Optional[float] = None,
    ) -> str:
        if default_value is not None:
            self._shader_controls[name] = default_value
        return f"#uicontrol float {name} slider(min={min_value}, max={max_value})"

    def make_color_component(self, name: str, default_color: str) -> str:
        self._shader_controls[name] = default_color
        return f"#uicontrol vec3 {name} color"


class OrientedPointShaderBuilder(ShaderBuilder):
    def __init__(self):
        super().__init__()
        self._make_default_shader()

    def _make_default_shader(self):
        self.add_to_shader_controls(
            (
                self.make_slider_component("pointScale", 0.01, 10.0, 1.0),
                self.make_slider_component("lineWidth", 0.01, 10.0, 1.0),
            ),
        )
        self.add_to_shader_main(
            (
                "setLineWidth(lineWidth());",
                "setLineColor(prop_line_color());",
                "setEndpointMarkerSize(prop_diameter() * pointScale(), 0.0);",
                "setEndpointMarkerColor(prop_point_color());",
                "setEndpointMarkerBorderWidth(0.0, 0.0);",
                "setEndpointMarkerBorderColor(vec3(0.0, 0.0, 0.0));",
            ),
        )
