class NoUnallottedDevelopers(Exception):
    def __init__(self, msg="All Developers are allotted with a project\n"):
        self.msg = msg
        super().__init__(self.msg)