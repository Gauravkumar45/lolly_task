from django.shortcuts import render,HttpResponse
from .models import FileUpload

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
    if request.method == "POST":
        num = request.POST.get('text')
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
        print(format_integer(num))
    return render(request,"commas.html")

def upload(request):
    if request.method == 'POST':
        files = request.FILES["file"]
        document = FileUpload.objects.create(file=files)
        document.save()
        return HttpResponse('your file was uploaded')
    return render(request, "upload.html")
    
