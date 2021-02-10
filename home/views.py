from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from.forms import *
from django.core.mail import send_mail,BadHeaderError
from django.views.decorators.csrf import csrf_exempt
# MERCHANT_KEY='34GORSrcLITE3vGw'
# from paytm import checksum
# Create your views here.

def ContactView(request):
    if request.method=='POST':
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['msg']
        from_email = 'rohitjain064@gmail.com'
        form_name=str(name).upper()

        contact = Contact(name=name, phone_no=phone_no, email=email, subject=subject, msg=msg)
        try:
            send_mail(
                subject,
                f''' Thanks for contacting us {form_name}.We will be in touch with you shortly

                Regards
                Kapoor Dental Hub
                ''',
                from_email,
                [email],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        contact.save()

    return render(request,'home/contact.html')



def index(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')


def gallery(request):
    gs=Gallery.objects.all()
    context={
        'gallerys':gs
    }
    return render(request,'home/gallery.html',context)

def single(request):
    return render(request,'home/single.html')

def blog(request):
    return render(request,'home/blog.html')

def service(request):
    services=Service.objects.all()
    return render(request,'home/service.html',{'services':services})

def appointment(request):
    if request.method=='POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
    order=form.cleaned_data.get('order')
    amount=form.cleaned_data.get('amount')
    email=form.cleaned_data.get('email')

    context={
        'form':form
    }
    param_dict = {

        'MID': 'TVHseG00634857275738',
        'ORDER_ID': str(order),
        'TXN_AMOUNT': str(amount),
        'CUST_ID': email,
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL': 'http://127.0.0.1:80/ap/handlerequest/',

    }
    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)

    return render(request,'home/appointment.html',context)


# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]
#
#     verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'home/paymentstatus.html', {'response': response_dict})