import unittest
import tempfile
from pathlib import Path
from multinut.env import Environment, Modes

class TestEnvironment(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and file
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_path = Path(self.temp_dir.name)
        self.default_file = self.base_path / ".env"
        self.mode_file = self.base_path / ".env.testing"
        self.named_file = self.base_path / "custom.env"
        self.named_mode_file = self.base_path / "custom.production"

        for f in [self.default_file, self.mode_file, self.named_file, self.named_mode_file]:
            f.write_text("KEY=value\n")

    def tearDown(self):
        self.temp_dir.cleanup()

    def reset_environment_singleton(self):
        Environment._instance = None

    def test_default_env(self):
        print("here")
        self.reset_environment_singleton()
        env = Environment(env_file_path=str(self.base_path))
        self.assertTrue(str(self.default_file) in env.env_file_path)

    def test_with_named_file(self):
        print("here")
        self.reset_environment_singleton()
        env = Environment(env_file_name="custom.env", env_file_path=str(self.base_path))
        self.assertTrue(str(self.named_file) in env.env_file_path)

    def test_with_mode_enum(self):
        print("here")
        self.reset_environment_singleton()
        env = Environment(mode=Modes.TESTING, env_file_path=str(self.base_path))
        self.assertTrue(str(self.mode_file) in env.env_file_path)

    def test_with_mode_string(self):
        print("here")
        self.reset_environment_singleton()
        env = Environment(mode="testing", env_file_path=str(self.base_path))
        self.assertTrue(str(self.mode_file) in env.env_file_path)

    def test_with_named_file_and_mode_enum(self):
        print("here")
        self.reset_environment_singleton()
        env = Environment(env_file_name="custom", mode=Modes.PRODUCTION, env_file_path=str(self.base_path))
        self.assertTrue(str(self.named_mode_file) in env.env_file_path)

    def test_missing_file_raises(self):
        self.reset_environment_singleton()
        with self.assertRaises(FileNotFoundError):
            Environment(env_file_name="notfound.env", env_file_path=str(self.base_path))

    def test_missing_file_suppressed(self):
        print("here")
        self.reset_environment_singleton()
        env = Environment(env_file_name="notfound.env", env_file_path=str(self.base_path), suppress_file_not_found=True)
        self.assertIn("notfound.env", env.env_file_path)

    def test_singleton_behavior(self):
        self.reset_environment_singleton()
        a = Environment(env_file_path=str(self.base_path), suppress_file_not_found=True)
        b = Environment(env_file_path="should/be/ignored", suppress_file_not_found=True)
        self.assertIs(a, b)
        self.assertEqual(a.env_file_path, b.env_file_path)


if __name__ == '__main__':
    unittest.main()
