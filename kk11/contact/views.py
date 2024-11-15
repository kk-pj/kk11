#kk11
from django.shortcuts import render, redirect# 追加
import os
""" 追加でインポート"""
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail,EmailMessage


""" 一覧画面"""
def index(request):
    return render(request, 'contact/index.html')


""" お問い合わせフォーム画面"""
def contact_form(request):

    try:
        if request.method == 'POST':
            picture = request.FILES.get('img')

            fname = './media/img/' + picture.name
            f =  open(fname,'wb+') 
            for chunk in picture.chunks():
                f.write(chunk) 
            f.close()


            subject = "sample"
            message = request.POST.get('message')
            sender = "y@gmail.com"
            recipients = [settings.EMAIL_HOST_USER]
            mail = EmailMessage(subject, message, sender, recipients)


            try:
                mail.attach_file(fname)
                mail.send()

            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')


            return redirect('contact:complete')

    except:
        return render(request, 'contact/contact_form.html',)

    return render(request, 'contact/contact_form.html')


""" 送信完了画面"""
def complete(request):
    return render(request, 'contact/complete.html')