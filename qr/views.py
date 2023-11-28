from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from PIL import Image, ImageDraw, ImageFont
import os, sys
import pandas as pd
from googleapiclient.http import MediaFileUpload

sys.path.append('static')
from Google import Create_Service


def index(request):
    data = {'form':'Hello'}
    return render(request, 'templates/forms.html', data)
# HELLO TEST
# def generate_image(request):
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         print(text)
#     image = Image.open('check.png')
#     draw = ImageDraw.Draw(image)
#     text = "Hello, World!"
#     text_position = (350, 1450)
#     text_color = (0, 0, 0)
#     draw.text(text_position, text, fill=text_color)
#     image.save('output.png')
#         # image = Image.new('RGB', (300, 100), color='white')
#         # draw = ImageDraw.Draw(image)
#         # # font = ImageFont.truetype("path_to_font.ttf", size=24)
#         # text_position = (10, 10)
#         # draw.text(text_position, text, fill='black')
#     response = HttpResponse(content_type='image/png')
#         # image.save(response, 'PNG')
#     response['Content-Disposition'] = f'attachment; filename=output.png'    
#     return response
def download_image(request):
    if(request.method == 'POST'):
        data = request.POST.get('csv_update')
        text = request.POST.get('text')
    print("suikbu yugfyfufufu")
    print(data)
    image = Image.open(r'static/image.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('static/amanda.ttf', 150)
    text_position = (450, 1450)
    text_color = (0, 0, 0)
    draw.text(text_position, text, fill=text_color, font = font)
    response = HttpResponse(content_type = 'image/png')
    image.save(response,'PNG')
    response['Content-Disposition'] = f'attachment; filename = output.png'
    print(response)
    


    

    url='https://drive.google.com/file/d/1UP3s56N-_OlDRs7qg7uNN7RDCzW61ib5/view?usp=sharing'
    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    df = pd.read_csv(dwn_url)

    c = df.loc[2,"QR Code string"]
    c = c.split(' ')

    df.loc[2,"Roll No."] = data
    df.loc[2,"QR Code string"] = '16an7s5yetr'

    df.to_csv('qwe.csv',index=False)

    print(df.head())
    print(c)





    CLIENT_SECRET_FILE = 'static/client_secrets.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # Upload a file
    # file_metadata = {
    #     'name': 'test.csv',
    #     'parents': ['16GBCR5LKeZSU4RZJLJGy5VcAoJ6u76NF']
    # }

    # media_content = MediaFileUpload('qwe.csv', mimetype='text/csv')

    # file = service.files().create(
    #     body=file_metadata,

    #     media_body=media_content
    # ).execute()

    # print(file)


    # Replace Existing File on Google Drive
    file_id = '1yXMjI9luV2inZv6z5ttL7K5g3ctPGYhM'

    media_content = MediaFileUpload('qwe.csv', mimetype='text/csv')

    service.files().update(
        fileId=file_id,
        media_body=media_content
    ).execute()

    return response


def login(request):
    return render(request, 'login.html')