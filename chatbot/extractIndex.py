{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "import re\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "f = open('example.txt','r', encoding = 'cp949')\n",
    "df = pd.DataFrame(columns=['keyword', 'number'])\n",
    "\n",
    "while True:\n",
    "    lines = f.readlines()\n",
    "    if not lines:\n",
    "          break\n",
    "    for line in lines:\n",
    "        #텍스트파일 전처리\n",
    "        if '페이지' in line:\n",
    "            line = line[0:0]\n",
    "        if 'Index' in line:\n",
    "            line = line[0:0]\n",
    "        if ''.join(line.split(',')).strip() == '':\n",
    "            continue\n",
    "        line = line[:-1]            \n",
    "\n",
    "        #'문자, 공백, 숫자'정규표현식으로 경계 표현\n",
    "        #페이지 수가 여러개 일 때 첫번째 경계가 키워드와 페이지를 나누는 것이다. \n",
    "        bou = re.findall(r'\\D\\s\\d',line)\n",
    "        if bou:\n",
    "            bound = bou[0]\n",
    "            tmp = line.find(bound)\n",
    "            num = line[tmp+2:]\n",
    "            key = line[:tmp+1]\n",
    "\n",
    "            \n",
    "        df = df.append(pd.DataFrame([[key, num]], columns=['keyword', 'number']), ignore_index=True)\n",
    "\n",
    "df.to_csv('keyword_number_list.csv', index=False, encoding='cp949')        \n",
    "   \n",
    "f.close()"
   ]
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
