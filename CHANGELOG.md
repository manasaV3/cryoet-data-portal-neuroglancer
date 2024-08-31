# Changelog

## 1.0.0 (2024-08-31)


### Features

* add color to VR shader ([bb87366](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/bb87366c412165615e81bb6ac3e4535bc588ffa4))
* add diameter and shader step ([f55888a](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/f55888ab55b2418a692cd7b6baedf32295b98ec9))
* add json generator for oriented points ([1f77510](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/1f77510004be31dcb0de89aa0325a165bc1d1bf6))
* add more properties to oriented point shader ([bb8d432](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/bb8d43256cc43890707d727a91b56cd7104ba350))
* add oriented point shader ([5ed1dde](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/5ed1ddee6e91fe5128d74f30cea973dc3fabf271))
* add rotations ([9238b70](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/9238b70da9b92b0e1848394b6de10c0916c84463))
* better ranges for point size and line width oriented ([4c83d40](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/4c83d4046ece433d731e8a42e8af1956a980a5df))
* change samples to 256 instead of 512 ([2152cdc](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/2152cdc6f70354ad3c81775169ebef572302fd9f))
* clearer line length ([15e12fe](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/15e12fe608d32fa3bb0d9bf6b49577738a57bcdf))
* compute window limits takes optional scale parameter ([d0a7177](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/d0a7177ffeacd2dc5e54547747506c1216b0925b))
* correctly handle opacity 0 points ([984d73f](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/984d73fcbf42b49cebeffca735f8d815330c709d))
* create a point annotation shader ([3163ebf](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/3163ebf33f327b5dea3c0ff49efd3bd676f24402))
* first round of oriented output as lines ([09bb936](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/09bb936e0d6ec9ace3f48e1e83580582590c3bfb))
* improve output shader naming ([e61067e](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/e61067ed35fcab9112a698905357f28369151d71))
* integrate VR shader into state generation ([d9db875](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/d9db8759765af0a44e8856084d2b46e60ddb8307))
* link shader to json generator ([5bc1609](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/5bc16092d6f0acc09b89fb7c5acb792223cd7e57))
* make the image shader support VR being off ([3958772](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/3958772b21b879a9df55f692f6606f1a44786e62))
* **public:** update public json generator to use new shader builder in background ([02b49c6](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/02b49c651db3a833a5760d8af1dc480c9a423e93))
* return self from builder for chaining methods ([1c02453](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/1c02453c34d04a94c4aa9e6a24a972d232b6418c))
* update default VR samples as 10k high ([186bdc8](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/186bdc8594b90e280b0941dc7bc8cfc20b1033dd))
* update shader ([2d01d5f](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/2d01d5f3b2327f2d230a7c87d5406ebd6fc6a285))
* visually restructure output shader code from builder ([27ae510](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/27ae5101af0b0dd7f28a9bf4e152b5f9f90e10a9))
* visualy improve shader output for invertible component ([162809c](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/162809c70466dac6b8449c58808077a9cdb8f82d))
* write out three lines for point ([dee1ca1](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/dee1ca1d60126dc88025967e088f7dd9d4f4f8b3))


### Bug Fixes

* accidentally had inverted condition for VR on/off shader ([b9e35a0](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/b9e35a0804d12bc9830691f909fe320451186a07))
* correct check for image layers in state combine ([75bca5b](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/75bca5b081e323b4954e45e7acf0f193b3f267df))
* correct import for image shader after refactor ([4310f0d](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/4310f0d424537bca472debd48390b8261a21a903))
* correct padding issue, correct non-square chunk issue ([485c7cd](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/485c7cda0688056840df449d58fdc7d85da1a53b))
* correct typing on scale parameter ([36cdea5](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/36cdea56596a7d3d9849315b511483f4df61a873))
* oriented shader ([6e563fd](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/6e563fd4479f45f85bb9a5e82021f249dbeebd0e))
* remove unused color parameter for image rendering ([f1e3148](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/f1e3148bd0671e253adf8fe06739cff45115b396))
* revert changs to ImageVolumeJSONGenerator and associated state ([e122031](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/e122031fe7eabe46881662fdb25449e05e9e8321))
* **typing:** correct typing ([7170e1a](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/7170e1a3f67d6ca07dcd4265e71bdd9792957b7e))
* **typing:** shard_by_id can be None to disable the feature ([3e25768](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/3e25768f9e5f5685da0a6f62e2bc7bdd8de73b0c))
* **typing:** vr and cross section code takes string or list of string ([7166086](https://github.com/manasaV3/cryoet-data-portal-neuroglancer/commit/71660861a63a29aa34b88b7256c4c3f0f22c01b3))
