import os
import unittest

from rowantree.common.sdk import EnvironmentVariableNotFoundError, demand_env_var


class TestSDK(unittest.TestCase):
    def setUp(self) -> None:
        if "FAKE_VALUE" in os.environ:
            del os.environ["FAKE_VALUE"]

    def tearDown(self) -> None:
        if "FAKE_VALUE" in os.environ:
            del os.environ["FAKE_VALUE"]

    def test_demand_env_var_should_gracefully_fail(self):
        with self.assertRaises(EnvironmentVariableNotFoundError) as context:
            demand_env_var("FAKE_VALUE")
        self.assertEqual(str(context.exception), "Environment variable (FAKE_VALUE) not found")


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestSDK())
