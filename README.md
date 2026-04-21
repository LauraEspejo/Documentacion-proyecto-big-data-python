# DOCUMENTACIÓN DEL PROYECTO: análisis de mercado de celulares

Este repositorio documenta un flujo de análisis de datos en Python para estudiar el mercado de celulares combinando **ventas** y **especificaciones técnicas**.

## Objetivo
Construir un análisis reproducible que permita comparar marcas y modelos por desempeño comercial (ventas/ingresos) y por características técnicas (RAM, batería, cámara, almacenamiento, precio, sistema operativo).

## Alcance del análisis
- Ingesta de `sales_clean.csv` y `specs_clean.csv`
- Estandarización de columnas para unir datasets
- Merge por `brand` y `model`
- Análisis exploratorio (EDA)
- KPIs por marca, modelo, ciudad y año
- Correlaciones entre especificaciones y ventas
- Generación de gráficas para interpretación ejecutiva

## Estructura esperada de datos

### Dataset de ventas (`sales_clean.csv`)
| Columna | Tipo sugerido | Descripción |
|---|---|---|
| `brand` | string | Marca del celular |
| `model` | string | Modelo del celular |
| `city` | string | Ciudad de la venta |
| `year` | int | Año de la venta |
| `units_sold` | int | Unidades vendidas |
| `revenue` | float | Ingreso generado |
| `customers` | int | Clientes asociados |

### Dataset de especificaciones (`specs_clean.csv`)
| Columna | Tipo sugerido | Descripción |
|---|---|---|
| `brand` | string | Marca del celular |
| `model` | string | Modelo del celular |
| `ram_gb` | float | Memoria RAM en GB |
| `storage_gb` | float | Almacenamiento en GB |
| `battery_mah` | int | Batería (mAh) |
| `camera_mp` | float | Cámara principal (MP) |
| `os` | string | Sistema operativo |
| `price_eur` | float | Precio en EUR |

## Requisitos del sistema
- Python 3.10+
- pip
- Dependencias de `requirements.txt`

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecución
```bash
python proyecto_big.py --sales data/sales_clean.csv --specs data/specs_clean.csv --output output
```

## Flujo de análisis
1. Carga de datos
2. Limpieza y estandarización de claves (`brand`, `model`)
3. Merge interno de datasets
4. Cálculo de KPIs
5. Correlaciones de variables numéricas
6. Exportación de reportes y gráficas

## Ejemplo de resultados e interpretación
- **Top marcas por unidades**: identifica liderazgo comercial.
- **Top modelos por ingresos**: muestra aportes de alto valor.
- **Correlación precio vs unidades**: ayuda a entender sensibilidad al precio.
- **Relación RAM/almacenamiento con ventas**: orienta estrategia de producto.

## Archivos principales
- `proyecto_big.py`: script principal documentado
- `ESTRUCTURA.md`: diccionario de variables, flujo y KPIs
- `ANALISIS.md`: guía de interpretación analítica
- `data/README.md`: guía de fuentes de datos
- `output/README.md`: guía de salidas generadas
