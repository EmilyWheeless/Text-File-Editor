# Converting Text File Indentations to Python Indentations

import black

def code_formatting(file_path):
    try: 
        with open(file_path, 'r') as file:
            translation=file.read()
            formatted_code = black.format_str(translation, mode=black.FileMode())
        with open(file_path, 'w') as file:
            file.write(formatted_code)
            print(f'Formatted {file_path} successfully!')
        return True #Format was successful :3
    except Exception as e:
        print(f'File {file_path} was unable to be translated properly.')
        print(f'Error: {e}') 
        return False #Format FAILED D:
    
def clean_input(file_path):
    return file_path.strip('')
while True:
    file_path = input(f'Please Input Raw Code File Here :] *file with python code only plz* --> ')
    file_path = clean_input(file_path) #Found that clean_input easier to use than classic if statements :D
    if file_path.lower() == 'exit' or file_path.lower() == 'quit':
        print(f'Goodbye!')
        break 
    if code_formatting(file_path):
        break 



