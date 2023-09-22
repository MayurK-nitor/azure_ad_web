# Azure Active Directory Web Python Service

Our flask service will act as integrated application of your application. So we have dockerize our flask application so we will prefer that you can use our docker file as per your needs.

### Prerequisites

- Python 3.8
- Docker version 24.0.2

##### 1. Configuring aad.config.json

- Configure add.config.json to set custom client_id, client_credential, tenant_id of your registered azure app

eg. In add.config.json

```
"client": {
        "client_id": "client_id",
        "client_credential": "client_credential",
        "authority": "https://login.microsoftonline.com/tenant_id"
    },
```


##### 2. Dockerization:
- (i)Build the docker image and run the container using this command 
```
docker-compose up -d --build
```
- (ii)check containers status using this command
```
docker-compose ps
```
- (iii)To down the container service using this command 
```
docker-compose down
```

##### 3. In your Project build on any coding platform

While getting the response use below encryption key to decrypt data('identity_context_data)
```
ENCRYPTION_KEY=b'85m-3ExDEz2wCCNERphWTMVJH29tLn-TEa4DpyDRCWM=' 
```


for eg. In python, we can use ```cryptography``` module for ecryption and decryption.
so we can install the ```cryptography``` module using below command 

```
pip install cryptography
```

and then we can use below ```code``` snippet to decrypt.
```
from cryptography.fernet import Fernet
encryption_key = b'85m-3ExDEz2wCCNERphWTMVJH29tLn-TEa4DpyDRCWM='
cipher_suite = Fernet(encryption_key)

#To Decrypt the parameter
identity_context_data = cipher_suite.decrypt(identity_context_data.encode()).decode()
```


##### Azure AD Web Library Structure
#### __init__.py
- main common code API is here.

#### flask_blueprint
- a class that implements all aad-specific endpoints. support for multiple instances with different prefixes if necessary
- all bindings are automatic with flaskcontextadapter
#### adapters.py
- FlaskContextAdapter for handling interaction between the API and flask context (e.g. session, request)
- An ABC defining the interface for writing more adapters
- Should be re-organised into folders on a per-framework basis?
#### context.py
- IdentityContext class that holds ID-specific info (simple class with attributes and has_changed function for write-to-session decision)
#### configuration.py
- simple configuration parser and sanity checker
#### constants.py
- AAD constants
#### errors.py
- AAd error classes
