from django.shortcuts import render_to_response

def plus(request):
    if 'a' not in request.GET:
        return render_to_response('plus.html')
    else:
        a = request.GET['a']
        b = request.GET['b']
        c = int(a) + int(b)
        return render_to_response('plusresult.html',{
            'result':str(c)
        })
