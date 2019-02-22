from selenium import webdriver

class OnlyofficeEmployees:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='./geckodriver')
        self.workers = self.data_collection()

    def data_collection(self):
        self.driver.get("https://www.onlyoffice.com/en")

        # Открываем меню About
        button = self.driver.find_element_by_xpath("//a[@id='navitem_about']")
        button.click()

        # Переходим по ссылке
        button1 = self.driver.find_element_by_xpath("//a[@id='navitem_about_about']")
        button1.click()

        # Собираем данные о сотрудниках
        names = self.driver.find_elements_by_class_name("dev_info_name")
        professions = self.driver.find_elements_by_class_name("dev_info_function")

        # Находим границу для исключения повторений сотрудников
        x = names[0].get_attribute('innerHTML')
        y = 0
        for y in range(1, len(names)):
            if x == names[y].get_attribute('innerHTML'):
                break

        # Создаем словарь [name: profession]
        workers = dict()

        for i in range(y):
            name = names[i].get_attribute('innerHTML')
            profession = professions[i].get_attribute('innerHTML')
            workers[name] = profession

        self.driver.quit()

        return workers


def main():
    a = OnlyofficeEmployees()
    workers = a.workers

    path = input('Укажите путь к выходному файлу: ')
    if path != '' != '/' and path[-1] != '/':
        path += '/'

    with open(path + 'workers.csv', 'w') as file:
        for name, profession in workers.items():
            file.write(name + ';' + profession + '\n')

if __name__ == '__main__':
    main()