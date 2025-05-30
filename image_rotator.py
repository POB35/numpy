{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP91LUp63Y+UOMRA4BgjwxW",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/POB35/numpy/blob/main/image_rotator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-5nDOFcG5wae"
      },
      "outputs": [],
      "source": [
        "# image_rotator.py\n",
        "\n",
        "from PIL import Image # importa el módulo Image de la librería PIL\n",
        "\n",
        "# carga una imagen llamada 'tripleten_logo.jpeg'.\n",
        "im = Image.open('tripleten_logo.jpeg')\n",
        "\n",
        "# obtén el tamaño de la imagen mediante el atributo .size y muéstralo\n",
        "print(im.size)\n",
        "\n",
        "# gira la imagen 90 grados en sentido contrario a las agujas del reloj\n",
        "rotated = im.rotate(90)\n",
        "\n",
        "# guarda la imagen girada\n",
        "rotated.save('rotated.png')"
      ]
    }
  ]
}