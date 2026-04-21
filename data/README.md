# data/

Esta carpeta almacena los datasets de entrada del análisis.

## Archivos esperados
- `sales_clean.csv`: dataset de ventas (marca, modelo, ciudad, año, unidades, ingresos, clientes)
- `specs_clean.csv`: dataset técnico (RAM, almacenamiento, batería, cámara, SO, precio)

## Recomendaciones
- Mantener UTF-8 y encabezados consistentes.
- Validar que `brand` y `model` existan en ambos archivos para un merge correcto.
