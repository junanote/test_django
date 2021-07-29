from django.shortcuts import render

# Create your views here.
import folium
def home(request):
    mf = folium.Map([35.3369, 127.7306], zoom_start=10)
    mf = mf._repr_html_()
    first ='juna'
    result ={'mapfolium': mf, 'fo1':first}

    return render(request, template_name='maps/home.html', context=result)



def plotly(request):
    xArray = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
    yArray = [17, 18, 18, 19, 19, 19, 10, 11, 14, 14, 15]
    result = {'x_array':xArray, 'y_array':yArray}



    xArray02 = [50,60,70,80,90,100,110,120,130,140,150];
    yArray02 = [17,18,18,19,19,19,10,11,14,14,15];
    result['x_array02'] = xArray02
    result['y_array02'] = yArray02
    return render(request, template_name='maps/plotly.html', context=result)
