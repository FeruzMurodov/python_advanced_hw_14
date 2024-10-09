import unittest


class BookNotFoundError(Exception):
    pass


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title):
        if isinstance(title, str):
            self._books.append(title)
        else:
            raise TypeError()

    def remove_book(self, title):
        if title in self._books:
            self._books.remove(title)
        else:
            raise BookNotFoundError('There is no such a book in the library!')

    def list_books(self):
        return self._books


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.data = Library()

    def test_has_list(self):
        self.assertEqual(len(self.data._books), 0, "Something's wrong!")

    def test_add_book_norm(self):
        self.data.add_book("Harry Potter")
        self.assertIn('Harry Potter', self.data._books)

    def test_add_book_wrong(self):
        with self.assertRaises(TypeError):
            self.data.add_book(654654)

    def test_remove_book_norm(self):
        self.data.add_book("Harry Potter")
        self.data.remove_book("Harry Potter")
        self.assertNotIn("Harry Potter", self.data._books, "Something's wrong!")

    def test_remove_book_wrong(self):
        self.data.add_book("Harry Potter")
        with self.assertRaises(BookNotFoundError):
            self.data.remove_book("HarryPotter")

    def test_get_list_books(self):
        self.data.add_book("Harry Potter")
        self.assertEqual(self.data.list_books(), ['Harry Potter'], "Something's wrong!")


if __name__ == '__main__':
    unittest.main(verbosity=2)
