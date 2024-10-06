import numpy as np
import cv2
from scipy.spatial import distance

def calculate_centroids(image_path):
    print(f"Intentando abrir la imagen: {image_path}")  # Imprimir la ruta
    ima = cv2.imread(image_path)
    if ima is None:
        print(f"Error: No se puede abrir la imagen en {image_path}. Verifica la ruta.")
        return None

    # Pasar a escala de grises para preprocesado
    ima_gray = cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)
    # Aplicar umbral para detectar zonas oscuras
    _, umbral = cv2.threshold(ima_gray, 100, 255, cv2.THRESH_BINARY)
    # Hallar contornos de las manchas negras
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Lista donde se guardaran todos los centroides
    centroids = []
    # Momento del contorno
    for contorno in contornos:
        M = cv2.moments(contorno)  # Calcular el momento del contorno
        if M["m00"] != 0:
            # Calcular el centroide
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            centroids.append((cx, cy))
            cv2.circle(ima, (cx, cy), 5, (0, 0, 255), -1)

    cv2.imshow("centroids", ima)
    cv2.waitKey(0)

    # Bucle para esperar a que se presione la tecla 'q' para cerrar
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    return centroids

def calculate_and_print_distances(centroids, image_name):
    print(f"\n--- Distancias entre centroides para la imagen {image_name} ---")
    for i in range(len(centroids)):
        for j in range(i + 1, len(centroids)):  # Evitar repetir distancias
            d = distance.euclidean(centroids[i], centroids[j])
            print(f"Distancia entre mancha {i + 1} y mancha {j + 1}: {d}")

# Lista de imágenes para procesar
image_paths1 = ["/Users/emece/ml/clases/nasa/i.png"]
image_paths2 = ["/Users/emece/ml/clases/nasa/ii.png"]
image_paths3 =  ["/Users/emece/ml/clases/nasa/iii.png"]
image_paths4 =  ["/Users/emece/ml/clases/nasa/iv.png"]
image_paths5 = ["/Users/emece/ml/clases/nasa/v.png"]
image_paths6 =  ["/Users/emece/ml/clases/nasa/vi.png"]

# Procesar cada imagen y obtener centroides
for path in image_paths1:
    centroids = calculate_centroids(path)
    if centroids is not None:
        calculate_and_print_distances(centroids, path)
        print("\n")
for path in image_paths2:
    centroids = calculate_centroids(path)
    if centroids is not None:
        calculate_and_print_distances(centroids, path)
        print("\n")   
for path in image_paths3:
    centroids = calculate_centroids(path)
    if centroids is not None:
        calculate_and_print_distances(centroids, path)
        print("\n")
      
for path in image_paths4:
    centroids = calculate_centroids(path)
    if centroids is not None:
        calculate_and_print_distances(centroids, path)
        print("\n")
       
for path in image_paths5:
    centroids = calculate_centroids(path)
    if centroids is not None:
        calculate_and_print_distances(centroids, path)
        print("\n")
        
for path in image_paths6:
    centroids = calculate_centroids(path)
    if centroids is not None:
        calculate_and_print_distances(centroids, path)
        print("\n")
np.sum(calculate_and_print_distances(centroids, path))
print(f"suma de las distancias entre centroides: {np.sum(calculate_and_print_distances(centroids, path))}")

