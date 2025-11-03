from django.test import TestCase
from django.urls import reverse, resolve
from core import views
from django.contrib.auth import get_user_model
from core.models import Agenda

User = get_user_model()


class UrlsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="orlando",
            email="orlando@fatec.sp.gov.br",
            password="senha123"
        )
        self.client.login(username="orlando", password="senha123")
        
        self.contact = Agenda.objects.create(
            nome_completo="Maria Souza",
            telefone="(19) 91234-5678",
            email="maria.souza@example.com",
            observacao="Contato de teste."
        )

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.login)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logout)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.home)

    def test_create_contact_url_resolves(self):
        url = reverse('create')
        self.assertEqual(resolve(url).func, views.create_contact)

    def test_list_contacts_url_resolves(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func, views.list_contacts)

    def test_detail_contact_url_resolves(self):
        url = reverse('detail', args=[self.contact.pk])
        self.assertEqual(resolve(url).func, views.detail_contact)

    def test_update_contact_url_resolves(self):
        url = reverse('update', args=[self.contact.pk])
        self.assertEqual(resolve(url).func, views.update_contact)

    def test_delete_contact_url_resolves(self):
        url = reverse('delete', args=[self.contact.pk])
        self.assertEqual(resolve(url).func, views.delete_contact)

    def test_protected_views_redirect_if_not_logged_in(self):
        """Verifica se páginas protegidas redirecionam para login."""
        self.client.logout()
        urls_protegidas = [
            'index', 'home', 'create', 'list', 'detail', 'update', 'delete'
        ]
        for nome in urls_protegidas:
            if nome in ['detail', 'update', 'delete']:
                url = reverse(nome, args=[self.contact.pk])
            else:
                url = reverse(nome)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertIn('/login/', response.url)
