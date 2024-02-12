class InvalidDataFormatError(Exception):
    pass

class InvalidDateFormatError(InvalidDataFormatError):
    pass

class InvalidPhoneNumberFormatError(InvalidDataFormatError):
    pass

class InvalidGenderFormatError(InvalidDataFormatError):
    pass

def validate_input(input_data):
    # Разбиваем введенные данные по пробелу
    data = input_data.split()

    # Проверяем количество элементов
    if len(data) != 6:
        raise InvalidDataFormatError("Ошибка: неверное количество данных. Пожалуйста, введите Фамилию, Имя, Отчество, дату рождения, номер телефона и пол, разделенные пробелом.")

    # Проверяем формат даты рождения (dd.mm.yyyy)
    dob = data[3]
    if len(dob) != 10 or dob[2] != '.' or dob[5] != '.':
        raise InvalidDateFormatError("Ошибка: неверный формат даты рождения. Используйте формат dd.mm.yyyy.")

    # Проверяем, что номер телефона состоит только из цифр
    phone_number = data[4]
    if not phone_number.isdigit():
        raise InvalidPhoneNumberFormatError("Ошибка: номер телефона должен содержать только цифры.")

    # Проверяем, что пол указан как 'f' или 'm'
    gender = data[5]
    if gender not in ['f', 'm']:
        raise InvalidGenderFormatError("Ошибка: пол должен быть указан как 'f' (женский) или 'm' (мужской).")

    # Если все проверки прошли успешно, возвращаем данные
    return data

def write_to_file(data):
    try:
        with open(data[0] + ".txt", "a") as file:
            file.write(" ".join(data) + "\n")
    except Exception as e:
        raise e

def main():
    try:
        # Запрашиваем данные у пользователя
        user_input = input("Введите Фамилию Имя Отчество дату_рождения номер_телефона пол, разделенные пробелом: ")

        # Проверяем и парсим введенные данные
        parsed_data = validate_input(user_input)

        # Если все успешно, записываем данные в файл
        write_to_file(parsed_data)

        print("Данные успешно записаны в файл.")

    except InvalidDataFormatError as e:
        print(e)
    except InvalidDateFormatError as e:
        print(e)
    except InvalidPhoneNumberFormatError as e:
        print(e)
    except InvalidGenderFormatError as e:
        print(e)
    except Exception as e:
        print("Произошла ошибка при записи данных в файл:")
        print(e)

if __name__ == "__main__":
    main()
