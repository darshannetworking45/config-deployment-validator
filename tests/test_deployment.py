import unittest
from src.deployment import DeploymentValidator

CONFIG = """
hostname r1
interface GigabitEthernet0/0
 ip address 10.0.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 198.51.100.1
"""

class TestDeploymentValidator(unittest.TestCase):
    def test_full_deployment(self):
        intended = ["ip route 0.0.0.0 0.0.0.0 198.51.100.1", "no shutdown"]
        res = DeploymentValidator.verify_deployment(intended, CONFIG)
        self.assertTrue(res.is_valid)
        self.assertEqual(len(res.missing_commands), 0)

    def test_partial_deployment(self):
        intended = ["ip route 0.0.0.0 0.0.0.0 198.51.100.1", "router ospf 1"]
        res = DeploymentValidator.verify_deployment(intended, CONFIG)
        self.assertFalse(res.is_valid)
        self.assertIn("router ospf 1", res.missing_commands)

if __name__ == "__main__":
    unittest.main()
