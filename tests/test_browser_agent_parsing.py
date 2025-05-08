import unittest
import os
import sys
from datetime import date
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to Python path
from sources.agents.browser_agent import BrowserAgent

class TestBrowserAgentParsing(unittest.TestCase):
    def setUp(self):
        # Initialize a basic BrowserAgent instance for testing
        self.agent = BrowserAgent(
            name="TestAgent",
            prompt_path="../prompts/base/browser_agent.txt",
            provider=None
        )

    def test_agent_initialization(self):
        #Test if agent is initialized with correct attributes
        self.assertEqual(self.agent.get_agent_name, "TestAgent")
        self.assertEqual(self.agent.get_agent_type, "browser_agent")
        self.assertEqual(self.agent.get_agent_role, "web")

    def test_agent_get_today_date(self):
        #Test for get_today_data method
        self.assertEqual(self.agent.get_today_date, date.today().date_time.strftime("%B %d, %Y"))

    def test_extract_links(self):
        # Test various link formats
        test_text = """
        Check this out: https://thriveonai.com/15-ai-startups-in-japan-to-take-note-of, and www.google.com!
        Also try https://test.org/about?page=1, hey this one as well bro https://weatherstack.com/documentation/.
        """
        expected = [
            "https://thriveonai.com/15-ai-startups-in-japan-to-take-note-of",
            "www.google.com",
            "https://test.org/about?page=1",
            "https://weatherstack.com/documentation",
        ]
        result = self.agent.extract_links(test_text)
        self.assertEqual(result, expected)

    def test_extract_form(self):
        # Test form extraction
        test_text = """
        Fill this: [username](john) and [password](secret123)
        Not a form: [random]text
        """
        expected = ["[username](john)", "[password](secret123)"]
        result = self.agent.extract_form(test_text)
        self.assertEqual(result, expected)

    def test_clean_links(self):
        # Test link cleaning
        test_links = [
            "https://example.com.",
            "www.test.com,",
            "https://clean.org!",
            "https://good.com"
        ]
        expected = [
            "https://example.com",
            "www.test.com",
            "https://clean.org",
            "https://good.com"
        ]
        result = self.agent.clean_links(test_links)
        self.assertEqual(result, expected)

    def test_parse_answer(self):
        # Test parsing answer with notes and links
        test_text = """
        Here's some info
        Note: This is important. We are doing test it's very cool.
        action: 
        i wanna navigate to https://test.com
        """
        self.agent.parse_answer(test_text)
        self.assertEqual(self.agent.notes[0], "Note: This is important. We are doing test it's very cool.")

if __name__ == "__main__":
    unittest.main()