from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title=title
        self.author=author

    @abstractmethod
    def display():
        pass


class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        # Book.__init__(self, title, author)
        super().__init__(title, author)

    def display(self):
        print('Title: {}'.format(self.title))
        print('Author: {}'.format(self.author))
        print('Price: {}'.format(self.price))


title= 'The Alchemist' #input()
author='Paulo Coelho' #input()
price= 125 # int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
