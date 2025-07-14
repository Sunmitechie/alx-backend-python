#!/usr/bin/env python3

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        expected_result = {"org": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        result = client.org

        # Check return value
        self.assertEqual(result, expected_result)

        # Check get_json was called with correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
