from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'length.html')

def precision(value):
    if value<0.000001:
        return 8
    elif value<0.0001:
        return 6
    elif value<0.01:
        return 4
    else:
        return 2
    
def length(request):
    if request.method == 'POST':
        # Process the form data and calculate the result
        result = length_converter_view(request.POST['le'], request.POST['from'], request.POST['to'])
        return render(request, 'Length.html', {'result': result[0], 'unit': result[1]})
    else:
        return render(request, 'Length.html')

def length_converter_view(length, frm, to):
    # Convert the length from the given unit to the desired unit
    # This is a simplified example and does not cover all possible units
    result = None
    error_msg = None
    frm = frm
    to = to
    convolen={
        'centi':' cm',
        'meter':' m'
    }
    try:
        if length:
            if frm == 'centi' and to == 'meter':
                result = float(length) / 100
                return result, convolen[to]
            elif frm == 'meter' and to == 'centi':
                result = float(length) * 100
                return result, convolen[to]
    except:
        error_msg = "Invalid input"
        return error_msg, None
    

def temp(request):
    if request.method == 'POST':
        resu = temperature_converter_view(request.POST.get('tem'), request.POST.get('from'), request.POST.get('to'))
        
        if resu is None:
            error_message = "Invalid input or conversion error"
            return render(request, 'Temperature.html', {'error_message': error_message})
        
        return render(request, 'Temperature.html', {'result': resu[0], 'unit': resu[1]})
    else:
        return render(request, 'Temperature.html')

def temperature_converter_view(temperature, frm, to):
    # Convert the temperature from the given unit to the desired unit
    result = None
    convotem = {
        'cel': '°C',
        'kel': 'K'
    }
    # Validate temperature input
    if not temperature:
        raise ValueError("Temperature value cannot be empty.")

    try:
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Invalid temperature input. Please enter a numeric value.")

    if frm == 'cel' and to == 'kel':
        result = temperature + 273.15
        return result, convotem[to]
    elif frm == 'kel' and to == 'cel':
        result = temperature - 273.15
        return result, convotem[to]
    
def weight(request):
    if request.method == 'POST':
        resu = weight_converter_view(request.POST.get('tem'), request.POST.get('from'), request.POST.get('to'))
        
        if resu is None:
            error_message = "Invalid input or conversion error"
            return render(request, 'Weight.html', {'error_message': error_message})
        
        return render(request, 'Weight.html', {'result': resu[0], 'unit': resu[1]})
    else:
        return render(request, 'Weight.html')

def weight_converter_view(weight, frm, to):
    # Convert the weight from the given unit to the desired unit
    # This is a simplified example and does not cover all possible units
    result = None
    convowei = {
        'kilo': 'kg',
        'gram': 'g'
    }
    # Validate weight input
    if not weight:
        raise ValueError("weight value cannot be empty.")

    try:
        weight = float(weight)
    except ValueError:
        raise ValueError("Invalid weight input. Please enter a numeric value.")

    if frm == 'gram' and to == 'kilo':
        result = weight/1000
        return result, convowei[to]
    elif frm == 'kilo' and to == 'gram':
        result = weight*1000
        return result, convowei[to]