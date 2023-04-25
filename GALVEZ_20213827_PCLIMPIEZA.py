#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd


# In[33]:


#en este caso escogí una tabla de wikipedia para limpiarla
dataNintendo= "https://es.wikipedia.org/wiki/Super_Mario_Bros."


# In[34]:


#al ser una página web y no un csv, va a detectar todas las tablas de las cuales se escogerá 1
MarioBros=pd.read_html(dataNintendo)
MarioBros


# In[35]:


#se usa type para averiguar que tipo de data se esta exportando
type(MarioBros)


# In[36]:


#se escoge la tabla que ubica al videojuego dentro de una categoría
MarioBros[2]


# In[37]:


#renombramos las columnas
MarioCorrecto=MarioBros[2].rename(columns={"Nombre de la lista":"MarioBros en los Top Mundiales"})
MarioCorrecto


# In[38]:


#pienso que la columna de "editorial" no es necesaria a comparación de las otras 3. Por lo tanto, será eliminada
byeColumns=['Editorial']
MarioCorrecto.drop(columns=byeColumns,inplace=True)
MarioCorrecto


# In[39]:


#asismo en la columna de posicion se sobreentiende que son lugares por ello se elimina "lugar"
MarioCorrecto.Posición=MarioCorrecto.Posición.str.split(' ',expand=True)[0]
MarioCorrecto


# In[41]:


#en vista que la tabla es pequeña, se le agregó una columna que muestra los personajes del videojuego
nuevos_valores = ["Mario Bros","Luigi", "Princesa Peach","Donkey Kong", "Yoshi","Toad","Kamek"]
MarioCorrecto.insert(loc=3, column='Personajes Característicos', value=nuevos_valores)
print(MarioCorrecto)


# In[42]:


MarioCorrecto


# In[43]:


#Los nombres de las posiciones están disparejas, lo ideal es reemplazar esos datos por un mejor arreglo
MarioCorrecto['Posición'] = MarioCorrecto['Posición'].replace("3.er", "Tercer lugar")
print(MarioCorrecto)


# In[44]:


MarioCorrecto


# In[45]:


#se realizó el mismo paso para las otras dos posiciones por ende se puede reemplazar en un solo cambio
cambios = {"1.er": "Primer lugar", "2.º": "Segundo lugar"}

# Cambiamos todos los valores de la columna 'A' según los cambios definidos en el diccionario
MarioCorrecto['Posición'] = MarioCorrecto['Posición'].replace(cambios)
print(MarioCorrecto)


# In[46]:


MarioCorrecto


# In[47]:


import re
# Reemplazamos los corchetes con números por espacios vacíos
patron = r"\[\d+\]"
MarioCorrecto = MarioCorrecto.replace(to_replace=patron, value="", regex=True)

print(MarioCorrecto)


# In[48]:


MarioCorrecto


# In[49]:


#finalmente, verificamos que nuestros datos cambiados no contengan numeros
patron = r'^[^0-9]+$'
MarioCorrecto = MarioCorrecto[MarioCorrecto['Posición'].str.contains(patron)]

print(MarioCorrecto)


# In[50]:


MarioCorrecto


# In[ ]:




