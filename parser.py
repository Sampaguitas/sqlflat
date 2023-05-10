import re

# converts the sql querry from a file into a single line querry string
def sql_to_string(filename):
    with open(filename, 'r') as file:
        content = file.read()
        content = re.sub(r'(--[^\n]*$|/\*[^\n]*\*/)', '', content, flags=re.DOTALL | re.MULTILINE) # remove any coments
        content = re.sub(r'(^\s+)', '', content, flags=re.MULTILINE) # remove tabs and spaces at the bigining of each line
        content = content.replace('\n', ' ') # replace carriage returns by single space
        content = re.sub(r'(\s+)', ' ', content, flags=re.MULTILINE) # replace all multi tabs and space by a single space
        return content
