# XHash Analyzer v 1.0 - XBlack Edition

<img width="692" height="111" alt="hash" src="https://github.com/user-attachments/assets/cd7656a1-3627-462a-af36-29c0feebd1f7" />


![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?logo=python&logoColor=white)
---

## 📝 Descripción
**XHash Analyzer** es una herramienta web forense y de análisis criptográfico diseñada para ser ejecutada completamente del lado del cliente (Client-Side). Pertenece al ecosistema **Rhino Forensic & Reverse Toolkit** y ofrece una interfaz oscura y moderna ("Black Edition") con acentos neón.

La herramienta permite identificar tipos de hashes, generar sumas de verificación para textos y archivos, comparar la integridad de archivos y realizar ataques de diccionario básicos para recuperación de contraseñas, todo ello sin necesidad de un servidor backend.


## ✨ Características Principales

### 1. 🔍 Detectar Hash
Analiza una cadena de texto para identificar el algoritmo hash probable.
*   **Detección por Longitud y Patrón:** Identifica MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512.
*   **Detección de Formatos Linux:** Reconoce formatos con salt como SHA-256 Crypt ($5$) y SHA-512 Crypt ($6$).
*   **Detección de Bcrypt:** Identifica hashes que comienzan con $2a$, $2b$, $2y$.
*   Muestra detalles técnicos como longitud en bits, tipo de caracteres y posibles algoritmos similares.

### 2. ⚙️ Generar Hash
Calcula múltiples hashes simultáneamente a partir de una entrada.
*   **Entrada:** Texto manual o carga de archivos locales.
*   **Algoritmos Soportados:** MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA3 (224, 256, 384, 512) y RIPEMD-160.
*   Genera resultados en minúsculas y mayúsculas para facilitar la comparación.

### 3. ⚖️ Comparar Archivos
Verifica la integridad o identidad de dos archivos.
*   Calcula el hash SHA-256 de dos archivos.
*   Determina si son idénticos byte por byte.

### 4. 💥 Crackear Hash
Herramienta de ataque offline mediante diccionario.
*   **Algoritmos Crackeables:** MD5, SHA-1, SHA-256, SHA-512.
*   **Diccionario Personalizado:** Permite cargar cualquier archivo de texto (.txt) con contraseñas.
*   **Interfaz Visual:** Barra de progreso animada y contador de intentos en tiempo real.
*   Procesamiento optimizado por bloques (chunks) para evitar bloqueos del navegador.

### 5. ℹ️ About
Información del programador y características detalladas de la herramienta.

## 🛠️ Tecnologías Utilizadas
*   **HTML5 & CSS3:** Diseño responsivo con estructura Grid/Flexbox.
*   **JavaScript (ES6):** Lógica de negocio y manipulación del DOM.
*   **CryptoJS:** Librería estándar para operaciones criptográficas.
*   **Google Fonts:** Fuentes 'Orbitron' y 'Rajdhani' para la estética tecnológica.

## 🚀 Instalación y Uso
Al ser una herramienta web estática, no requiere instalación compleja.

1.  Clona el repositorio o descarga el archivo `index.html`.
2.  Coloca el archivo `index.html` en la raíz de tu servidor web o ábrelo directamente en un navegador moderno.
3.  Si deseas utilizar el diccionario de ejemplo, asegúrate de que el archivo `Ropckyou.rar` esté en el mismo directorio que el `index.html`.

## Requisitos Previos para la Versión CLI
pip install pyfiglet colorama  

## 📦 Recursos
La herramienta está diseñada para funcionar con diccionarios externos. Se deja un enlace de descarga sugerido dentro de la pestaña "About" del programa.

*   **Diccionario de Ataque:** `Ropckyou.rar` (Aprox. 136 MB).

## 👨‍💻 Autor
**Rodolfo Hernandez Baz aKa Pr@fEs0r X**

## ⚠️ Aviso Legal
Esta herramienta ha sido desarrollada con fines educativos y de auditoría de seguridad legítima. El uso de las funciones de cracking para obtener contraseñas sin autorización es ilegal. El usuario se hace responsable del uso que le dé a este software.
```
