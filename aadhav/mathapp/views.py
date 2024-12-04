from django.shortcuts import render

def power(request):
    context = {
        'power': "0",
        'r': "0",
        'h': "0"
    }
    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('intensity', '0')
        h = request.POST.get('resistance', '0')
        
        try:
            intensity = float(r)
            resistance = float(h)
            
            power = (intensity ** 2) * resistance

            context['power'] = round(power, 2)
            context['r'] = r
            context['h'] = h
            print('intensity =', intensity)
            print('resistance =', resistance)
            print('power =', power)
        except ValueError:
            context['power'] = "Invalid input"
            print("Invalid input provided")
            
    return render(request, 'mathapp/math.html', context)