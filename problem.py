class problem:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __str__(self):
        return f'{self.name}'
    
    def html_str(self):
        return f'<a href="{self.link}">{self.name}</a>'