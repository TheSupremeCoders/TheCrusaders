from datetime import date


class GetMessage:
    def __init__(self, coders):
        self.coders = coders

    @staticmethod
    def unique_problems_set(problems):
        return set([problem.name for problem in problems])

    @staticmethod
    def print_problem(self, platform, problems, f):
        problems = self.unique_problems_set(problems)
        if len(problems) != 0:
            f.write(f'{platform} - {len(problems)}\n')
            for problem in problems:
                f.write(f' ~ {problem}\n')

    def generate_message(self, file_name):
        tdy = date.today()

        cross = '\u274C'
        check = '\u2705'

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(f'*DATE - {tdy.strftime("%d/%m/%Y")}*\n\n')
            for coder in self.coders:
                if coder.total_problems == 0:
                    f.write(f'*{coder.name} - {cross}*\n')
                else:
                    f.write(f'*{coder.name} - {coder.total_problems} problems solved - {check}*\n')
                self.print_problem(coder, '   _Leetcode_', coder.problems_leetcode, f)
                self.print_problem(coder, '   _Codeforces_', coder.problems_codeforces, f)
                self.print_problem(coder, '   _Codechef_', coder.problems_codechef, f)
                f.write('-------------------------------\n')
