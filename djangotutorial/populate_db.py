import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from core.models import AIAuthor, NeuralNetworkType

# Clear existing data
AIAuthor.objects.all().delete()
NeuralNetworkType.objects.all().delete()

# Add AI Authors
ai_authors = [
    {
        'name': 'John McCarthy',
        'definition': 'La ciencia e ingeniería de crear máquinas inteligentes.',
        'year': '1956'
    },
    {
        'name': 'Stuart Russell y Peter Norvig',
        'definition': 'La IA es la capacidad de una máquina para imitar el comportamiento humano inteligente y realizar tareas que normalmente requieren inteligencia.',
        'year': '2003'
    },
    {
        'name': 'Marvin Minsky',
        'definition': 'La ciencia que hace máquinas capaces de resolver problemas que normalmente requieren inteligencia humana.',
        'year': '1986'
    }
]

for author_data in ai_authors:
    AIAuthor.objects.create(**author_data)
    print(f"Created AIAuthor: {author_data['name']}")

# Add Neural Network Types
nn_types = [
    {
        'name': 'Perceptrón',
        'description': 'El modelo más simple de una red neuronal artificial, consiste en una única capa de neuronas de entrada conectadas a una neurona de salida.',
        'use_case': 'Clasificación binaria, problemas linealmente separables',
        'icon': 'layer-group'
    },
    {
        'name': 'Redes Feedforward',
        'description': 'Las capas de neuronas están organizadas en una estructura de alimentación hacia adelante, donde la información fluye solo en una dirección, desde la entrada hacia la salida.',
        'use_case': 'Regresión, clasificación, reconocimiento de patrones',
        'icon': 'project-diagram'
    },
    {
        'name': 'Redes Convolucionales (CNN)',
        'description': 'Especializadas en procesar datos con estructura de cuadrícula, utilizan capas convolucionales para extraer características locales de manera eficiente.',
        'use_case': 'Visión por computadora, reconocimiento de imágenes, detección de objetos',
        'icon': 'image'
    },
    {
        'name': 'Redes Recurrentes (RNN)',
        'description': 'Diseñadas para procesar secuencias de datos, tienen conexiones que permiten que la información persista en el tiempo a través de retroalimentación.',
        'use_case': 'Procesamiento de lenguaje natural, series de tiempo, traducción automática',
        'icon': 'sync'
    },
    {
        'name': 'LSTM (Long Short-Term Memory)',
        'description': 'Una variante avanzada de RNN que resuelve el problema del desvanecimiento del gradiente, permitiendo que las redes aprendan dependencias a largo plazo.',
        'use_case': 'Generación de texto, análisis de series de tiempo, reconocimiento de voz',
        'icon': 'memory'
    },
    {
        'name': 'GANs (Generative Adversarial Networks)',
        'description': 'Consisten en dos redes que compiten entre sí: un generador que crea datos y un discriminador que intenta distinguir datos reales de generados.',
        'use_case': 'Generación de imágenes, sintetización de datos, enhancimiento de imágenes',
        'icon': 'dice'
    },
    {
        'name': 'Transformers',
        'description': 'Arquitectura basada en mecanismos de atención que procesa datos completos sin necesidad de recurrencia, permitiendo paralelización y mejor captura de dependencias a largo plazo.',
        'use_case': 'Procesamiento de lenguaje natural, traducción, modelado de lenguaje',
        'icon': 'cube'
    }
]

for nn_type_data in nn_types:
    NeuralNetworkType.objects.create(**nn_type_data)
    print(f"Created NeuralNetworkType: {nn_type_data['name']}")

print("\n✓ Base de datos poblada exitosamente!")
