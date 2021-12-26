import time
import os

def parameters_saved_file (file_parameters = ['file_name', 'mode', 'encoding']):

    def save_decor(calculation_function):

        def save(*args, **kwargs):
            print(file_parameters[0])
            text_file = open(file_parameters[0], mode=file_parameters[1], encoding=file_parameters[2])
            Creation_time = time.time()
            arguments = ''
            for argument in args:
                arguments += str(argument) + ' '
            result = calculation_function(*args, **kwargs)
            path_to_logs = os.path.join(os.getcwd(), file_parameters[0])
            text_file.write(f'date of function call: {Creation_time}\nfunction name: {calculation_function.__name__}\nattribute name: {arguments}\nreturn value: {result}\npath to logs:{path_to_logs}')
            print(f"Файл сохранён: {path_to_logs}")
            return result
        return save
    return save_decor

@parameters_saved_file(['logger.txt', 'w', 'utf-8'])
def function_operation(variable_1, variable_2):
    return variable_1 + variable_2

result = function_operation(3, 9)

print(result)