import re
import codechef
import codeforces
import leetcode
from problemClient import ProblemClient

class Coder:
    def __init__(self, Timestamp, Email_Address, Name, Scholar_Number, Gender, Profile_Picture, Batch, Codeforces_ID, Leetcode_ID, Codechef_ID, GFG_ID, WhatsApp_Number, Notion_Page_ID, Codeforces_URL, Codechef_URL, Leetcode_URL, GFG_URL):
        self.timestamp = Timestamp
        self.email = Email_Address
        self.name = Name
        self.scholar_number = Scholar_Number
        self.gender = Gender
        self.profile_picture = Profile_Picture
        self.batch = Batch
        self.codeforces_id = Codeforces_ID
        self.leetcode_id = Leetcode_ID
        self.codechef_id = Codechef_ID
        self.gfg_id = GFG_ID
        self.whatsapp_number = WhatsApp_Number
        self.notion_page_id = Notion_Page_ID

        self.codeforces_url = Codeforces_URL
        self.codechef_url = Codechef_URL
        self.leetcode_url = Leetcode_URL
        self.gfg_url = GFG_URL

        self.problems_leetcode = set()
        self.problems_gfg = set()
        self.problems_codeforces = set()
        self.problems_codechef = set()

        self.total_problems = 0

    @staticmethod
    def unique_problems_set(problems):
        return set([problem.name for problem in problems])

    @staticmethod
    def validate_id(id_value, pattern):
        if id_value and re.match(pattern, id_value):
            return True
        return False

    def fetch_solved_problems(self, problem_client, driver):
        platforms = {
            "leetcode": (self.leetcode_url, r"https:\/\/leetcode\.com\/[a-zA-Z0-9_]+\/?"),
            "gfg": (self.gfg_url, r"https:\/\/auth\.geeksforgeeks\.org\/user\/[a-zA-Z0-9_]+\/practice\/?"),
            "codechef": (self.codechef_url, r"https:\/\/www\.codechef\.com\/users\/[a-zA-Z0-9_]+\/?"),
            "codeforces": (self.codeforces_url, r"https:\/\/codeforces\.com\/profile\/[a-zA-Z0-9_]+\/?")
        }

        for platform, (id_value, pattern) in platforms.items():
            if self.validate_id(id_value, pattern):
                print(f"Fetching {platform} problems for {self.name}...")
                try:
                    if platform == "leetcode":
                        self.problems_leetcode = leetcode.get_problems_solved(driver, problem_client, id_value, self.scholar_number)
                        self.total_problems += len(self.unique_problems_set(self.problems_leetcode))
                    elif platform == "gfg":
                        # Fetch problems for gfg
                        pass
                    elif platform == "codechef":
                        self.problems_codechef = codechef.get_problems_solved(driver, problem_client, id_value, self.scholar_number)
                        self.total_problems += len(self.unique_problems_set(self.problems_codechef))
                    elif platform == "codeforces":
                        self.problems_codeforces = codeforces.get_problems_solved(driver, problem_client, id_value, self.scholar_number)
                        self.total_problems += len(self.unique_problems_set(self.problems_codeforces))
                except Exception as e:
                    print(f"Error fetching {platform} problems for {self.name}: {str(e)}")
            else:
                print(f"Invalid {platform} ID for {self.name}...")
            