from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class Test1(TestCase):

    # Todo test debe iniciar con "test_" al principio
    def test_numero1(self):
        # Con reverse le pasamos el name de una url para poder indicar la ruta
        url = reverse("IndexName")

        # Indicamos que request tenga la respuesta de la petición
        request = self.client.get(url)

        # Hacemos la pregunta y el test
        self.assertEqual(request.status_code, 200)