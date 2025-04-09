from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_protect
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Doctor
from PIL import Image, ImageDraw, ImageFont
import io
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def docindex(request):
    return render(request, 'docindex.html')





def cardiology(request):

    doctors = Doctor.objects.filter(specialization="Cardiology")
    print(f"Found {doctors.count()} cardiology doctors")
    for doc in doctors:
        print(f"Doctor: {doc.name}, Specialization: {doc.specialization}")

    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    
    context = {
        'doctors': doctors,
        'specializations': specializations
    }
    print(f"Found {doctors.count()} cardiology doctors")
    return render(request, 'cardiology.html', context)



def dentist(request):
    doctors = Doctor.objects.filter(specialization="Dentist")
    print(f"Found {doctors.count()} dentist doctors")

    for doc in doctors:
        print(f"Doctor: {doc.name}, Specialization: {doc.specialization}")

    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    
    context = {
        'doctors': doctors,
        'specializations': specializations
    }

    print(f"Found {doctors.count()} dentist doctors")
    return render(request, 'dentist.html', context)

def homeopathy(request):

    doctors = Doctor.objects.filter(specialization="Homeopathy")
    print(f"Found {doctors.count()} homeopathy doctors")
 
    for doc in doctors:
        print(f"Doctor: {doc.name}, Specialization: {doc.specialization}")

    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
 
    context = {
        'doctors': doctors,
        'specializations': specializations
    }

    print(f"Found {doctors.count()} homeopathy doctors")
    
    return render(request, 'homeopathy.html', context)


def neurology(request):

    doctors = Doctor.objects.filter(specialization="Neurology")
    print(f"Found {doctors.count()} neurology doctors")
 
    for doc in doctors:
        print(f"Doctor: {doc.name}, Specialization: {doc.specialization}")

    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    
    context = {
        'doctors': doctors,
        'specializations': specializations
    }

    print(f"Found {doctors.count()} neurology doctors")
    
    return render(request, 'neurology.html', context)


def pediatrics(request):

    doctors = Doctor.objects.filter(specialization="Pediatrics")
    print(f"Found {doctors.count()} pediatrics doctors")

    for doc in doctors:
        print(f"Doctor: {doc.name}, Specialization: {doc.specialization}")

    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
   
    context = {
        'doctors': doctors,
        'specializations': specializations
    }

    print(f"Found {doctors.count()} pediatrics doctors")
  
    return render(request, 'pediatrics.html', context)





def radiology(request):
    # Filter doctors with specialization "Radiology"
    doctors = Doctor.objects.filter(specialization="Radiology")
    print(f"Found {doctors.count()} radiology doctors")
    
    for doc in doctors:
        print(f"Doctor: {doc.name}, Specialization: {doc.specialization}")

    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    
    context = {
        'doctors': doctors,
        'specializations': specializations
    }

    print(f"Found {doctors.count()} radiology doctors")
    
    return render(request, 'radiology.html', context)



def traumatology(request):


    doctors = Doctor.objects.filter(specialization="Traumatology")
    print(f"Found {doctors.count()} traumatology doctors")
    
    
    for doc in doctors:
        print(f"Doctor: {doc.name}, Specialization: {doc.specialization}")

    
    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    
    
    context = {
        'doctors': doctors,
        'specializations': specializations
    }

    print(f"Found {doctors.count()} traumatology doctors")
    
  
    return render(request, 'traumatology.html', context)


def index(request):
    return render(request, 'index.html')

def doctor(request):
    return render(request, 'doctor.html')

def service(request):
    return render(request, 'service.html')

def department(request):
    return render(request, 'department.html')

def contact(request):
    return render(request, 'contact.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def blog(request):
    return render(request, 'blog-single.html')

def appoinment(request):
    return render(request, 'appoinment.html')

def about(request):
    return render(request, 'about.html')

def docabout(request):
    return render(request, 'docabout.html')

def docservice(request):
    return render(request, 'docservice.html')


def docdepartment(request):
    return render(request, 'docdepartment.html')



def doccontact(request):
    return render(request, 'doccontact.html')

def perdepartment(request):
    return render(request, 'perdepartment.html')

def placeholder_image(request, width, height):

    img = Image.new('RGB', (int(width), int(height)), color=(211, 211, 211))
    draw = ImageDraw.Draw(img)
    
 
    text = f"{width}x{height}"
    draw.text((int(width)/2 - 20, int(height)/2 - 10), text, fill=(100, 100, 100))
    

    img_io = io.BytesIO()
    img.save(img_io, format='JPEG')
    img_io.seek(0)
    return HttpResponse(img_io.getvalue(), content_type='image/jpeg')

def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "Email already exists!!"
            return render(request, 'signup.html', {'msg': msg})
        except User.DoesNotExist:
            if request.POST['password'] == request.POST['confirm_password']:
                usertype = request.POST.get('userType')
                
                if not usertype:
                    msg = "Please select user type (Patient or Doctor)!"
                    return render(request, 'signup.html', {'msg': msg})
                
                # Get profile image
                profile = None
                if 'profile' in request.FILES:
                    profile = request.FILES['profile']
                
                User.objects.create(
                    name=request.POST['name'], 
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                    usertype=usertype,
                    profile=profile
                )
                msg = "Signup successfully!!"
                return render(request, 'login.html', {'msg': msg})
            else:
                msg = "Password and confirm password doesn't match!!"
                return render(request, 'signup.html', {'msg': msg})

    return render(request, 'signup.html')




def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if user.password == request.POST['password']:
                request.session['email'] = user.email
                request.session['name'] = user.name
                request.session['usertype'] = user.usertype  
                
            
                if user.profile:
                    request.session['profile_pic'] = user.profile.url
                
           
                if user.usertype == "Doctor":
                    return redirect('docindex')
                else:  
                    return redirect('index')
            else:
                msg = "Incorrect Password"
                return render(request, 'login.html', {'msg': msg})
        except User.DoesNotExist:
            msg = "Email Not Registered"
            return render(request, 'login.html', {'msg': msg})
    return render(request, 'login.html')






def logout(request):
    del request.session['email']
    return redirect('login')



def otp(request):
    print(f"OTP view: Session ID: {request.session.session_key}")
    print(f"OTP view: Session contents: {dict(request.session)}")
    
    if 'email' not in request.session:
        return redirect('forgotpass')
        
    if request.method == "POST":
        try:
          
            stored_otp = request.session.get('otp')
      
            user_otp = request.POST.get('uotp', '')
            
      
            print(f"Stored OTP: {stored_otp}, Type: {type(stored_otp)}")
            print(f"User entered OTP: {user_otp}, Type: {type(user_otp)}")
            
        
            if stored_otp is None:
                msg = "OTP session expired. Please request a new OTP."
                return render(request, 'forgotpass.html', {'msg': msg})
       
            try:
                stored_otp = int(stored_otp)
                user_otp = int(user_otp)
            except ValueError:
                msg = "Please enter a valid numeric OTP!"
                return render(request, 'otp.html', {'msg': msg, 'email': request.session['email']})

            # Compare OTPs
            if stored_otp == user_otp:
         
                return redirect('newpass')
            else:
            
                msg = "Invalid OTP! Please check and try again."
                return render(request, 'otp.html', {'msg': msg, 'email': request.session['email']})

        except Exception as e:
            print(f"Error in OTP verification: {str(e)}")
            msg = "An error occurred. Please try again."
            return render(request, 'otp.html', {'msg': msg, 'email': request.session.get('email', '')})


    return render(request, 'otp.html', {'email': request.session.get('email', '')})





def forgotpass(request):
    if request.method == "POST":
        try:
            email = request.POST.get('email')
            if not email:
                msg = "Please enter an email address!"
                return render(request, 'forgotpass.html', {'msg': msg})
                
            user = User.objects.get(email=email)
            
            otp = random.randint(1001, 9999)
            subject = "OTP for Password Reset"
            message = f"""
                        Dear User,

                        We received a request to reset your password. Please use the One-Time Password (OTP) below to proceed with resetting your account password:

                        Your OTP: {otp}

                        This OTP is valid for the next 10 minutes. Please do not share this code with anyone for security reasons. If you did not request a password reset, please ignore this email or contact our support team immediately.

                        Thank you,  
                        DriveEasy Support Team
                        """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            
   
            send_mail(subject, message, email_from, recipient_list)
   
            request.session['email'] = user.email
            request.session['otp'] = str(otp)  
            request.session.modified = True
            
   
            print(f"Session ID: {request.session.session_key}")
            print(f"Session contents: {dict(request.session)}")
            print(f"OTP {otp} stored in session for {email}")
            
            return redirect('otp')

        except User.DoesNotExist:
            msg = "Invalid Email ID! This email is not registered."
            return render(request, 'forgotpass.html', {'msg': msg})
        except Exception as e:
            print(f"Error in forgot password: {str(e)}")
            msg = f"An error occurred: {str(e)}. Please try again."
            return render(request, 'forgotpass.html', {'msg': msg})

    return render(request, 'forgotpass.html')









def newpass(request):
    
    
    if 'email' not in request.session:
        return redirect('forgotpass')
        
    if request.method == "POST":
        try:
            email = request.session.get('email')
            user = User.objects.get(email=email)

         
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            
            print(f"New password: '{password}', Confirm password: '{cpassword}'") 

   
            if not password or not cpassword:
                msg = "Password cannot be empty!"
                return render(request, 'newpass.html', {'msg': msg})

            if password == cpassword:
         
                user.password = password
                user.save()
      
                request.session.flush()
                
                msg = "Password changed successfully! Please login with your new password."
                return render(request, 'login.html', {'msg': msg})
            else:
                msg = "New Password and Confirm Password do not match!"
                return render(request, 'newpass.html', {'msg': msg})

        except User.DoesNotExist:
            msg = "User not found. Please try again."
            return render(request, 'forgotpass.html', {'msg': msg})
        except Exception as e:
            print(f"Error in new password: {str(e)}")
            msg = "An error occurred. Please try again."
            return render(request, 'newpass.html', {'msg': msg})

    return render(request, 'newpass.html')






@csrf_exempt
def userprofile(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        request.session.flush()
        return redirect('login')

    if user.usertype == "Doctor":
        return redirect('docprofile')
    
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        
        if not all([name, mobile]):
            msg = "Please fill in all fields!"
            return render(request, 'userprofile.html', {'user': user, 'msg': msg})
        
        user.name = name
        user.mobile = mobile
        
        profile = request.FILES.get('profile')
        if profile:
       
            if user.profile:
                try:
                    user.profile.delete(save=False)
                except:
                    pass
            
            user.profile = profile
            user.save()
            
        
            import time
            request.session['profile_pic'] = f"{user.profile.url}?t={int(time.time())}"
          
            request.session.modified = True
        else:
            user.save()
            
        return redirect('index')
    
    return render(request, 'userprofile.html', {'user': user})

def docprofile(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        request.session.flush()
        return redirect('login')

    if user.usertype != "Doctor":
        return redirect('userprofile')
    
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        
        if not all([name, mobile]):
            msg = "Please fill in all fields!"
            return render(request, 'docprofile.html', {'user': user, 'msg': msg})
        
        user.name = name
        user.mobile = mobile
        
        profile = request.FILES.get('profile')
        if profile:
          
            if user.profile:
                try:
                    user.profile.delete(save=False)
                except:
                    pass
                    
            user.profile = profile
            user.save()
            
       
            import time
            request.session['profile_pic'] = f"{user.profile.url}?t={int(time.time())}"
            
            request.session.modified = True
        else:
            user.save()
            
        return redirect('docindex')
    
    return render(request, 'docprofile.html', {'user': user})


def changepass(request):
    user = User.objects.get(email=request.session.get('email'))
    
    template = 'changepass1.html' if user.usertype == "Doctor" else 'changepass.html'
    
    if request.method == "POST":
        opassword = request.POST.get('opassword', '').strip()
        npassword = request.POST.get('npassword', '').strip()
        cnpassword = request.POST.get('cnpassword', '').strip()
        
  
        if not all([opassword, npassword, cnpassword]):
            msg = "Please fill in all fields!"
        elif user.password != opassword:
            msg = "Old Password Does Not Match!"
        elif npassword != cnpassword:
            msg = "New Password and Confirm New Password do not match!"
        else:
            user.password = npassword
            user.save()
            return redirect('logout')
        
        return render(request, template, {'msg': msg, 'user': user})
    
    msg = "Please fill out the form to change your password."
    return render(request, template, {'msg': msg, 'user': user})



def adddoc(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.session.get('email'))
            
          
            required_fields = [
                'name', 'specialization', 'highest_qualification', 'position',
                'years_of_experience', 'languages', 'patients_treated',
                'consultation_fee', 'emergency_fee', 'surgery_fee'
            ]
            
            missing_fields = [field for field in required_fields if not request.POST.get(field, '').strip()]
            if missing_fields:
                msg = "Please fill in all required fields."
                return render(request, 'adddoc.html', {'msg': msg})
            
            Doctor.objects.create(
                user=user,
                name=request.POST['name'],
                specialization=request.POST['specialization'],
                highest_qualification=request.POST['highest_qualification'],
                position=request.POST['position'],
                years_of_experience=int(request.POST.get('years_of_experience', 0)),
                languages=request.POST['languages'],
                patients_treated=int(request.POST.get('patients_treated', 0)),
                biography=request.POST.get('biography', ''),
                profile_image=request.FILES.get('profile_image', None),
                consultation_fee=int(request.POST.get('consultation_fee', 0)),
                emergency_fee=int(request.POST.get('emergency_fee', 0)),
                surgery_fee=int(request.POST.get('surgery_fee', 0)),
                
                morning_availability=int(request.POST.get('morning_availability', 0)),
                afternoon_availability=int(request.POST.get('afternoon_availability', 0)),
                evening_availability=int(request.POST.get('evening_availability', 0)),
                
                telemedicine=request.POST.get('telemedicine') == "on",
                emergency_service=request.POST.get('emergency_service') == "on",
                home_visits=request.POST.get('home_visits') == "on",
                international_patients=request.POST.get('international_patients') == "on",
                insurance_accepted=request.POST.get('insurance_accepted') == "on",
                research_publications=request.POST.get('research_publications') == "on",
                multilingual=request.POST.get('multilingual') == "on",
                weekend_availability=request.POST.get('weekend_availability') == "on"
            )
            msg = "Application Submitted Successfully! Our team will review your credentials."
            return redirect('docindex') 
        
        except Exception as e:
            print("************", e)
            msg = "Error submitting application. Please try again."
            return render(request, 'adddoc.html', {'msg': msg})
    else:
        return render(request, 'adddoc.html')

def viewdoc(request):
 
    doctors = Doctor.objects.all()
    
  
    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    
    context = {
        'doctors': doctors,
        'specializations': specializations
    }
    
    return render(request, 'viewdoc.html', context) 

def docdoctor(request):

    doctors = Doctor.objects.all()
    
   
    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    
    context = {
        'doctors': doctors,
        'specializations': specializations
    }
    
    return render(request, 'docdoctor.html', context)

def cardiology_specialists(request):
  
    doctors = Doctor.objects.filter(specialization='Cardiology')
    
    context = {
        'doctors': doctors,
    }
    
    return render(request, 'cardiology.html', context)


def docdetails(request, doctor_id):
    try:
        
        doctor = Doctor.objects.get(id=doctor_id)
        return render(request, 'docdetails.html', {'doctor': doctor})
    except Doctor.DoesNotExist:
       
        return redirect('docdoctor')  #
    
    
def userdetails(request, doctor_id):
    try:
    
        doctor = Doctor.objects.get(id=doctor_id)
        return render(request, 'userdetails.html', {'doctor': doctor})
    except Doctor.DoesNotExist:
       
        return redirect('index')  
    
def userdoctor(request):
    
    doctors = Doctor.objects.all()
    
    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    
    context = {
        'doctors': doctors,
        'specializations': specializations
    }
    
    return render(request, 'userdoctor.html', context)   




def delete(request, pk):
    doctor = get_object_or_404(Doctor, id=pk)

  
    if request.method == 'POST':
        doctor.delete()
        return redirect('docindex')  

    return render(request, 'delete.html', {'doctor': doctor})



def updatedoc(request, pk):
    try:
  
        user = User.objects.get(email=request.session['email'])
  
        doctor = get_object_or_404(Doctor, pk=pk)
        
        if request.method == "POST":
        
            doctor.name = request.POST.get('name', doctor.name)
            doctor.specialization = request.POST.get('specialization', doctor.specialization)
            doctor.highest_qualification = request.POST.get('highest_qualification', doctor.highest_qualification)
            doctor.position = request.POST.get('position', doctor.position)
            doctor.years_of_experience = int(request.POST.get('years_of_experience', doctor.years_of_experience))
            doctor.languages = request.POST.get('languages', doctor.languages)
            doctor.patients_treated = int(request.POST.get('patients_treated', doctor.patients_treated))
            doctor.biography = request.POST.get('biography', doctor.biography)
            doctor.consultation_fee = int(request.POST.get('consultation_fee', doctor.consultation_fee))
            doctor.emergency_fee = int(request.POST.get('emergency_fee', doctor.emergency_fee))
            doctor.surgery_fee = int(request.POST.get('surgery_fee', doctor.surgery_fee))
            
       
            doctor.morning_availability = int(request.POST.get('morning_availability', doctor.morning_availability))
            doctor.afternoon_availability = int(request.POST.get('afternoon_availability', doctor.afternoon_availability))
            doctor.evening_availability = int(request.POST.get('evening_availability', doctor.evening_availability))
            
        
            doctor.telemedicine = request.POST.get('telemedicine') == "on"
            doctor.emergency_service = request.POST.get('emergency_service') == "on"
            doctor.home_visits = request.POST.get('home_visits') == "on"
            doctor.international_patients = request.POST.get('international_patients') == "on"
            doctor.insurance_accepted = request.POST.get('insurance_accepted') == "on"
            doctor.research_publications = request.POST.get('research_publications') == "on"
            doctor.multilingual = request.POST.get('multilingual') == "on"
            doctor.weekend_availability = request.POST.get('weekend_availability') == "on"
            
            # Profile image upload
            if 'profile_image' in request.FILES:
                doctor.profile_image = request.FILES['profile_image']
            
            
            doctor.save()
            
            msg = "Doctor information updated successfully!"
            return redirect('docdetails', doctor_id=pk)
            
        else:
            return render(request, 'updatedoc.html', {'doctor': doctor})
            
    except Exception as e:
        print("************", e)
        msg = "Error updating doctor information. Please try again."
        return render(request, 'updatedoc.html', {'msg': msg, 'doctor': doctor})
    
    
    
    
    
    
    
    
    
    
    
    
def book_appointment(request):
    if request.method == 'POST':
        try:
        
            if 'email' not in request.session:
                messages.error(request, "Please log in first")
                return redirect('login')
          
            user = User.objects.get(email=request.session['email'])
      
            doctor_id = request.POST.get('doctor')
            specialization = request.POST.get('specialization')
            name = request.POST.get('name', user.name)
            mobile = request.POST.get('mobile', '')
            reason = request.POST.get('reason', '')
            
          
            print(f"Form data received: doctor_id={doctor_id}, specialization={specialization}, name={name}")
            
      
            if not doctor_id:
                messages.error(request, "Please select a doctor")
                return redirect('appoinment')
                
            doctor = Doctor.objects.get(id=doctor_id)
            
         
            booking = Booking(
                user=user,
                doctor=doctor,
                specialization=specialization or doctor.specialization,
                name=name,
                mobile=mobile,
                reason=reason,
                appointment=True
            )
            booking.save()
            
       
            messages.success(request, "Appointment booked successfully!")
            return redirect('appoinment')
            
        except Doctor.DoesNotExist:
            messages.error(request, "Selected doctor does not exist")
            return redirect('appoinment')
        except Exception as e:
       
            print(f"Exception in booking appointment: {str(e)}")
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('appoinment')
    
    specializations = Doctor.objects.values_list('specialization', flat=True).distinct()
    doctors = Doctor.objects.all()
    
    return render(request, 'appoinment.html', {
        'doctors': doctors,
        'specializations': specializations
    })
    
    
def doctor_appointments(request):
    if 'email' not in request.session:
        messages.error(request, "Please log in first")
        return redirect('login')
    
    try:
        # First get the user by email
        user = User.objects.get(email=request.session['email'])
        
        # Get all doctors associated with this user
        doctors = Doctor.objects.filter(user=user)
        
        if not doctors.exists():
            messages.error(request, "You are not registered as a doctor")
            return redirect('docindex')
        
        # If there are multiple doctors, either:
        # Option 1: Show appointments for all of the user's doctor profiles
        all_appointments = []
        for doctor in doctors:
            appointments = Booking.objects.filter(doctor=doctor, appointment=True)
            all_appointments.extend(appointments)
        
        # Alternative option: Get the doctor ID from the request if provided
        doctor_id = request.GET.get('doctor_id')
        active_doctor = None
        
        if doctor_id:
            try:
                active_doctor = doctors.get(id=doctor_id)
            except Doctor.DoesNotExist:
                # If specified doctor doesn't exist or doesn't belong to user
                messages.error(request, "Invalid doctor selection")
                active_doctor = doctors.first()  # Default to first doctor
        else:
            active_doctor = doctors.first()  # Default to first doctor
        
        # Get appointments for the active doctor
        active_doctor_appointments = Booking.objects.filter(doctor=active_doctor, appointment=True)
        
        context = {
            'user': user,
            'doctors': doctors,
            'active_doctor': active_doctor,
            'appointments': active_doctor_appointments,
            'all_appointments': all_appointments
        }
        
        return render(request, 'docappoinment.html', context)
    
    except User.DoesNotExist:
        messages.error(request, "User not found")
        return redirect('login')
    except Exception as e:
        print(f"Exception in doctor appointments: {str(e)}")
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('docindex')
    
def appointment_detail(request, appointment_id):
    if 'email' not in request.session:
        messages.error(request, "Please log in first")
        return redirect('login')
    
    try:
        # First get the user
        user = User.objects.get(email=request.session['email'])
        
        # Get all doctors associated with this user
        doctors = Doctor.objects.filter(user=user)
        
        if not doctors.exists():
            messages.error(request, "You are not registered as a doctor")
            return redirect('docindex')
        
        # Get doctor IDs for this user
        doctor_ids = doctors.values_list('id', flat=True)
        
        # Get the specific appointment, ensuring it belongs to one of the user's doctor profiles
        appointment = Booking.objects.get(id=appointment_id, doctor__id__in=doctor_ids)
        
        context = {
            'appointment': appointment
        }
        
        return render(request, 'appointment_detail.html', context)
    
    except User.DoesNotExist:
        messages.error(request, "User not found")
        return redirect('login')
    except Booking.DoesNotExist:
        messages.error(request, "Appointment not found or you don't have permission to view it")
        return redirect('docappoinment')
    except Exception as e:
        print(f"Exception in appointment detail: {str(e)}")
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('docappoinment')