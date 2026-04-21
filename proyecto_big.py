"""Módulo principal para análisis de mercado de celulares.

Este script integra datasets de ventas y especificaciones técnicas para
construir un dataset analítico unificado, calcular KPIs de negocio y generar
visualizaciones de apoyo para la toma de decisiones.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def load_data(sales_path: str | Path, specs_path: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Carga los datasets de ventas y especificaciones desde archivos CSV.

    Args:
        sales_path: Ruta al archivo CSV de ventas.
        specs_path: Ruta al archivo CSV de especificaciones técnicas.

    Returns:
        Tupla con dos DataFrames: (sales_df, specs_df).
    """
    sales_df = pd.read_csv(sales_path)
    specs_df = pd.read_csv(specs_path)
    return sales_df, specs_df


def standardize_merge_keys(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Estandariza columnas clave para reducir fallos en operaciones de merge.

    Transformaciones aplicadas:
    - Conversión a string
    - Eliminación de espacios al inicio/fin
    - Normalización a minúsculas

    Args:
        df: DataFrame de entrada.
        columns: Nombres de columnas a estandarizar.

    Returns:
        DataFrame con las columnas clave normalizadas.
    """
    clean_df = df.copy()
    for col in columns:
        clean_df[col] = clean_df[col].astype(str).str.strip().str.lower()
    return clean_df


def merge_datasets(sales_df: pd.DataFrame, specs_df: pd.DataFrame) -> pd.DataFrame:
    """Une ventas y especificaciones por marca y modelo.

    Se usa un inner join para conservar solo registros con información
    comercial y técnica disponible.
    """
    sales_clean = standardize_merge_keys(sales_df, ["brand", "model"])
    specs_clean = standardize_merge_keys(specs_df, ["brand", "model"])
    return pd.merge(sales_clean, specs_clean, on=["brand", "model"], how="inner")


def sales_by_dimension(df: pd.DataFrame, dimension: str) -> pd.DataFrame:
    """Calcula ventas e ingresos agregados por una dimensión de análisis."""
    grouped = (
        df.groupby(dimension, dropna=False)[["units_sold", "revenue"]]
        .sum()
        .sort_values(by="units_sold", ascending=False)
        .reset_index()
    )
    return grouped


def technical_sales_correlation(df: pd.DataFrame) -> pd.DataFrame:
    """Genera matriz de correlación entre variables numéricas relevantes."""
    numeric_cols = [
        "units_sold",
        "revenue",
        "customers",
        "ram_gb",
        "storage_gb",
        "battery_mah",
        "camera_mp",
        "price_eur",
    ]
    available = [col for col in numeric_cols if col in df.columns]
    return df[available].corr(numeric_only=True)


def run_analysis(sales_path: str | Path, specs_path: str | Path, output_dir: str | Path) -> None:
    """Ejecuta el flujo completo de análisis y exporta resultados base."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    sales_df, specs_df = load_data(sales_path, specs_path)
    market_df = merge_datasets(sales_df, specs_df)

    brand_kpis = sales_by_dimension(market_df, "brand")
    model_kpis = sales_by_dimension(market_df, "model")
    city_kpis = sales_by_dimension(market_df, "city") if "city" in market_df.columns else pd.DataFrame()
    year_kpis = sales_by_dimension(market_df, "year") if "year" in market_df.columns else pd.DataFrame()
    corr = technical_sales_correlation(market_df)

    market_df.to_csv(output_path / "market_merged.csv", index=False)
    brand_kpis.to_csv(output_path / "kpis_by_brand.csv", index=False)
    model_kpis.to_csv(output_path / "kpis_by_model.csv", index=False)
    if not city_kpis.empty:
        city_kpis.to_csv(output_path / "kpis_by_city.csv", index=False)
    if not year_kpis.empty:
        year_kpis.to_csv(output_path / "kpis_by_year.csv", index=False)
    corr.to_csv(output_path / "correlation_matrix.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Análisis de mercado de celulares")
    parser.add_argument("--sales", required=True, help="Ruta al CSV de ventas")
    parser.add_argument("--specs", required=True, help="Ruta al CSV de especificaciones")
    parser.add_argument("--output", default="output", help="Carpeta de salida")
    args = parser.parse_args()

    run_analysis(args.sales, args.specs, args.output)
