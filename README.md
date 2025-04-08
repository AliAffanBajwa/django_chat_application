## 🗨️ Real-Time Chat App (Django + Channels + WebSockets + HTMX)

A real-time chat application built with **Django**, **Channels**, **Daphne**, **HTMX**, and **WebSockets**. It supports:

- 🧑‍🤝‍🧑 Public chat rooms  
- 🔒 Private 1-on-1 chats  
- 👥 Group chats  
- 🔄 Real-time message delivery with WebSockets  
- ⚡ Interactive features using HTMX

---

### 🚀 Features

- Real-time communication using Django Channels & WebSockets
- Public and private chatrooms
- Group chat support with member management
- HTMX-powered message sending and live updates without full page reloads
- Responsive UI with Bootstrap
- Authentication (Login/Register)
- Middleware-protected routes
- Chat history and user tracking

---

### 🛠️ Tech Stack

| Technology         | Purpose                         |
|--------------------|---------------------------------|
| Django             | Main web framework              |
| Django Channels    | Async support and WebSockets    |
| Daphne             | ASGI server                     |
| HTMX               | Frontend interactivity          |
| WebSockets         | Real-time communication         |
| Bootstrap 5        | UI styling                      |
| SQLite / PostgreSQL| Database (default: SQLite)      |

---

### 📂 Project Structure

```
django_chat_application/
│
├── rtChat/                # Chat app with views, consumers, models
│   ├── consumers.py       # WebSocket handlers
│   ├── routing.py         # WebSocket routing
│   ├── views.py           # Django views
│   ├── models.py          # ChatGroup, ChatMessage models
│   ├── templates/         # Templates (HTMX + Bootstrap)
│
├── authApp/               # Handles authentication (login/register)
├── authProject/          # Main project config (settings, urls)
│   ├── asgi.py            # ASGI config with channel layers
│   ├── settings.py
│
├── requirements.txt       # Dependencies
└── manage.py
```

---

### 🔧 Installation Guide

#### 1. Clone the Repository
```bash
git clone https://github.com/AliAffanBajwa/django_chat_application
cd django_chat_application
```

#### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
python -m pip install -U 'channels[daphne]'
```

#### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

#### 6. Run Daphne ASGI Server
```bash
python manage.py runserver
```

> ✅ Make sure your `asgi.py` and `settings.py` are configured for Channels.

---

### 🔌 WebSocket Configuration

Make sure you’ve added Channels to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'daphne',
    ...
    'django_htmx',
    'rtChat',
    'authApp',
]
```

### 💬 Usage

- **Login/Register** to start chatting.
- Navigate to:
  - `/rtChat/` for the default public chat
  - `/rtChat/chat/room/<room_name>` to access a specific room
- Create new group chats, add/remove members
- Use HTMX to send messages live without reloading

---

### 📦 requirements.txt (sample)

```
django
channels
daphne
djang-htmx
shortuuid
```
---

### ✅ HTMX Integration

HTMX is used for sending chat messages asynchronously:

- **Form submission:**  
  HTMX sends the message via POST and renders new messages in a partial.

```html
<form hx-post="." hx-target="#chat-messages" hx-swap="beforeend">
  {{ form }}
  <button type="submit" class="btn btn-primary">Send</button>
</form>
```

---

### 🧪 Development Commands

| Command                          | Action                             |
|----------------------------------|------------------------------------|
| `python manage.py runserver`    | Run app (sync, for testing)            |
| `python manage.py createsuperuser` | Create admin user                |
