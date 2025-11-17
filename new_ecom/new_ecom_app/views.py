from django.shortcuts import render ,redirect
from new_ecom_app.models import student
from django.http import HttpResponse
# Create your views here.
def index(request):
    content={}
    content['data'] = student.objects.all()
    return render(request, 'index.html', content)

def forms(request):
        if request.method == 'POST':
            name = request.POST['name']
            dob = request.POST['dob']
            address = request.POST['address']
            email = request.POST['email']
            phone = request.POST['phone']
            t1=student.objects.create(name=name,dob=dob,address=address,email=email,phone=phone)
            # print(t1)
            # return HttpResponse("Data submitted successfully")
            t1.save()
            # You can add code here to save the data to the database if needed
            return redirect('/index')  # Redirect to a success page or another view
        else:
            return render(request, 'index.html')
        


def delete(request, id):
    student.objects.get(id=id).delete()
    return redirect('/index')