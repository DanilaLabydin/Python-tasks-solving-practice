# импортируем нужную библиотеку
from scipy.stats import uniform, expon, norm


def greeting():
    print(
        "Данная программа предназначена для вычисления следующих параметров:\n"
        "    мат.ожидание\n"
        "    ср.квдр.отклонение\n"
        "    дисперсию\n"
        "При заданных параметрах:\n"
        "     число переменных\n"
        "     закон распределения\n"
        "\n1 - равномерное распределение\n"
        "2 - экспоненциальное\n"
        "3 - нормальное\n"
    )


def display_math_stuff(sample):
    """
    функция выводит в консоль все элменты выборки
    и считает мат ожидание, диспесию и ср.кв.отклонениие
    """
    print(f"элементы выборки:\n{sample}\n")
    print(f"математическое ожидание: {sample.mean()}")
    print(f"дисперсия: {sample.var()}")
    print(f"Среднеквадратическое отклонение: {sample.std()}")


def main():
    # приветствие
    greeting()

    while True:
        size = int(input("Выберите число переменных(от 1 до 1000): "))
        distribution = int(input("Введите номер закона распределения: "))

        if size in range(1, 1001) and distribution in range(1, 5):
            break
        print("Вы ввели некоретные данные!")

    # делаем выборку с равномерным распределением
    if distribution == 1:
        title = "равномерное распределение"
        data = uniform.rvs(size=size, loc=5, scale=10)
        display_math_stuff(data)

    # экспоннциальная выборка
    elif distribution == 2:
        title = "экспоненциальное распределение"
        data = expon.rvs(size=size, loc=5, scale=10)
        display_math_stuff(data)

    # нормальное распределение
    else:
        title = "нормальное распределение"
        data = norm.rvs(size=size, loc=5, scale=10)
        display_math_stuff(data)

    # запись данных в файл
    with open("math_results.txt", "w") as file:
        file.write(f"вид распределения: {title}\n")
        file.write(f"количетсво переменных в выборке: {size}\n")
        file.write(f"математическое ожидание {data.mean()}\n")
        file.write(f"дисперсия {data.var()}\n")
        file.write(f"среднеквадратическое отклонение {data.std()}\n")
        file.write(f"элементы выборки:\n{str(data)}")


if __name__ == "__main__":
    main()
