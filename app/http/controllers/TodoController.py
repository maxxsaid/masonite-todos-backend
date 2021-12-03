""" A TodoController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Todo import Todo


class TodoController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request
        
        
    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", TodoController)
        """
        id = self.request.param("id")
        return Todo.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", TodoController)
        """
        return Todo.all()

    def create(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        todo = Todo.create({"subject": subject, "details": details})
        return todo

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", TodoController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", TodoController)
        """

        pass

    def update(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        id = self.request.param("id")
        Todo.where("id", id).update({"subject": subject, "details": details})
        return Todo.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        todo = Todo.where("id", id).get()
        Todo.where("id", id).delete()
        return todo