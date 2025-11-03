from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Agenda


class ViewsTestCase(TestCase):
    def setUp(self):

        self.client = Client()

        self.user = User.objects.create_user(username='wilson', password='12345')
        
        self.contact = Agenda.objects.create(
            nome_completo="João da Silva",
            telefone="11999998888",
            email="joao@example.com",
            observacao="Contato importante"
        )

    def test_home_autenticado(self):
        """Página home acessível para usuários autenticados"""
        self.client.login(username='wilson', password='12345')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_create_contact(self):
        """Criação de contato via formulário"""
        self.client.login(username='wilson', password='12345')
        response = self.client.post(reverse('create'), {
            'nome_completo': 'Maria Oliveira',
            'telefone': '11988887777',
            'email': 'maria@example.com',
            'observacao': 'Nova cliente'
        })
        self.assertRedirects(response, reverse('list'))
        self.assertTrue(Agenda.objects.filter(nome_completo='Maria Oliveira').exists())

    def test_list_contacts(self):
        """Lista de contatos é renderizada"""
        self.client.login(username='wilson', password='12345')
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_contacts.html')
        self.assertContains(response, 'João da Silva')

    def test_detail_contact(self):
        """Página de detalhes de um contato"""
        self.client.login(username='wilson', password='12345')
        response = self.client.get(reverse('detail', args=[self.contact.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_contact.html')
        self.assertContains(response, self.contact.nome_completo)

    def test_update_contact(self):
        """Atualização de contato existente"""
        self.client.login(username='wilson', password='12345')
        response = self.client.post(reverse('update', args=[self.contact.pk]), {
            'nome_completo': 'João da Silva Atualizado',
            'telefone': '11900009999',
            'email': 'joao2@example.com',
            'observacao': 'Atualizado'
        })
        self.assertRedirects(response, reverse('detail', args=[self.contact.pk]))
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.nome_completo, 'João da Silva Atualizado')

    def test_delete_contact(self):
        """Exclusão de contato"""
        self.client.login(username='wilson', password='12345')
        response = self.client.post(reverse('delete', args=[self.contact.pk]))
        self.assertRedirects(response, reverse('list'))
        self.assertFalse(Agenda.objects.filter(pk=self.contact.pk).exists())

    def test_delete_contact_get(self):
        """Página de confirmação de exclusão"""
        self.client.login(username='wilson', password='12345')
        response = self.client.get(reverse('delete', args=[self.contact.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_contact.html')
        self.assertContains(response, self.contact.nome_completo)
