# Day 01 — Internet & Web Fundamentals
> **Backend Development Journey**  
> **Topic:** How the Internet Works, HTTP, HTTPS, DNS, APIs, and Backend Servers  
> **Level:** Complete Beginner  

---

## 📚 Table of Contents

1. [How the Internet Works]
2. [DNS Resolution — Two Methods]
3. [HTTP vs HTTPS]
4. [HTTP Status Codes]
5. [Role of a Backend Server]
6. [What is an API?]
7. [Key Terms Glossary]
8. [Quick Revision Q&A]

---

## 1. How the Internet Works

When you type a URL like `youtube.com` in your browser, a series of steps happen behind the scenes to find the website and display it on your screen.

### 1.1 Key Components

| Component      | Description |
|----------------|--------------------------------------------------------------------|
| **IP Address** | A unique numerical address for every device/server on the internet (e.g. `142.250.64.78`) |
| **DNS**        | Domain Name System — converts human-readable domain names into IP addresses |
| **DNS Resolver** | Your ISP's local server that looks up IP addresses on your behalf |
| **Root Server** | The top-level server that knows where TLD servers are located |
| **TLD Server** | Top Level Domain server — manages extensions like `.com`, `.org`, `.in` |
| **Authoritative Server** | The final server that holds the actual IP address of the domain |
| **Web Server** | The server that hosts the actual website and sends back HTML/CSS/JS |

### 1.2 Simple Flow

```
You type youtube.com
      ↓
Browser → DNS Resolver → Root Server → TLD Server → Authoritative Server
                                                              ↓
                                                        IP Address found
                                                              ↓
Browser → Web Server (using IP) → Gets back HTML, CSS, JS → Website loads!
```

---

## 2. DNS Resolution — Two Methods

### Method 1: Recursive DNS 🔄

In Recursive DNS, the **DNS Resolver does all the heavy lifting** on your behalf.

```
Step 1: Browser asks DNS Resolver → "What is the IP of youtube.com?"
Step 2: DNS Resolver asks Root Server
Step 3: Root Server replies → "Ask the .com TLD Server"
Step 4: DNS Resolver asks TLD Server (.com)
Step 5: TLD Server replies → "Ask the Authoritative Server"
Step 6: DNS Resolver asks Authoritative Server
Step 7: Authoritative Server replies with IP → (e.g. 142.250.64.78)
Step 8: DNS Resolver returns IP to Browser
Step 9: Browser connects to Web Server → Gets HTML/CSS/JS → Website loads!
```

> **Key Point:** The DNS Resolver does all the asking. Your browser just waits for the final answer.

---

### Method 2: Iterative DNS 🔁

In Iterative DNS, your **browser/machine itself contacts each server** one by one.

```
Step 1: Browser asks DNS Resolver → Gets a referral to Root Server
Step 2: Browser directly asks Root Server → Gets a referral to TLD Server
Step 3: Browser directly asks TLD Server → Gets a referral to Authoritative Server
Step 4: Browser directly asks Authoritative Server → Gets the IP address
Step 5: Browser connects to Web Server → Gets HTML/CSS/JS → Website loads!
```

> **Key Point:** The browser/machine does all the asking itself. Each server just points to the next one.

---

### Recursive vs Iterative — Comparison

| Feature | Recursive | Iterative |
|---|---|---|
| **Who does the work?** | DNS Resolver | Browser / Machine |
| **Load on client** | Low (just waits for answer) | High (asks each server) |
| **Common usage** | Most browsers (default) | Used by DNS servers themselves |
| **Speed** | Generally faster for end user | More control, more steps |

---

## 3. HTTP vs HTTPS

**HTTP (HyperText Transfer Protocol)** is the set of rules that defines how data is sent and received between a browser (client) and a web server.

### 3.1 Key Differences

| Feature | HTTP | HTTPS |
|---|---|---|
| **Full Form** | HyperText Transfer Protocol | HyperText Transfer Protocol Secure |
| **Data Format** | Plain text (readable by anyone) | Encrypted (unreadable without key) |
| **Security** | ❌ Unsafe | ✅ Secure |
| **Speed** | Slightly faster | Slightly slower (due to encryption) |
| **URL** | `http://` | `https://` |
| **Browser indicator** | No lock icon | 🔒 Lock icon |
| **Port** | Port 80 | Port 443 |
| **Used for** | Old/internal sites | All modern websites, banking, login |

### 3.2 How HTTPS Works

```
Client                          Server
  |                               |
  |  ——— HTTPS Request ————————→  |
  |     (encrypted with SSL/TLS)  |
  |                               |
  |  ←—— HTTPS Response ————————  |
  |     (encrypted with SSL/TLS)  |
  |                               |
```

- **Encryption** → Converting readable data into a secret coded format before sending
- **Decryption** → Converting the secret coded data back into readable format on arrival
- **SSL/TLS Certificate** → The digital certificate that enables HTTPS encryption

### 3.3 Real Example

```
Without HTTPS (HTTP):
Password sent as → "mypassword123"  ← Anyone can read this! ❌

With HTTPS:
Password sent as → "xT7#kL9!mP2$" ← Unreadable without the key! ✅
```

---

## 4. HTTP Status Codes

Every time your browser makes a request, the server responds with a **status code** that tells you what happened.

### 4.1 Status Code Categories

| Range | Category | Meaning |
|---|---|---|
| **1xx** | Informational | Request received, processing |
| **2xx** | Success | Request successful |
| **3xx** | Redirection | Further action needed |
| **4xx** | Client Error | Problem with the request |
| **5xx** | Server Error | Problem on the server side |

### 4.2 Most Important Status Codes

| Code | Name | Meaning | Example |
|---|---|---|---|
| **200** | OK | Request was successful ✅ | Page loaded perfectly |
| **201** | Created | New resource created ✅ | User registered successfully |
| **204** | No Content | Success but no data returned | Deleted successfully |
| **301** | Moved Permanently | Page moved to new URL | Old URL redirects to new one |
| **400** | Bad Request | Malformed/invalid request | Wrong data format sent |
| **401** | Unauthorized | Login required | Accessing without logging in |
| **403** | Forbidden | No permission | Accessing admin page as normal user |
| **404** | Not Found | Resource does not exist ❌ | Wrong URL typed |
| **500** | Internal Server Error | Server-side problem 💥 | Server crashed |
| **503** | Service Unavailable | Server is down | Server under maintenance |

### 4.3 Quick Memory Trick

```
2xx = ✅ Success   (2 = good, 2 thumbs up!)
4xx = ❌ Your fault (4 = client error)
5xx = 💥 Server's fault (5 = server error)
```

---

## 5. Role of a Backend Server

The **backend server** is the brain of a web application. It sits between the frontend (what the user sees) and the database (where data is stored).

### 5.1 What a Backend Server Does

```
Frontend (Browser/App)
        ↓ Request
   Backend Server
   ┌─────────────────────────────┐
   │  1. Receives the request    │
   │  2. Validates the data      │
   │  3. Applies business logic  │
   │  4. Talks to the database   │
   │  5. Returns a response      │
   └─────────────────────────────┘
        ↓ Response (JSON)
Frontend (Browser/App)
```

### 5.2 CRUD Operations

Every backend application performs **CRUD** operations on data:

| Operation | HTTP Method | SQL Command | Example |
|---|---|---|---|
| **C**reate | POST | INSERT | Register a new user |
| **R**ead | GET | SELECT | Get all products |
| **U**pdate | PUT / PATCH | UPDATE | Update profile picture |
| **D**elete | DELETE | DELETE | Delete an account |

### 5.3 Frontend vs Backend

| Aspect | Frontend | Backend |
|---|---|---|
| **What user sees?** | ✅ Yes (UI, buttons, forms) | ❌ No (runs on server) |
| **Languages** | HTML, CSS, JavaScript | Python, Node.js, Java, PHP |
| **Main job** | Display data to user | Process data, talk to database |
| **Frameworks** | React, Vue, Angular | Express, Django, Spring Boot |
| **Runs on** | User's browser | Server (cloud/hosting) |

### 5.4 Three-Tier Architecture

```
┌─────────────────┐
│   FRONTEND      │  ← What users see (HTML/CSS/JS)
│   (Client)      │
└────────┬────────┘
         │ HTTP Request/Response
┌────────▼────────┐
│   BACKEND       │  ← Business logic (Node.js/Python/Java)
│   (Server)      │
└────────┬────────┘
         │ SQL/NoSQL Queries
┌────────▼────────┐
│   DATABASE      │  ← Data storage (MySQL/MongoDB)
│                 │
└─────────────────┘
```

---

## 6. What is an API?

**API** stands for **Application Programming Interface**.

> It is a set of rules and protocols that allows different software applications to communicate and share data with one another.

### 6.1 Simple Analogy — The Restaurant 🍽️

```
YOU (Client/Frontend)
  ↓  "I want Pasta please"
WAITER (API)
  ↓  Carries your order to kitchen
KITCHEN (Backend Server)
  ↓  Prepares the food (processes data)
WAITER (API)
  ↓  Brings food back to you
YOU (Client/Frontend)
  ← Receives the response
```

> You never go into the kitchen yourself — the waiter (API) is the middleman!

### 6.2 Types of APIs

| Type | Description | Use Case |
|---|---|---|
| **REST API** | Uses HTTP methods, data in JSON format | Most web/mobile apps |
| **GraphQL** | Client requests exactly the data it needs | Complex data requirements |
| **WebSocket** | Real-time two-way communication | Chat apps, live scores |
| **SOAP** | XML-based, older protocol | Enterprise/banking systems |

### 6.3 REST API — HTTP Methods

| HTTP Method | CRUD Action | Example |
|---|---|---|
| **GET** | READ — fetch data | Get list of all users |
| **POST** | CREATE — send new data | Register a new user |
| **PUT** | UPDATE — replace existing data | Update entire profile |
| **PATCH** | UPDATE — modify part of data | Update only profile picture |
| **DELETE** | DELETE — remove data | Delete an account |

### 6.4 API Request & Response Example

```
REQUEST:
GET https://api.example.com/users/1
Headers: { "Authorization": "Bearer token123" }

RESPONSE:
Status: 200 OK
Body: {
  "id": 1,
  "name": "Rahul",
  "email": "rahul@example.com",
  "age": 20
}
```

### 6.5 What is JSON?

**JSON (JavaScript Object Notation)** is the most common data format used in APIs.

```json
{
  "name": "Rahul",
  "age": 20,
  "city": "Delhi",
  "skills": ["Python", "JavaScript", "SQL"],
  "is_employed": false
}
```

> JSON is just like Python's Dictionary! Key-value pairs. 🐍

---

## 7. Key Terms Glossary

| Term | Definition |
|---|---|
| **Client** | The browser or app that makes requests (your phone, laptop) |
| **Server** | A computer that receives requests, processes them, and sends responses |
| **Protocol** | A set of rules for communication (e.g. HTTP, HTTPS, TCP/IP) |
| **Request** | A message sent from client to server asking for data or action |
| **Response** | The server's reply to a client's request |
| **DNS** | Domain Name System — converts domain names to IP addresses |
| **IP Address** | Unique address of every device/server on the internet |
| **Port** | A virtual channel on a server (HTTP=80, HTTPS=443) |
| **JSON** | Lightweight data format used in APIs (key-value pairs) |
| **SSL/TLS** | Security certificates that enable HTTPS encryption |
| **CRUD** | Create, Read, Update, Delete — basic database operations |
| **REST** | Representational State Transfer — architectural style for APIs |
| **Encryption** | Converting data into a coded format for security |
| **Decryption** | Converting coded data back into readable format |
| **Localhost** | Your own computer acting as a server (127.0.0.1) |

---

## 8. Quick Revision Q&A

### Q1: What happens step-by-step when you visit a website?
**Answer:**
1. You type `youtube.com` in browser
2. Browser asks DNS Resolver for the IP address
3. DNS Resolver contacts Root Server → TLD Server → Authoritative Server
4. IP address is returned to browser (e.g. `142.250.64.78`)
5. Browser sends HTTP/HTTPS request to the Web Server at that IP
6. Web Server processes the request and sends back HTML, CSS, JS
7. Browser renders the webpage and displays it to you ✅

---

### Q2: What is the difference between HTTP and HTTPS?
**Answer:**
- **HTTP** → Data sent as plain text, anyone on the network can read it ❌
- **HTTPS** → Data encrypted with SSL/TLS certificate, safe and secure ✅
- HTTPS uses port 443, HTTP uses port 80
- All modern websites use HTTPS

---

### Q3: What does a 404 error mean?
**Answer:**
- 404 = **Not Found**
- The resource/page you requested does not exist on the server
- Example: Typing a wrong URL like `website.com/abcxyz`

---

### Q4: What is the role of a backend server?
**Answer:**
A backend server:
1. Receives requests from the frontend
2. Validates and processes the data
3. Performs CRUD operations on the database
4. Returns a response (usually JSON) back to the frontend

---

### Q5: What is an API?
**Answer:**
- **API = Application Programming Interface**
- A set of rules that allows different software to communicate with each other
- Acts as a middleman between frontend and backend
- Most common type: **REST API** using HTTP methods (GET, POST, PUT, DELETE)

---

### Q6: What is the difference between Recursive and Iterative DNS?
**Answer:**
- **Recursive** → DNS Resolver does all the work, browser just waits for the final IP
- **Iterative** → Browser/machine itself contacts each DNS server one by one
- Most browsers use **Recursive** DNS by default

---

## 📝 Summary

```
Internet Works  →  DNS finds IP  →  Browser sends HTTP Request
                                              ↓
                                    Web Server receives request
                                              ↓
                                    Backend processes & queries DB
                                              ↓
                                    Server sends HTTP Response
                                              ↓
                                    Browser renders HTML/CSS/JS
                                              ↓
                                    You see the website! ✅
```
