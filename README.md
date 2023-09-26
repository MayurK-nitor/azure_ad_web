# Azure Active Directory Web Python Service

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Configuration](#configuring-aadconfigjson)
  - [Dockerization](#dockerization)
  - [How to Integrate](#how-to-integrate)
- [Flask Service Directory Structure](#flask-service-directory-structure)
- [Azure AD Web Library Structure](#azure-ad-web-library-structure)

## Overview

Our Flask service integrates with Azure Active Directory (Azure AD) to provide secure authentication for your application.We have dockerized our Flask application to make it easy to use and deploy as needed.

## Getting Started

### Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- Python version 3.8
- Docker version 24.0.2

### Configuring aad.config.json

To configure your Azure AD settings, edit the `aad.config.json` file with your custom `client_id`, `client_credential`, and `tenant_id` for your registered Azure app:

```json
"client": {
    "client_id": "client_id",
    "client_credential": "client_credential",
    "authority": "https://login.microsoftonline.com/tenant_id"
}
```


##### 2. Dockerization:
- (i) To build the Docker image and run the container, use the following command:
```
docker-compose up -d --build
```
- (ii) To check the status of containers, use the following command:
```
docker-compose ps
```
- (iii) To stop the container service, use the following command:
```
docker-compose down
```

##### 3. How to Integrate:

To enable Azure AD login, make a request to ```/auth/sign_in``` with current_url as a parameter. The ```current_url``` should be the URL where your current application container is running. 
For example:
```
http://localhost:5000/auth/sign_in?current_url={{current_url}}
```
You will receive a response on your ```index``` URL with an ```identity_context_data``` parameter in encrypted format. To decrypt the data, use the provided encryption key:

```
ENCRYPTION_KEY=b'85m-3ExDEz2wCCNERphWTMVJH29tLn-TEa4DpyDRCWM=' 
```
For example:
In python, we can use ```cryptography``` module for ecryption and decryption.
We can install the ```cryptography``` module using below command 

```
pip install cryptography
```

We can use below ```code``` snippet to decrypt.
```
from cryptography.fernet import Fernet
encryption_key = b'85m-3ExDEz2wCCNERphWTMVJH29tLn-TEa4DpyDRCWM='
cipher_suite = Fernet(encryption_key)

#To Decrypt the parameter
identity_context_data = cipher_suite.decrypt(identity_context_data.encode()).decode()
```

This code snippet illustrates the process of decrypting data using the Fernet cipher suite and your encryption key. You can use a similar approach in your chosen coding platform to handle encryption and decryption as needed. For example, In case of JavaScript, we use the ```crypto``` module from ```Node.js``` to perform encryption and decryption. 
##### Flask Service Directory Structure

####  add.config.json

- This is configuration file where we will keep all the credentials of Azure Active Directory app.( client_id, etc.,)

####  app_config.py

- It is configuration file for Flask Web Application.

#### app.py
- Flask web application and integrates it with Azure Active Directory (Azure AD) for authentication. 


##### Azure AD Web Library Structure
#### __init__.py
- Main common code API is here.

#### flask_blueprint
- A class that implements all aad-specific endpoints. support for multiple instances with different prefixes if necessary
- all bindings are automatic with ```flaskcontextadapter```
#### adapters.py
- ```FlaskContextAdapter``` for handling interaction between the API and flask context (e.g. session, request)
- An ABC defining the interface for writing more adapters.
#### context.py
- ```IdentityContext``` class that holds ID-specific info (simple class with attributes and has_changed function for write-to-session decision)
#### configuration.py
- Simple configuration parser and sanity checker
#### constants.py
- AAD constants
#### errors.py
- AAd error classes



This README provides an organized and detailed explanation of your Flask service, including prerequisites, configuration, Dockerization, integration instructions, directory structures, and library structure. Developers and users will find it helpful in understanding and using your service.
