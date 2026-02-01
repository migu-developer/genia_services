# DVC - Comandos para subir y descargar datos

# =============================================================================
# REMOTE ORIGIN (DagsHub Storage)
# =============================================================================

# Subir datos al storage de DagsHub
dvc push -r origin

# Descargar datos desde DagsHub
dvc pull -r origin


# =============================================================================
# REMOTE S3 (AWS bucket migudev-dagshub-genia-services)
# =============================================================================

# Subir datos al bucket S3 en AWS
dvc push -r s3

# Descargar datos desde el bucket S3
dvc pull -r s3


# =============================================================================
# SUBIR O DESCARGAR EN AMBOS REMOTES
# =============================================================================

# Subir a DagsHub y a S3 (ejecutar ambos)
dvc push -r origin
dvc push -r s3

# Descargar desde DagsHub (por defecto suele usarse origin)
dvc pull -r origin

# Descargar desde S3
dvc pull -r s3


# =============================================================================
# ÚTILES
# =============================================================================

# Ver remotes configurados
dvc remote list

# Ver estado de archivos DVC (tracked, etc.)
dvc status
