# Smart Home Backend (modular)

Cấu trúc backend được tách thành nhiều file theo kiểu project backend nhiều module:

```text
smart_home_backend_modular/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── datasets.py
│   │       ├── devices.py
│   │       ├── health.py
│   │       └── ingest.py
│   ├── core/
│   │   ├── config.py
│   │   ├── helpers.py
│   │   └── time_utils.py
│   ├── db/
│   │   ├── database.py
│   │   └── session.py
│   ├── schemas/
│   │   ├── control_event.py
│   │   ├── device_twin.py
│   │   └── telemetry.py
│   ├── services/
│   │   └── mqtt_bridge.py
│   ├── workers/
│   │   └── resample_worker.py
│   └── main.py
├── requirements.txt
└── run.py
```

## Cài đặt

```bash
pip install -r requirements.txt
```

## Chạy server

```bash
uvicorn run:app --host 0.0.0.0 --port 8000 --reload
```

## MQTT topics

- `devices/<device_id>/telemetry`
- `devices/<device_id>/control-events`
- `devices/<device_id>/devicetwin`
