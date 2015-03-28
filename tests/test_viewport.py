from tests.base import IntegrationTest


class TestViewportsTaskGeneration(IntegrationTest):

    viminput = """
    === Work tasks | +work ===
    """

    vimoutput = """
    === Work tasks | +work ===
    * [ ] tag work task  #{uuid}
    """

    tasks = [
        dict(description="tag work task", tags=['work']),
    ]

    def execute(self):
        self.command("w", regex="written$", lines=1)


class TestViewportsTaskRemoval(IntegrationTest):

    viminput = """
    === Work tasks | -work ===
    * [ ] tag work task  #{uuid}
    """

    vimoutput = """
    === Work tasks | -work ===
    """

    tasks = [
        dict(description="tag work task", tags=['work']),
    ]

    def execute(self):
        self.command("w", regex="written$", lines=1)


class TestViewportDefaultsAssigment(IntegrationTest):

    viminput = """
    === Work tasks | +work ===
    * [ ] tag work task
    """

    vimoutput = """
    === Work tasks | +work ===
    * [ ] tag work task  #{uuid}
    """

    def execute(self):
        self.command("w", regex="written$", lines=1)
        assert len(self.tw.tasks.pending()) == 1

        task = self.tw.tasks.pending()[0]
        assert task['description'] == 'tag work task'
        assert task['status'] == 'pending'
        assert task['tags'] == ['work']


class TestViewportDefaultsOverriding(IntegrationTest):

    viminput = """
    === Work tasks | project:Home +home | project:Chores  ===
    * [ ] home task
    """

    vimoutput = """
    === Work tasks | project:Home +home | project:Chores  ===
    """

    def execute(self):
        self.command("w", regex="written$", lines=1)
        assert len(self.tw.tasks.pending()) == 1

        task = self.tw.tasks.pending()[0]
        assert task['description'] == 'home task'
        assert task['status'] == 'pending'
        assert task['project'] == 'Chores'
        assert task['tags'] == ['home']


class TestViewportDefaultsRemoval(IntegrationTest):

    viminput = """
    === Work tasks | project:Home +home | project:  ===
    * [ ] home task
    """

    vimoutput = """
    === Work tasks | project:Home +home | project:  ===
    """

    def execute(self):
        self.command("w", regex="written$", lines=1)
        assert len(self.tw.tasks.pending()) == 1

        task = self.tw.tasks.pending()[0]
        assert task['description'] == 'home task'
        assert task['status'] == 'pending'
        assert task['project'] == None
        assert task['tags'] == ['home']
