import pandas as pd
student_data = [
    ['Tinu',24,'Sydney','Australia'],
  ['Ryan',32,'Delhi','India'],
  ['Viji',41,'Toronto','Canada'],
  ['Lu',22,'Washington','US'],
  ['John',16,'New York','US'],
  ['Mike',17,'Las vegas','US'],
    ]
data_frame = pd.DataFrame(student_data)

fees = [2000, 3000, 4000, 3500, 4500, 2900]

data_frame['fees'] = fees
data_frame = pd.DataFrame(student_data, columns = ['Name', 'Age','City','Country','fees'])
data_frame

