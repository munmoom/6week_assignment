{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPmcOaVcU9EtwaQoVUKSaXM",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/6week_assignment/blob/main/1_202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GwiC2KSF9feL",
        "outputId": "fab227db-0555-4a7b-9b40-ff66370507b6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "0.1cm\n",
            "0.001m\n",
            "0.03937inch\n",
            "0.003281ft\n"
          ]
        }
      ],
      "source": [
        "def convertUnit(num) :\n",
        " CM = num*1/10\n",
        " M = num*1/1000\n",
        " INCH = num*3937/100000\n",
        " FT = num*3281/1000000\n",
        " print(str(CM) + 'cm')\n",
        " print(str(M) + 'm')\n",
        " print(str(INCH) + 'inch')\n",
        " print(str(FT) + 'ft')\n",
        "\n",
        "num = int(input())\n",
        "\n",
        "convertUnit(num)\n"
      ]
    }
  ]
}