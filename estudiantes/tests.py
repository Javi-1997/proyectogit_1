from django.test import TestCase
from estudiantes.models import Estudiante

# Create your tests here.
class EstudianteTests(TestCase):
    def test_largo_del_nombre(self):

        #probamos un estudiante con nombre corto y uno largo
        
        estudiante_nombre_valido = Estudiante.objects.create(
            nombre="pepas", apellido="pepona"
        )
        self.assertEqual(Estudiante.objects.all().count(),1)
        self.assertIsNone(estudiante_nombre_valido.id)

