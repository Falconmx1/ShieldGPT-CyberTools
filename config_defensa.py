import json

CONFIG_FILE = 'config.json'

def load_config():
    """Carga la configuración desde un archivo JSON."""
    try:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            print("Configuración cargada exitosamente.")
            return config
    except FileNotFoundError:
        print(f"El archivo de configuración {CONFIG_FILE} no se encontró. Usando configuración predeterminada.")
        return get_default_config()
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo de configuración {CONFIG_FILE}. Usando configuración predeterminada.")
        return get_default_config()

def save_config(config):
    """Guarda la configuración en un archivo JSON."""
    try:
        with open(CONFIG_FILE, 'w') as file:
            json.dump(config, file, indent=4)
            print("Configuración guardada exitosamente.")
    except IOError as e:
        print(f"Error al guardar la configuración: {e}")

def get_default_config():
    """Devuelve una configuración predeterminada."""
    return {
        "phishing_threshold": 0.75,
        "malicious_ia_threshold": 0.80,
        "alert_email": "admin@example.com",
        "alert_sms": "1234567890",
        "scan_interval": 60,  # en segundos
        "model_path": "path/to/model",
        "api_keys": {
            "virustotal": "your_virustotal_api_key",
            "ibm_watson": "your_ibm_watson_api_key"
        }
    }

def update_config(key, value):
    """Actualiza un parámetro específico en la configuración."""
    config = load_config()
    config[key] = value
    save_config(config)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar configuración
    config = load_config()

    # Mostrar configuración actual
    print("Configuración actual:", config)

    # Actualizar un parámetro
    update_config("phishing_threshold", 0.85)

    # Mostrar configuración actualizada
    print("Configuración actualizada:", load_config())
