"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd
    import os  

    # ------------------------------------------------------------
    # 1. Lectura del archivo
    # ------------------------------------------------------------
    data = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)

    # ------------------------------------------------------------
    # 2. Limpieza por columnas
    # ------------------------------------------------------------
    data["sexo"] = data["sexo"].str.lower()

    data["tipo_de_emprendimiento"] = data["tipo_de_emprendimiento"].str.lower().str.strip()

    data["barrio"] = (
        data["barrio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    data["idea_negocio"] = (
        data["idea_negocio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.strip()
    )

    data["línea_credito"] = (
        data["línea_credito"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.strip()
    )

    data["monto_del_credito"] = (
        data["monto_del_credito"]
        .str.strip()
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(".00", "", regex=False)
    )
    data["monto_del_credito"] = pd.to_numeric(data["monto_del_credito"], errors="coerce")

    # ------------------------------------------------------------
    # 3. Conversión de fechas (dos formatos posibles)
    # ------------------------------------------------------------
    data["fecha_de_beneficio"] = pd.to_datetime(
        data["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(
        pd.to_datetime(data["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    )

    data["comuna_ciudadano"] = pd.to_numeric(data["comuna_ciudadano"], errors="coerce").astype("Int64")

    # ------------------------------------------------------------
    # 4. Eliminación de duplicados
    # ------------------------------------------------------------
    data.drop_duplicates(inplace=True)

    # ------------------------------------------------------------
    # 5. Eliminación de filas con valores nulos
    # ------------------------------------------------------------
    data.dropna(inplace=True)

    # ------------------------------------------------------------
    # 6. Guardado del archivo limpio
    # ------------------------------------------------------------
    os.makedirs("files/output", exist_ok=True)
    data.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)


if __name__ == "__main__":
    pregunta_01()
