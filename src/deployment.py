"""Cisco IOS Configuration Deployment Post-Validation Engine."""

from dataclasses import dataclass
from typing import Dict, List, Set, Tuple


@dataclass(frozen=True)
class DeploymentResult:
    """Outcome of a deployment verification pass."""
    is_valid: bool
    missing_commands: List[str]
    applied_commands: List[str]


class DeploymentValidator:
    """Verifies that intended configuration declarations exist in device running state."""

    @staticmethod
    def verify_deployment(intended_commands: List[str], running_config: str) -> DeploymentResult:
        """
        Cross-references intended CLI commands against active running configuration lines.
        Strips whitespace to prevent false negatives from indentation differences.
        """
        running_lines: Set[str] = {l.strip() for l in running_config.splitlines() if l.strip()}
        applied: List[str] = []
        missing: List[str] = []

        for cmd in intended_commands:
            cleaned = cmd.strip()
            if not cleaned or cleaned.startswith("!"):
                continue

            if cleaned in running_lines:
                applied.append(cleaned)
            else:
                missing.append(cleaned)

        return DeploymentResult(
            is_valid=(len(missing) == 0),
            missing_commands=missing,
            applied_commands=applied
        )
