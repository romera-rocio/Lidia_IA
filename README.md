# Lidia_IA


# WhatsApp AI Sales Platform

Plataforma universal de  **ventas y atención por WhatsApp** , impulsada por IA, diseñada para funcionar como **demo comercial** y como **solución productiva** para e‑commerce, restaurantes y servicios,  **sin modificar la web existente del cliente** .

---

## 1. Objetivo del proyecto

Este proyecto permite demostrar y luego implementar un **asistente inteligente de ventas por WhatsApp** que:

* Atiende clientes 24/7
* Responde **SIEMPRE** preguntas
* Toma pedidos o solicitudes
* Notifica al administrador
* Se adapta a cualquier rubro
* Funciona con datos externos (web, Sheets, APIs)
* No requiere panel web obligatorio

WhatsApp es la **única interfaz** para clientes y administradores.

---

## 2. Casos de uso

* E‑commerce (productos, precios, stock, pedidos)
* Restaurantes (menú, ingredientes, horarios, pedidos)
* Servicios (consultas, presupuestos, turnos)
* Demos comerciales para vender automatización

---

## 3. Arquitectura general

```
WhatsApp (Cliente / Admin)
        ↓
Webhook Backend (Python)
        ↓
Motor Conversacional IA
        ↓
Lógica de Negocio (flows)
        ↓
Fuentes de datos (Sheets / APIs / Web)
```

---

## 4. Principios clave del sistema

* WhatsApp es el frontend único
* La IA **siempre responde**
* El sistema no depende del rubro
* La web del cliente no se modifica
* La demo debe funcionar en horas, no semanas

---

## 5. Estructura del proyecto

```
whatsapp-ai-platform/
│
├── app.py                  # Webhook único de WhatsApp
│
├── core/
│   ├── router.py           # Decide flujo (pregunta / compra / admin)
│   ├── ia_engine.py        # IA + prompts + fallback obligatorio
│   └── context.py          # Construcción de contexto del negocio
│
├── flows/
│   ├── ecommerce.py        # Flujo e-commerce
│   ├── restaurant.py      # Flujo restaurante
│   └── services.py        # Flujo servicios
│
├── admin/
│   └── commands.py        # Comandos por WhatsApp para admin
│
├── data_sources/
│   ├── sheets.py          # Google Sheets (default)
│   ├── shopify.py         # Shopify (opcional)
│   ├── woocommerce.py     # WooCommerce (opcional)
│   └── scraper.py         # Scraping demo
│
├── config/
│   └── settings.py        # Configuración general
│
└── utils/
    └── safety.py          # Garantiza respuesta siempre
```

---

## 6. Flujo de conversación

### Cliente

1. Escribe por WhatsApp
2. Hace una pregunta o pedido
3. La IA responde usando datos del negocio
4. Si compra, se registra pedido
5. Recibe confirmación y seguimiento

### Administrador

1. Recibe notificación automática
2. Gestiona pedidos desde WhatsApp
3. Usa comandos simples

---

## 7. Comandos de administrador (WhatsApp)

```
#pedidos                 → Lista pedidos pendientes
#pedido 12               → Detalle pedido
#enviado 12              → Cambia estado a enviado
#entregado 12            → Marca como entregado
#stock                   → Ver stock
#stock actualizar X 10   → Actualiza stock
```

---

## 8. Fuentes de datos soportadas

* Google Sheets (recomendado para demo)
* Shopify API
* WooCommerce API
* Scraping simple de web
* CSV

Las fuentes son intercambiables sin afectar la lógica central.

---

## 9. Base de datos (Google Sheets)

### Productos

| ID | Nombre | Descripción | Precio | Stock | Extra |

### Pedidos

| ID | Cliente | Teléfono | Detalle | Total | Estado | Fecha |

### Clientes

| ID | Nombre | Teléfono | Historial | Último contacto |

---

## 10. IA – comportamiento obligatorio

La IA está configurada con reglas estrictas:

* Responder siempre
* Nunca decir "no sé" o "no entiendo"
* Inferir si falta información
* Mantener tono comercial
* Guiar a conversión

---

## 11. Instalación (local)

```bash
pip install flask gspread oauth2client
python app.py
```

Configurar el webhook de WhatsApp (Twilio / WATI / similar) apuntando a `/webhook`.

---

## 12. Uso como demo comercial

Este proyecto está pensado para:

* Mostrar valor rápido
* Adaptarse a cualquier negocio
* Vender automatización sin fricción

Mensaje típico de venta:

> "No cambiamos tu web. Te muestro cómo WhatsApp atiende y vende solo usando tu información actual."

---

## 13. Roadmap sugerido

* Modo demo multi‑cliente
* Persistencia por negocio
* IA con upsell automático
* Métricas de conversión
* Activación por QR o link

---

## 14. Licencia

Uso libre para demos, pruebas y desarrollo comercial.

---

## 15. Autor

Plataforma diseñada para automatización comercial basada en WhatsApp + IA, orientada a ventas, atención y escalabilidad.
