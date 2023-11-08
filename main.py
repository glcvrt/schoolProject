from schoolProject.API_vacancies import HeadHunter, SuperJob, HHFile, SJFile


def main():
    page = 1
    keywords = input("Введите ключевое слово: ")
    salary = int(input("Введите желаемую зарплату: "))
    platform = int(input("Выберите сервис поиска вакансий: 1 - HeadHunter, 2 - SuperJob: "))
    answer = "more"
    if platform == 1:
        while answer == "more":
            hh = HeadHunter(keywords, salary, page)
            hh.get_vacancies()
            data = hh.sorting_vacansies()
            if len(data) == 0:
                page += 1
            else:
                hh = HHFile(data)
                hh.load_vacancies()
                hh.formatting()
                answer = input("more - ещё посмотреть вакансии, exit - выйти: ")
                if answer == "more":
                    page += 1
                else:
                    break

    elif platform == 2:
        while answer == "more":
            sj = SuperJob(keywords, salary, page)
            sj.get_vacancies()
            data = sj.sorting_vacansies()
            if len(data) == 0:
                page += 1

            else:
                sj = SJFile(data)
                sj.load_vacancies()
                sj.formatting()
                answer = input("more - ещё посмотреть вакансии, exit - выйти: ")
                if answer == "more":
                    page += 1
                else:
                    break


main()
