# Your code goes here:
def render_person(nombre,fec_nac,color_ojos,edad,sexo): 
   print( nombre  + ' is a ' + str(edad) + ' old male born in ' + str(fec_nac) + ' with ' + color_ojos + ' eyes')  
   return print(f'{nombre} is a {edad} old male born in {fec_nac} with {color_ojos} eyes')


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))