# AccConf 

AccConf is a Python package to configure Python devices for particle accelerators.

The package includes code and architectural concepts derived from [HAPPI](https://github.com/pcdshub/happi) developed by SLAC National Accelerator Laboratory. See license/SLAC_LICENSE.md for details.

The code is still under development. AccConf will provide:

- A light-weight device database for particle accelerators which use the EPICS control system.
  The implementation will however be sufficiently generic to also support other control systems which have need for a way to store configuration data for devices.

- Built-in support for configuring pyAML devices to be used with pyAML applications and/or ophyd/ophyd-async devices to be used with Bluesky applications,
  providing a common way to configure devices of different types.
  
- Support to extend to also include devices from other frameworks. Likely using entrypoints similarly to how the integration is done in HAPPI: https://pcdshub.github.io/happi/v3.0.1/containers.html#integrating-with-your-package
