def send_alerts(malicious_ia, phishing_analysis):
    # Lógica para enviar alertas basadas en las detecciones
    if malicious_ia["detected"]:
        print("Alerta: IA maliciosa detectada")
    if phishing_analysis["phishing_detected"]:
        print("Alerta: Phishing detectado")
