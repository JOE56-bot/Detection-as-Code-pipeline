import re
import unittest


ENCODED_SWITCH = re.compile(
    r"(?i)(^|\s)(-|/)(enc|encodedcommand)(\s|:|$)"
)


def detect_encoded_powershell(file_name, command_line):
    is_powershell = file_name.lower() in {
        "powershell.exe",
        "pwsh.exe",
    }

    has_encoded_switch = bool(ENCODED_SWITCH.search(command_line))

    return is_powershell and has_encoded_switch


class TestEncodedPowerShellDetection(unittest.TestCase):

    def test_short_encoded_switch(self):
        self.assertTrue(detect_encoded_powershell(
            "powershell.exe", "powershell.exe -enc SQBFAFgA"
        ))

    def test_full_encoded_switch(self):
        self.assertTrue(detect_encoded_powershell(
            "powershell.exe", "powershell.exe -EncodedCommand SQBFAFgA"
        ))

    def test_powershell_7_encoded_switch(self):
        self.assertTrue(detect_encoded_powershell(
            "pwsh.exe", "pwsh.exe -enc SQBFAFgA"
        ))

    def test_slash_encoded_switch(self):
        self.assertTrue(detect_encoded_powershell(
            "powershell.exe", "powershell.exe /encodedcommand SQBFAFgA"
        ))

    def test_ordinary_powershell_command(self):
        self.assertFalse(detect_encoded_powershell(
            "powershell.exe", "powershell.exe -Command Get-Process"
        ))

    def test_execution_policy_argument(self):
        self.assertFalse(detect_encoded_powershell(
            "powershell.exe", "powershell.exe -ExecutionPolicy Bypass"
        ))

    def test_unrelated_executable(self):
        self.assertFalse(detect_encoded_powershell(
            "cmd.exe", "cmd.exe /c echo encodedcommand"
        ))


if __name__ == "__main__":
    unittest.main(verbosity=2)
