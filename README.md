# Django and React Account Transfer Project

## Overview

This project demonstrates how to integrate a Django backend with a React frontend. The Django backend provides APIs for account management, including importing accounts from a CSV file, listing accounts, retrieving account details, and transferring funds between accounts.


## Functionality 

• Import accounts from CSV files.
• List all accounts.
• Get account information.
• Transfer funds between two accounts.


## Prerequisites

- Docker
- Docker Compose

## Backend Setup

### 1. Clone the Repository

```sh
git clone <repository-url>
cd <repository-directory>
```

### 2. Build and Run the Project with Docker Compose

``` sh
docker compose up --build
``` 


## Project Functionality :

#### Import Accounts from CSV

1. Navigate to the Import CSV section in the React app.
2. Upload a CSV file containing account data.

#### List Accounts

1. Navigate to the List Accounts section in the React app.
2. View the list of accounts.

#### Get Account Details

1. Navigate to the Account Details section in the React app.
2. Enter the UUID of an account to retrieve its details.

#### Transfer Funds

1. Navigate to the Transfer Funds section in the React app.
2. Enter the sender ID, receiver ID, and the amount to transfer funds.




## Running Tests
### Backend Tests

1- Access the running backend container:
```
docker exec -it <container-name>  bash
```
2- Run the tests:

```
python manage.py test
```


### Frontend Tests

1- Access the running backend container:
```
docker exec -it <container-name>  /bin/sh
```
2- Run the tests:

```
npm test
```
