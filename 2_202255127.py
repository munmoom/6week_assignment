{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "2-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyOpfN8sVqnmeHBXl8ycSllB",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/6week_assignment/blob/main/2_202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9bCjFdfPDSe7",
        "outputId": "2b43279d-09f6-4da9-b9e1-b9478da69d4d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "===가위/바위/보 게임을 시작합니다.===\n",
            "===5판 3선증제입니다.===\n",
            "===1번째 판===\n",
            "1.가위 2.바위 3.보 >> 1\n",
            "2\n",
            "현재 스코어: 0:0\n",
            "===2번째 판===\n",
            "1.가위 2.바위 3.보 >> 2\n",
            "1\n",
            "현재 스코어: 0:0\n",
            "===3번째 판===\n",
            "1.가위 2.바위 3.보 >> 3\n",
            "3\n",
            "현재 스코어: 0:0\n",
            "===4번째 판===\n",
            "1.가위 2.바위 3.보 >> 4\n",
            "2\n",
            "현재 스코어: 0:0\n",
            "===5번째 판===\n",
            "1.가위 2.바위 3.보 >> 5\n",
            "1\n",
            "현재 스코어: 1:0\n"
          ]
        }
      ],
      "source": [
        "print('===가위/바위/보 게임을 시작합니다.===')\n",
        "print('===5판 3선증제입니다.===')\n",
        "\n",
        "from random import randint\n",
        "\n",
        "n = 0\n",
        "c = 0\n",
        "\n",
        "i = 0\n",
        "for i in range (1,6):\n",
        " print(f'==={i}번째 판===')\n",
        " print(f'1.가위 2.바위 3.보 >> {i}')\n",
        " user = int(input())\n",
        " com = randint(1,3) \n",
        " print(f'현재 스코어: {n}:{c}')\n",
        " if com == 1 and user == 2 or com == 3 and user == 1 or com == 2 and user == 3:\n",
        "  n += 1\n",
        "  if n==3:\n",
        "     break\n",
        "     print('당신이 이겼습니다!')\n",
        "  else:\n",
        "    continue\n",
        "\n",
        "  if com == 2 and user == 1 or com == 1 and user == 3 or com == 3 and user == 2:\n",
        "    c +=1\n",
        "    if n==3:\n",
        "     break\n",
        "     print('당신이 졌습니다!')\n",
        "    else:\n",
        "     continue"
      ]
    }
  ]
}