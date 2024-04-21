class Book:
    mater = 'бумага'
    n_txt = True

    def __init__(self, neim_b, avtor, count_str, isbn, reserv=False):
        self.neim_b = neim_b
        self.avtor = avtor
        self.count_str = count_str
        self.isbn = isbn
        self.reserv = reserv

    def reserv_book(self):
        if self.reserv:
            print(
                f'Название: {self.neim_b}, Автор: {self.avtor}, страниц: {self.count_str}, материал: {self.mater},'
                f' зарезервирована')
        else:
            print(f"Название: {self.neim_b}, Автор: {self.avtor}, страниц: {self.count_str}, материал: {self.mater}")


class ShcoolBook(Book):

    def __init__(self, neim_b, avtor, count_str, predmet, cl, isbn, reserv=False,
                 zadanie=False):
        super().__init__(neim_b, avtor, count_str, isbn, reserv)
        self.predmet = predmet
        self.cl = cl
        self.zadanie = zadanie

    def reserv_book(self):
        if self.reserv:
            print(
                f'Название: {self.neim_b}, Автор: {self.avtor}, страниц: {self.count_str}, материал: {self.mater},'
                f' зарезервирована')
        else:
            print(f"Название: {self.neim_b}, Автор: {self.avtor}, страниц: {self.count_str}, материал: {self.mater}")


book_1 = Book("Идиот", "Достоевский", 800, "78-98Н", reserv=True)
book_1.reserv_book()
book_2 = Book("Умный", "Гоголь", 897, "67-08Н")
book_2.reserv_book()
book_3 = Book("Острый", "Пушкин", 500, "98-93К")
book_3.reserv_book()
book_4 = Book("Муму", "Иванов", 674, "56-08Р")
book_4.reserv_book()
book_5 = Book("Кто я?", "Лермантов", 234, "46-01о")
book_5.reserv_book()
#
shcool_book_1 = ShcoolBook("Алгебра", "Иванов", 100, "Математика", 9, "F-6CD", reserv=True)
shcool_book_1.reserv_book()
shcool_book_2 = ShcoolBook("Русский", "Петров", 234, "Алгебра", 11, "B-78D")
shcool_book_2.reserv_book()