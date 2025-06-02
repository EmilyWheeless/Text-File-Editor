# Converting Text File Indentations to Python Indentations

import black

def check_software_status():
    try:
        import black
        print('Black is available!')
    except ImportError:
        print('Black not installed properly.')

def code_formatting(file_path):
    try: 
        with open(file_path, 'r') as file:
            translation=file.read()
            formatted_code = black.format_str(translation, mode=black.FileMode())
        with open(file_path, 'w') as file:
            file.write(formatted_code)
            print(f'Formatted {file_path} successfully!')
    except Exception as e:
        print(f'File {file_path} was unable to be translated properly.')
        print(f'Error: {e}') 

file_path=input(f'Please Input Raw Code File Here :] *.txt with python only plz* --> ')

code_formatting(file_path)


