

from django.shortcuts import render

def contact_page(request):
    context = {
        'name': 'Onwudike Uche .C.',
        'email': 'Onwudikeu@gmail.com',
        'message': 'Welcome to my Contact page for TechRise Cohort 5!',
        'dob': '27th October, 1991',
        'title': 'Photographer and Web Developer',
        'twitter': '@Uonwudike',
        'instagram': 'itz_o.r.i.s',
        'whatsapp': '+234-812-476-4217'
        
        
    }
    return render(request, 'contact_page.html', context)
# 

