from django.shortcuts import render,HttpResponse
from .models import FileUpload
from .forms import UploadForm

value = ''

def index(request):
    return render(request,"index.html")

def checkDuplication(request):
    string = request.GET.get('text','default')
    # print(string)
    duplicated = ""
    for char in string:
        if char not in duplicated:
            duplicated=duplicated+char
    #print(duplicated)
    params = {'duplicated_text': duplicated}
    return render(request,"duplicate.html",params)
    
def commas(request):
    num = request.POST.get('text','---')
    def format_integer(number, thousand_separator='.'):
        def reverse(string):
            string = "".join(reversed(string))
            return string
        s = reverse(str(number))
        count = 0
        result = ''
        for char in s:
            count = count + 1
            if count % 3 == 0:
                if len(s) == count:
                    result = char + result
                else:
                    result = thousand_separator + char + result
            else:
                result = char + result
        
        return result
    value = format_integer(num)
    context = {'value':value}
        
    return render(request,"commas.html",context)

def upload(request):
    if request.method == 'POST':
        form = UploadForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            print(obj)
            print("===================")
            return render(request,'upload.html',{'obj':obj})
    else:
        form = UploadForm()
        file = FileUpload.objects.all()
        print(file)
        print('---------------------')
        print(form)
    return render(request, "upload.html",{"form":form,"file":file})
    
# def upload(request):
#     if request.method == 'POST':
#         files = request.FILES['file'].readlines()
#         print(files)
#     return render(request, "upload.html")
