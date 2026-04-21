# ESTRUCTURA DEL PROYECTO

## 1) Flujo de datos
1. Cargar `sales_clean.csv` (ventas).
2. Cargar `specs_clean.csv` (especificaciones técnicas).
3. Estandarizar claves de unión (`brand`, `model`): trim, minúsculas y reemplazo de nulos.
4. Ejecutar merge interno por `brand` y `model`.
5. Calcular KPIs por dimensión de negocio.
6. Generar artefactos de salida (CSV/PNG).

## 2) Esquema del merge
```text
sales_clean.csv                      specs_clean.csv
(brand, model, city, year, ...)  +   (brand, model, ram_gb, ...)
                  \              /
                   \            /
                    inner merge on [brand, model]
                           |
                    market_df (dataset analítico)
```

## 3) Diccionario de variables (dataset unificado)
- `brand`: marca del equipo
- `model`: modelo del equipo
- `city`: ciudad
- `year`: año
- `units_sold`: unidades vendidas
- `revenue`: ingreso total
- `customers`: número de clientes
- `ram_gb`: memoria RAM
- `storage_gb`: almacenamiento
- `battery_mah`: capacidad de batería
- `camera_mp`: megapíxeles de cámara principal
- `os`: sistema operativo
- `price_eur`: precio en euros

## 4) KPIs principales
- **Unidades totales**: suma de `units_sold`
- **Ingresos totales**: suma de `revenue`
- **Ticket promedio**: `revenue / units_sold` (cuando unidades > 0)
- **Ventas por marca/modelo/ciudad/año**: agregaciones por dimensión
- **Correlaciones técnicas vs ventas**: matriz de correlación numérica

## 5) Decisiones de diseño
- Se usa un merge interno para asegurar que el análisis técnico-comercial tenga datos completos.
- La estandarización de claves evita pérdidas por variaciones de formato.
- El cálculo de KPIs se mantiene en funciones separadas para facilitar mantenimiento.
