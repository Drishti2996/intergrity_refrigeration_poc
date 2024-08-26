from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product
import uuid
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django import forms


from django.shortcuts import render
import qrcode
import os


    
def landing_page(request, new_uuid):
  print("&&&&&&&&&&&&&&&&&")
  if request.method == 'POST':
    print("####################")
    button_action = request.POST.get('button_action')
    print(button_action)
    if button_action == 'update':
      return render(request, 'create_product.html', {'uuid': new_uuid})
    
    name = request.POST['name']
    description = request.POST['description']
    fridge_id = request.POST['fridge_id']
    model_number = request.POST['model_number']
    serial_number = request.POST['serial_number']
    purchase_date = request.POST['purchase_date']
    installation_date = request.POST['installation_date']
    warranty_expiry_date = request.POST['warranty_expiry_date']
    location = request.POST['location']

    try:

      print("here2")
      product = Product.objects.get(uuid=new_uuid) 
      product.name = name
      product.description = description
      product.fridge_id = fridge_id
      product.model_number = model_number
      product.serial_number = serial_number
      product.purchase_date = purchase_date
      product.installation_date = installation_date
      product.warranty_expiry_date = warranty_expiry_date
      product.location = location
      product.save()
      product_data = {
        'name': product.name,
        'description': product.description,
        'fridge_id':product.fridge_id,
        'model_number':product.model_number,
        'serial_number':product.serial_number,
        'purchase_date':product.purchase_date,
        'installation_date':product.installation_date,
        'warranty_expiry_date':product.warranty_expiry_date,
        'location':product.location
      }

      # Handle successful update
      return render(request, 'product_detail.html', {"product_data":product_data})
    except ObjectDoesNotExist:
      product = Product.objects.create(uuid=new_uuid) 
      product.name = name
      product.description = description
      product = Product.objects.get(uuid=new_uuid) 
      product.name = name
      product.description = description
      product.fridge_id = fridge_id
      product.model_number = model_number
      product.serial_number = serial_number
      product.purchase_date = purchase_date
      product.installation_date = installation_date
      product.warranty_expiry_date = warranty_expiry_date
      product.location = location
      
      product.save()
      product_data = {
        'name': product.name,
        'description': product.description,
        'fridge_id':product.fridge_id,
        'model_number':product.model_number,
        'serial_number':product.serial_number,
        'purchase_date':product.purchase_date,
        'installation_date':product.installation_date,
        'warranty_expiry_date':product.warranty_expiry_date,
        'location':product.location        

      }

      # Handle successful update
      return render(request, 'product_detail.html', {"product_data":product_data}) 
  else:
    try:
      product = Product.objects.get(uuid=new_uuid)
      print("***********************")
      print(new_uuid)
      print(product)
      product_data = {
        'name': product.name,
        'description': product.description,
        'fridge_id':product.fridge_id,
        'model_number':product.model_number,
        'serial_number':product.serial_number,
        'purchase_date':product.purchase_date,
        'installation_date':product.installation_date,
        'warranty_expiry_date':product.warranty_expiry_date,
        'location':product.location
      }
      return render(request, 'product_detail.html', {"product_data":product_data})
    except ObjectDoesNotExist:
      # Create a new product
      #product = Product.objects.create(uuid=new_uuid)
      return render(request, 'create_product.html', {'uuid': new_uuid})

   # else:
   #     form = SimpleForm()
   # return render(request, 'landing_page.html', {'form': form})
    
#def render_product_detail(product):
    
   
def register_product(request):
    if request.method == 'POST':
        # Handle form submission
        product = Product.objects.create()  # Create a new product with a UUID
        return HttpResponseRedirect(f'/product/{product.uuid}')
    else:
        # Display registration form
        return render(request, 'register_product.html')

def product_detail(request, product_uuid):
    product = Product.objects.get(uuid=product_uuid)
    # Process the product
 
    # Retrieve additional product information from the database (replace with your fields)
    product_data = {
        'name': product.name,
        'description': product.description,
    # ... other product details
    }
    return render(request, 'product_detail.html', {"product_data":product_data}) 
    #return HttpResponse("Hello, world. Product Detail")
    
def create_product(request, uuid):
    print("here")
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        try:
            print("here2")
            product = Product.objects.get(uuid=uuid)
            product.name = name
            product.description = description
            product.save()
            # Handle successful update, e.g., redirect or display a message
            #return HttpResponse("Hello, world. Product Detail") 
            return redirect('product_detail', product_uuid=uuid)
        except ObjectDoesNotExist:
            return HttpResponse("Hello, world. Product Detail") 
        #return HttpResponse("Product created")
    else:
        # Not a POST request, unlikely scenario, handle appropriately if needed
       	 return render(request, 'create_product.html', {'uuid': uuid})  # Or display an error
         #return HttpResponse("Hello, world. Create Product")


def generate_empty_qr_code(request):
    """Generates an empty QR code."""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    new_uuid = uuid.uuid4()
    #create url including this uuid
    # Add empty data
    base_url = "http://192.168.5.18:8000/poc/landing"
    full_url = f"{base_url}/{new_uuid}"
    print(full_url)
    qr.add_data(full_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    response = HttpResponse(content_type='image/png')
    img.save(response, "PNG")
    
    #os.makedirs(os.path.join('poc', 'static'), exist_ok=True)
    filename = f"qr_code_{new_uuid}"
    relative_path = '/home/drishti/Documents/integrity_refrigeration/poc/static'
    file_path = os.path.join(relative_path, filename)

 
  # Save the image to the specified filepath
    img.save(file_path, "PNG")
    
    return response

    

class SimpleForm(forms.Form):
    uuid_field = forms.CharField(label='Enter UUID')
    
    





