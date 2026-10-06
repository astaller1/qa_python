from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    import pytest

    @pytest.mark.parametrize('title', [
        'А', 
        'Преступление и наказание', 
        'Название, в котором ровно сорок символов'
    ])
    def test_add_new_book_valid_title_length(self, title):
        collector = BooksCollector()

        collector.add_new_book(title)

        assert title in collector.books_genre

    @pytest.mark.parametrize('invalid_title', [
        '',
        'Название содержит ровно сорок один символ'
    ])
    def test_add_new_book_invalid_title_length(self, invalid_title):
        collector = BooksCollector()

        collector.add_new_book(invalid_title)

        assert invalid_title not in collector.books_genre

    def test_add_new_book_dublicate_not_allowed(self):
        collector = BooksCollector()

        collector.add_new_book('Возрождение')
        collector.add_new_book('Возрождение')

        assert len(collector.books_genre) == 1

    def test_set_book_genre_book_exists_and_genre_exists(self):
        collector = BooksCollector()

        collector.add_new_book('Снеговик')
        collector.set_book_genre('Снеговик', 'Детективы')

        assert collector.books_genre['Снеговик'] == 'Детективы'

    def test_get_book_genre_book_and_genre_correctly_matched(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_filtration(self):
        collector = BooksCollector()

        collector.add_new_book('Снеговик')
        collector.set_book_genre('Снеговик','Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Снеговик']

    def test_get_books_genre_returns_current_dict(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')

        assert collector.get_books_genre() == {'Оно': ''}

    def test_get_books_for_children_returns_only_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert 'Гарри Поттер' in collector.get_books_for_children() and 'Оно' not in collector.get_books_for_children()

    def test_add_book_in_favorites_successfully_adds_book(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')

        assert 'Оно' in collector.favorites

    def test_delete_book_from_favorites_successfully_removes_book(self):
        collector = BooksCollector()

        collector.add_new_book('Возрождение')
        collector.add_book_in_favorites('Возрождение')
        collector.delete_book_from_favorites('Возрождение')
        
        assert 'Возрождение' not in collector.favorites

    def test_get_list_of_favorites_books_shows_current_favorite_list(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')

        assert 'Оно' not in collector.get_list_of_favorites_books()
