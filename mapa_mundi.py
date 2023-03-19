import folium
#Codigo Fonte

# criar um mapa centrado no Brasil com o zoom ajustado para mostrar apenas o Brasil.
mapa = folium.Map(location=[-15.77972, -47.92972], zoom_star=5)

# Adicionar marcadores para algumas cidades do Brasil.
folium.Marker(location=[-23.5505, -466333], popup='São Paulo').add_to(mapa)
folium.Marker(location=[-22.9068, -43.1729], popup='Rio de Janeiro').add_to(mapa)
folium.Marker(location=[-12.9722, -38.5014], popup='Salvador').add_to(mapa)

# Salvar o mapa como um arquivo HTML.
mapa.save("mapa_mundi.html")