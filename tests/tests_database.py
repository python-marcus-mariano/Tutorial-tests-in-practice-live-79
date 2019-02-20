"""
Testes na prática

Live de Python #79 - Testes de unidade na prática

Homepage and documentation:


Copyright (c) 2018, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from unittest import TestCase, mock
from app.database import select_task

tasks  = [
    {'id': 1, 'task_name': 'Dormir',  'date': '??', 'state': 'TODO'},
    {'id': 2, 'task_name': 'Acordar',  'date': '??', 'state': 'TODO'},
    {'id': 3, 'task_name': 'Ligar pro Will',  'date': '??', 'state': 'TODO'},
    {'id': 4, 'task_name': 'Acordar',  'date': '??', 'state': 'TODO'},
    {'id': 5, 'task_name': 'Acordar',  'date': '??', 'state': 'Fazendo'}
]


class TestSelectTask(TestCase):
    """Classe Test Select Task."""

    @mock.patch('app.database.db', new=tasks)
    def test_select_task_deve_retornar_somente_task_acordar(self):
        """Testar Select Task Acordar."""
        results = select_task('Acordar', '')

        for result in results:
            with self.subTest(f'Acordar in {result}'):
                self.assertEqual('Acordar', result['task_name'])
    
    @mock.patch('app.database.db', new=tasks)
    def test_select_task_deve_retornar_somente_task_com_o_stage_fazendo(self):
        """Testar Select Task Fazendo."""
        results = select_task('', 'Fazendo')

        for result in results:
            with self.subTest(f'Fazendo in {result}'):
                self.assertEqual('Fazendo', result['state'])
        
        
