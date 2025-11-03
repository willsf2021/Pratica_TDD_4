from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from core.forms import LoginForm, AgendaForm
from core.models import Agenda


class LoginFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="wilson",
            email="wilson@fatec.sp.gov.br",
            password="12345"
        )

    def test_login_form_valido(self):
        """Formulário de login deve ser válido com e-mail institucional e senha correta"""
        form_data = {
            'email': 'wilson@fatec.sp.gov.br',
            'password': '12345'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.user, self.user)

    def test_login_form_email_invalido(self):
        """Deve falhar se o e-mail não for institucional"""
        form_data = {
            'email': 'wilson@gmail.com',
            'password': '12345'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Informe seu e-mail institucional.', form.errors['email'][0])

    def test_login_form_usuario_nao_existe(self):
        """Deve falhar se o e-mail institucional não estiver cadastrado"""
        form_data = {
            'email': 'naoexiste@fatec.sp.gov.br',
            'password': '12345'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Usuário com esse e-mail não encontrado.', form.non_field_errors())

    def test_login_form_senha_errada(self):
        """Deve falhar se a senha estiver incorreta"""
        form_data = {
            'email': 'wilson@fatec.sp.gov.br',
            'password': 'senhaerrada'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Senha incorreta para o e-mail informado.', form.non_field_errors())


class AgendaFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'nome_completo': 'João da Silva',
            'telefone': '11999998888',
            'email': 'joao@example.com',
            'observacao': 'Cliente antigo'
        }

    def test_agenda_form_valido(self):
        """Formulário deve ser válido com todos os campos preenchidos"""
        form = AgendaForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_agenda_form_nome_obrigatorio(self):
        """Campo nome é obrigatório"""
        data = self.valid_data.copy()
        data['nome_completo'] = ''
        form = AgendaForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('Informe o nome completo do contato.', form.errors['nome_completo'][0])

    def test_agenda_form_telefone_obrigatorio(self):
        """Campo telefone é obrigatório"""
        data = self.valid_data.copy()
        data['telefone'] = ''
        form = AgendaForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('Informe o telefone do contato.', form.errors['telefone'][0])

    def test_agenda_form_email_invalido(self):
        """Campo e-mail deve ser válido"""
        data = self.valid_data.copy()
        data['email'] = 'emailinvalido'
        form = AgendaForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('Informe um endereço de email válido.', form.errors['email'][0])

    def test_agenda_form_salva_objeto(self):
        """Formulário deve salvar um contato corretamente"""
        form = AgendaForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        contato = form.save()
        self.assertIsInstance(contato, Agenda)
        self.assertEqual(contato.nome_completo, 'João da Silva')
