# Overview

This interface is used for a charm to request a restart of a service managed by
another charm.

# Usage

The interface provides the `{relation-name}.connected` state.

Requesting a restart of all remote services:

```python
@reactive.when('service-control.connected')
def configure(service_control):
    ...
    service_control.request_restart()
```

Requesting a restart of a specific type of remote services:

```python
@reactive.when('service-control.connected')
def configure(service_control):
    ...
    service_control.request_restart(service_type='neutron')
```

# Metadata

To consume this interface in your charm or layer, add the following to
`layer.yaml`:

```yaml
includes: ['interface:service-control']
```

and add a requires interface of type `service-control` to your charm or layers
`metadata.yaml` eg:

```yaml
requires:
  neutron-control:
    interface: service-control
```

# Bugs

Please report bugs on
[Launchpad](https://bugs.launchpad.net/openstack-charms/+filebug).

For development questions please refer to the OpenStack [Charm
Guide](https://github.com/openstack/charm-guide).
