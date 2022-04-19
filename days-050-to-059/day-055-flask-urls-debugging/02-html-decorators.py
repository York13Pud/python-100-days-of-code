# Define some decorator functions to format HTML.
def make_h1(function_called_from):
    def h1_text():
        return f'<h1 style="color:red">{function_called_from()}</h1>'
    return h1_text

def make_bold(function_called_from):
    def bold_text():
        return f'<b>{function_called_from()}</b>'
    return bold_text

def make_italic(function_called_from):
    def italic_text():
        return f'<em>{function_called_from()}</em>'
    return italic_text

def make_underlined(function_called_from):
    def underlined_text():
        return f'<u>{function_called_from()}</u>'
    return underlined_text

@make_h1
@make_bold
@make_italic
@make_underlined
def goodbye():
    return '<a href="https://www.google.com">Google it</a>'

print(goodbye())