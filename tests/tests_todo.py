"""
Testes na prática

Live de Python #79 - Testes de unidade na prática

Homepage and documentation:


Copyright (c) 2018, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from app.todo import nova_task, process_date, listar_task

from unittest import TestCase, mock
from datetime import datetime

"""
{
    'id': int,
    'task_name': str,
    'date': datetime.datetime,
    'state': str['TODO', 'Fazendo', 'Pronto']
}

"""


class TestNovaTask(TestCase):
    """Classe Test Nova Task."""
    def test_nova_task(self):
        """Testar Nova Task."""
        esperado = {
            'id': 1,
            'task_name': 'Ligar pro Will',
            'date': datetime(2019, 2, 19, 0, 0, 0),
            'state': 'TODO'
        }
        result = nova_task('Ligar pro Will', '19/02/2019')
        
        self.assertEqual(esperado, result)
    
    @mock.patch('app.todo.process_date', return_value=123)
    def test_process_date_deve_ser_chamado_com_19_02_2019(self, mocked):
        """Testar process date chama 19/02/2019."""

        # chama a função
        # Dummy é  a string vazia: ''
        result = nova_task('', '19/02/2019')

        # Garante que a função interna foi chamada
        # mock usado para criar um spy
        mocked.assert_called_with('19/02/2019')

        # Garantir se o resultado está no contexto
        # com isso deixa de ser um spy e se torna um mock
        self.assertEqual(result['date'], 123)

    @mock.patch('app.todo.insert_task')    
    def test_insert_task_deve_ser_chamado_com_o_objeto_da_task(self, mocked):
        """Testar process date chama 19/02/2019."""        
        result = nova_task('', '19/02/2019')

        mocked.assert_called_with(result)


class TestProcessDate(TestCase):
    """Classe Test Process Date."""
    def test_process_date_deve_converter_para_datetime_a_string_passada(self):
        """Testar Process Date.

        19/02/2019 -> datetime(2019, 02, 19, 0, 0, 0)
        """
        esperado = datetime(2019, 2, 19, 0, 0, 0)
        
        result = process_date('19/02/2019')

        self.assertEqual(esperado, result)


class TestListarTask(TestCase):
    """Classe Test Listar Task."""
    def test_listar_task(self):
        """Testar Listar Task."""
        ...
