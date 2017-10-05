from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Book
from ..Authors.models import Author

import datetime as dt
import json


class BooksTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author_1 = Author.objects.create(
            name='test_name_1',
            last_name='test',
            nacionalidad='MX',
            biography='kjdhkhlsdfsk.,df',
            gender='M',
            age=45,
            is_alive=True
        )
        self.book1 = Book.objects.create(
            title='Book_test_name',
            author=self.author_1,
            isbn='12345678',
            date_published=dt.datetime.now(),
            raiting=4.5,
            cover='jhgsjdgfjhdf',
            prologue='ahjsdhkjhdsf',
            literary_genre='DR',
            price=12.5
        )

    def test_get_book(self):
        response = self.client.get(reverse('books:list_books'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()[0].get('title', ''), self.book1.title)