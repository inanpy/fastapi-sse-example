# 🚀 FastAPI SSE Example

This is a simple example project showing how to implement **Server-Sent Events (SSE)** using FastAPI.

## 🔧 How to Run

1. Create a virtual environment:
```bash
python -m venv venv && source venv/bin/activate
```

2. Install dependencies:
```bash
# Using pip
pip install -r requirements.txt

# Or using uv
uv pip install -r requirements.txt
```

3. Start the server:
```bash
uvicorn main:app --reload
```

4. Open your browser and visit:
```
http://localhost:8000/sse
```

## 💡 How It Works

- `event_generator()` yields data with the required SSE format (`data: ... \n\n`)
- The browser (or frontend app) connects using `EventSource`.
- FastAPI’s `StreamingResponse` keeps the connection alive and streams updates.

## 🧪 Frontend (Test)

You can test with this HTML snippet:

```html
<script>
  const sse = new EventSource("http://localhost:8000/sse");
  sse.onmessage = (e) => console.log("Message:", e.data);
</script>
```

## 🧠 Notes

- SSE is great for unidirectional updates like notifications or live counters.
- For bi-directional communication, consider WebSockets.

## 📖 Related Articles

- [Real-time Notifications in Python using SSE with FastAPI](https://medium.com/@inandelibas/real-time-notifications-in-python-using-sse-with-fastapi-1c8c54746eb7) (A detailed article explaining how to implement Server-Sent Events with FastAPI).

---

### 🧑‍💻 Author

**İnan Delibaş**

Senior Python Developer | Python Team Lead & Architect

[LinkedIn](https://www.linkedin.com/in/inandelibas/) |
[GitHub](https://github.com/inanpy)
