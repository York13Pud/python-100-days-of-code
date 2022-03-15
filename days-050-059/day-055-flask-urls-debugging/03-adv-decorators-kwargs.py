class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_user_authenticated(function_called_from):
    # You can use *args and **kwargs to pass extra arguments in from the function that was called.
    # By default, these are not passed / usable by the wrapper function below so adding *args, 
    # You can then use a tuple index to call the argument from the function called from as an 
    # index value after args (for example, args[0] for the first argument that was passed from create_blog_post):
    
    def check_logged_in(*args, **kwargs):
        # Pretty simple, check if the user is logged in and return a value back:
        #
        # To do it using args (remove user= from the create_blog_post() call):
        # if args[0].is_logged_in == True:
        #     function_called_from(args[0])
        if kwargs.get("user").is_logged_in == True:
            function_called_from(kwargs.get("user"))
        else:
            print("You are not logged in!")
    return check_logged_in


@is_user_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post!")

new_user = User("Neil")
#new_user.is_logged_in = True
create_blog_post(user=new_user)