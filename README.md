# Cisco Configuration Post-Check

Checks whether the intended command lines are present in a post-change running configuration and reports missing commands.

## Main entry points

- `src.deployment.DeploymentResult`
- `src.deployment.DeploymentValidator` (`verify_deployment`)

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The project uses the Python standard library; no third-party package is required.

## Scope

This is a text validation step. It does not push configuration to a device or prove that a command is operationally effective.
