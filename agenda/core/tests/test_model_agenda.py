from django.test import TestCase
from core.models import Agenda

class AgendaModelTest(TestCase):
    def setUp(self):
        self.agenda = Agenda.objects.create(
            nome_completo="João da Silva",
            telefone="(19) 99999-8888",
            email="joao.silva@example.com",
            observacao="Cliente importante, prefere contato por e-mail."
        )

    def test_agenda_criada_com_sucesso(self):
        self.assertEqual(self.agenda.nome_completo, "João da Silva")
        self.assertEqual(self.agenda.telefone, "(19) 99999-8888")
        self.assertEqual(self.agenda.email, "joao.silva@example.com")
        self.assertEqual(self.agenda.observacao, "Cliente importante, prefere contato por e-mail.")

    def test_str_retorna_nome_e_email(self):
        self.assertEqual(str(self.agenda), "João da Silva - joao.silva@example.com")

    def test_campos_podem_ser_editados(self):
        """Verifica se é possível atualizar um registro existente."""
        self.agenda.nome_completo = "João Pedro da Silva"
        self.agenda.telefone = "(19) 97777-6666"
        self.agenda.save()

        agenda_atualizada = Agenda.objects.get(pk=self.agenda.pk)
        self.assertEqual(agenda_atualizada.nome_completo, "João Pedro da Silva")
        self.assertEqual(agenda_atualizada.telefone, "(19) 97777-6666")

    def test_criacao_varios_contatos(self):
        """Verifica se o modelo suporta múltiplas entradas."""
        Agenda.objects.create(
            nome_completo="Maria Souza",
            telefone="(19) 91234-5678",
            email="maria.souza@example.com",
            observacao="Contato secundário."
        )
        total = Agenda.objects.count()
        self.assertEqual(total, 2)

    def test_observacao_pode_ser_vazia(self):
        """Verifica se o campo observação aceita string vazia."""
        contato = Agenda.objects.create(
            nome_completo="Carlos Almeida",
            telefone="(19) 93333-4444",
            email="carlos.almeida@example.com",
            observacao=""
        )
        self.assertEqual(contato.observacao, "")

    def test_email_unico_nao_e_exigido(self):
        """Confirma que o campo email não é definido como unique."""
        Agenda.objects.create(
            nome_completo="Outro João",
            telefone="(19) 95555-0000",
            email="joao.silva@example.com",  # mesmo e-mail
            observacao="Teste de duplicidade."
        )
        total = Agenda.objects.filter(email="joao.silva@example.com").count()
        self.assertEqual(total, 2)

    def test_exclusao_de_contato(self):
        """Verifica se um contato é realmente removido do banco."""
        pk = self.agenda.pk
        self.agenda.delete()
        self.assertFalse(Agenda.objects.filter(pk=pk).exists())

    def test_repr_retorna_str_legivel(self):
        """Verifica se o método __str__ retorna algo legível."""
        texto = str(self.agenda)
        self.assertIn("João da Silva", texto)
        self.assertIn("joao.silva@example.com", texto)

    