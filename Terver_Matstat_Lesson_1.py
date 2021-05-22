{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import factorial as fl\n",
    "def combinations(n,k):\n",
    "    return int(fl(n)/(fl(k)*fl(n-k)))\n",
    "def arrangements(n,k):\n",
    "    return int(fl(n)/fl(n-k))\n",
    "def permutations(n):\n",
    "    return int(fl(n))\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "А) Число благоприятных( сочетания 4ех карт из всех крести делим на общее число сочетаний)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0026410564225690276"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clubs = combinations(13,4)/combinations(52,4)\n",
    "clubs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Б) Найдем колличество комбинаций тузов"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4, 6, 4, 1)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ace1=combinations(4,1)\n",
    "ace2=combinations(4,2)\n",
    "ace3=combinations(4,3)\n",
    "ace4=combinations(4,4)\n",
    "ace1,ace2,ace3,ace4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Т.к. тузы занимают 1,2,3,4 карты из нужной выборки, найдем оставшиеся комбинации для 3,2,1,0 карт"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(17296, 1128, 48, 1)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "withoutace1=combinations(48,3)\n",
    "withoutace2=combinations(48,2)\n",
    "withoutace3=combinations(48,1)\n",
    "withoutace4=combinations(48,0)\n",
    "withoutace1,withoutace2,withoutace3,withoutace4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Cложим их произведения и поделим на общее кол-во комбинаций"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.2812632745405855"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fullP=((ace1*withoutace1)+(ace2*withoutace2)+(ace3*withoutace3)+(ace4*withoutace4))/combinations(52,4)\n",
    "fullP"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2.На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.008333333333333333"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p = 1/combinations(10,3)\n",
    "p"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3.В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.18461538461538457"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P= (9/15)*(8/14)*(7/13)\n",
    "P"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4.В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.00040404040404040404"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "winable=combinations(2,2)\n",
    "withoutwin=combinations(98,0)\n",
    "P=(winable+withoutwin)/combinations(100,2)\n",
    "P"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
