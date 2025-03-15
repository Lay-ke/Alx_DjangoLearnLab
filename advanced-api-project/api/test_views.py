from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from .serializers import BookSerializer
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Author')
        self.book = Book.objects.create(title='Test Book', author=self.author, publication_year=2021)
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        new_author = Author.objects.create(name='New Author')
        data = {'title': 'New Book', 'author': new_author.id, 'publication_year': 2022}
        url = reverse('create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_list_books(self):
        url = reverse('list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        url = reverse('detail', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        updated_author = Author.objects.create(name='Updated Author')
        url = reverse('update', args=[self.book.id])
        data = {'title': 'Updated Book', 'author': updated_author.id, 'publication_year': 2023}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
        self.assertEqual(self.book.author.name, 'Updated Author')

    def test_delete_book(self):
        url = reverse('delete', args=[self.book.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = reverse('list') + '?title=Test Book'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_search_books(self):
        url = reverse('list') + '?search=Author'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author.id)

    def test_order_books(self):
        another_author = Author.objects.create(name='Another Author')
        Book.objects.create(title='Another Book', author=another_author, publication_year=2020)
        url = reverse('list') + '?ordering=publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
        self.assertEqual(response.data[1]['publication_year'], 2021)

    def test_partial_update_book(self):
        url = reverse('update', args=[self.book.id])
        data = {'title': 'Partially Updated Book', 'publication_year': 2023}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Partially Updated Book')

    def test_create_book_without_authentication(self):
        self.client.logout()
        new_author = Author.objects.create(name='New Author')
        data = {'title': 'New Book', 'author': new_author.id, 'publication_year': 2022}
        url = reverse('create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)


