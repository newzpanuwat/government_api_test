# -*- coding: utf-8 -*-
"""GovernmentAPI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V9wSzRhICKgbdxH5Kcqu-sksBwbhBrbb
"""

import requests
from pprint import  pprint


def SearchProject(key=''):
  # maybe bugs when fill params key into func
  token = 'paste your token from data.go.th'

  url = 'https://opend.data.go.th/govspending/cgdcontract'

  params = {
      'api-key': token,
      'year': 2562,
      'keyword': key
  }

  req = requests.get(url, params= params)

  allprojects = res['result']
  print('Count: ', len(allprojects))

  allbugdet = []

  for pj in allprojects:
    print('Project name: '+ pj['project_name'])
    print('Sum: ' + pj['sum_price_agree'])
    print('Department name: ' + pj['dept_name'])
    print('Price build: ' + pj['price_build']+ ' Baht')
    allbugdet.append(int(pj['sum_price_agree'].replace(',','')))
    print('---------------------')
  print('*************************************')
  print('ค้นหาคำว่า: {} งบประมาณทั้งหมด: {:,d} '.format(key, sum(allbugdet)))
  print('*************************************')

SearchProject()

