from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    context = {'success_message': ''}

    if request.method == "POST":
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject,
                message,
                'muaztalib345@gmail.com',
                [to_email],
            )
            context['success_message'] = 'Email sent successfully!'
        except Exception as e:
            context['success_message'] = f'Error sending email: {e}'

    return render(request, 'contact.html', context)

def Blog(request):
    return render(request, 'blog-single.html', {})

def details(request):
    return render(request, 'portfolio-details.html', {})

def news(request):
    return render(request, 'news-single.html', {})

def services(request):
    return render(request, 'services.html')

def ambulance(request):
    return render(request, 'ambulance.html')

def appointment(request):
    context = {'success_message': ''}

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        schedule = request.POST.get('schedule')
        date = request.POST.get('date')
        message = request.POST.get('message')

        # Construct the subject and message for the email
        subject = f"New Appointment Request from {name}"
        message_body = f"""
        Appointment Details:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Department: {department}
        Doctor: {doctor}
        Schedule: {schedule}
        Date: {date}
        Message: {message}
        """

        try:
            send_mail(
                subject,
                message_body,
                email,  # From email (dynamic based on form input)
                ['recipient@example.com'],  # Recipient email (replace with your actual recipient)
            )
            context['success_message'] = 'Email sent successfully!'
        except Exception as e:
            context['success_message'] = f'Error sending email: {e}'

        # Add the form data to the context to display in the template
        context.update({
            'name': name,
            'email': email,
            'phone': phone,
            'department': department,
            'doctor': doctor,
            'schedule': schedule,
            'date': date,
            'message': message,
        })

    return render(request, 'appointment.html', context)

def Error_404(request):
    return render(request, '404.html')