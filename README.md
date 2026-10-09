# FastAPI Product Management CRUD API

A lightweight RESTful API built with **FastAPI** that demonstrates routing, CRUD operations, and persistent data handling using a local JSON file (`products.json`).

---

## 🚀 Features

- **Fast & Modern**: Built with [FastAPI](https://fastapi.tiangolo.com/) and powered by [Uvicorn](https://www.uvicorn.org/).
- **Interactive API Docs**: Built-in interactive documentation powered by Swagger UI and ReDoc.
- **Product Catalog Management**:
  - View all products
  - Search product by ID
  - Add new products
  - Update existing product attributes
  - Delete products by ID
- **JSON File Persistence**: Product data is stored directly in `products.json`.

---

## 📁 Project Structure

```text
fast api/
├── app.py             # Main FastAPI application with routes and logic
├── products.json      # JSON data storage for product records
├── requirements.txt   # Python package dependencies
└── README.md          # Project documentation
```

---

## 🛠️ Prerequisites & Installation

### 1. Clone or Open the Project Directory
Navigate to your project folder:
```bash
cd "fast api"
```

### 2. Set Up a Virtual Environment (Recommended)

**On Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
Install FastAPI and Uvicorn:
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the development server with auto-reload:

```bash
uvicorn app:app --reload
```

The server will start at:
- **API Base URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Documentation:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📚 API Endpoints

### General Endpoints

| Method | Endpoint | Description | Sample Response |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root health/status endpoint | `{"status": "Hello world"}` |
| `GET` | `/display` | Simple greeting test page | `["This is another page..."]` |
| `GET` | `/name` | Author / user information | `["Hi i am om "]` |

---

### Product Management Endpoints

| Method | Endpoint | Description | Request Body / Param |
| :--- | :--- | :--- | :--- |
| `GET` | `/show` | Retrieve all products | None |
| `GET` | `/show/{id}` | Retrieve a single product by ID | Path parameter: `id` (int) |
| `POST` | `/add` | Add a new product to `products.json` | JSON Body (`dict`) |
| `PUT` | `/update/{id}` | Update product fields by ID | Path param: `id`, JSON Body (`dict`) |
| `DELETE` | `/delete/{id}` | Remove a product by ID | Path parameter: `id` (int) |

---

## 📝 Request Examples

### 1. Get Product by ID
- **Method:** `GET`
- **URL:** `http://127.0.0.1:8000/show/1`
- **Response:**
```json
{
  "id": 1,
  "name": "Wireless Mouse",
  "category": "Electronics",
  "price": 599.0,
  "in_stock": true
}
```

---

### 2. Add New Product
- **Method:** `POST`
- **URL:** `http://127.0.0.1:8000/add`
- **Headers:** `Content-Type: application/json`
- **Body:**
```json
{
  "id": 10,
  "name": "Smart Watch",
  "category": "Electronics",
  "price": 2999.0,
  "in_stock": true
}
```

---

### 3. Update Existing Product
- **Method:** `PUT`
- **URL:** `http://127.0.0.1:8000/update/10`
- **Headers:** `Content-Type: application/json`
- **Body:**
```json
{
  "price": 2499.0,
  "in_stock": false
}
```

---

### 4. Delete Product
- **Method:** `DELETE`
- **URL:** `http://127.0.0.1:8000/delete/10`
- **Response:**
```json
[
  "Item deleted"
]
```

---

## 📌 Data Model Reference (`products.json`)

Each product entry in `products.json` follows this general schema:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier for the product |
| `name` | String | Product title / name |
| `category` | String | Category (e.g., Electronics, Stationery, Lifestyle) |
| `price` | Number | Price of the item |
| `in_stock` | Boolean | Inventory availability status |

---

## 💡 Recommended Future Enhancements

- **Pydantic Models:** Replace raw `dict` request bodies with Pydantic schemas (`BaseModel`) for automated input validation and auto-populated Swagger documentation.
- **HTTP Status Codes:** Return standard HTTP status codes (e.g., `201 Created`, `404 Not Found`).
- **Database Integration:** Transition from file-based JSON storage to an asynchronous SQL database (e.g., SQLite, PostgreSQL with SQLAlchemy).
