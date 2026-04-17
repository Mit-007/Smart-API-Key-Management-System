
# 🚀 Smart API Key Management System

A backend system built using **FastAPI + MongoDB Atlas + JWT Authentication** that allows users to securely generate, manage, and track API keys with usage monitoring.

---

## 📌 Features

* 🔐 User Registration & Authentication 
* ♻️ Access & Refresh Token System
* 🔑 API Key Creation & Management
* 📊 API Usage Tracking
* ⏱️ Middleware for Request Timing
* 🌐 MongoDB Atlas Cloud Database Integration

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** MongoDB Atlas
* **Authentication:** JWT (Access + Refresh Tokens)
* **Language:** Python


## 🔑 API Endpoints (Total: 9)

### 🔐 Auth APIs

1. **POST** `/auth/register`
   👉 Register new user

2. **POST** `/auth/login`
   👉 Login user → returns **Access Token + Refresh Token**

3. **POST** `/auth/refresh`
   👉 Generate new access token using refresh token

---

### 🔑 API Key Management

> ⚠️ All below endpoints require **valid Access Token**

4. **POST** `/Api_Mangement/create`
   👉 Create new API key

5. **GET** `/Api_Mangement/view`
   👉 Get all API keys

6. **GET** `/Api_Mangement/view/{api_id}`
   👉 Get single API key

7. **DELETE** `/Api_Mangement/delete/{api_id}`
   👉 Delete API key

8. **PUT** `/Api_Mangement/update/{api_id}`
   👉 Update API key status (Active / Inactive)

---

### 📊 Usage Tracker

9. **GET** `/usage_tracker/call_api`
   👉 Send URL as string → store in database

---

## ⚙️ Setup Instructions (Step-by-Step)

### 🔹 1. Clone Repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 🔹 2. Create Virtual Environment

```
python -m venv myenv
myenv\Scripts\activate   # Windows
```

---

### 🔹 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 🔹 4. Setup Environment Variables

Create `.env` file:

```
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/Smart_api_mangement_system
DB_NAME=Smart_api_mangement_system

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=20
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

### 🔹 5. Run Server

```
uvicorn app.main:app --reload
```

---

## 🌐 Swagger UI (API Testing)

Open browser:

```
http://127.0.0.1:8000/docs
```

---

## 🔄 How to Use APIs (Step-by-Step)

### ✅ Step 1: Register User

* Use `/auth/register`
* Provide username & password

---

### ✅ Step 2: Login

* Use `/auth/login`
* Get:

  * Access Token
  * Refresh Token

---

### ✅ Step 3: Access Token for Authorize 

copy **Access Token**

Enter the Access Token Format:

```
Bearer <your_access_token>
```

---

### ✅ Step 4: Use Protected APIs

Now you can:

* Create API key
* View API keys
* Update / Delete API key

---

### 🔁 Step 5: Refresh Token

If access token expires:

* Call `/auth/refresh`
* Get new access token

---

### 📊 Step 6: Track API Usage

* Call `/usage_tracker/call_api`
* Send URL as string :

```
example : /ApiKey/home/profile
```

* Data stored in MongoDB

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
