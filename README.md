# FastAPI Text File CRUD

This project demonstrates a simple FastAPI implementation for performing CRUD operations on a text file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MamangRust/fastapi-text-file-crud.git
2. Change into the project directory:
   ```bash
    cd fastapi-text-file-crud

   ```
3. Install the required dependencies:
   ```bash
    pipenv install
   ```

## Usage

1. Run the FastAPI server:
   ```bash
   python main.py
   ```
2. Access the FastAPI interactive documentation at `http://127.0.0.1:8000/docs`:
   
## Endpoints

### Create Data

- **Endpoint:** `/create_data/`
- **Method:** `POST`
- **Description:** Creates new data in the text file.

#### Request Body

```json
{
  "data": "Your data here"
}
```

#### Response
- **Status Code::** `200 OK`
- **Response Body:** `{ "message": "Data created successfully" }`


### Read All Data

- **Endpoint:** `/read_all_data/`
- **Method:** `GET`
- **Description:** Retrieves all data from the text file.


#### Response
- **Status Code::** `200 OK`
- **Response Body:** `[ "Data 1", "Data 2", ... ]`


### Find Data by ID

- **Endpoint:** `/find_by_id/{target_id}`
- **Method:** `GET`
- **Description:** Finds data by ID from the text file.


#### Response
- **Status Code::** `200 OK`
- **Response Body:** `mengolang`


### Update Data

- **Endpoint:** `/update_data/{index}`
- **Method:** `PUT`
- **Description:** Updates data at a specific index in the text file.


#### Request Body

```json
{
  "data": "Your data here"
}
```

#### Response
- **Status Code::** `200 OK`
- **Response Body:** `{ "message": "Data at index {index} updated successfully" }`


### Delete Data

- **Endpoint:** `/delete_data/{target_id}`
- **Method:** `GET`
- **Description:** Deletes data at a specific index from the text file.


#### Response
- **Status Code::** `200 OK`
- **Response Body:** `{ "message": "Data at index {index} deleted successfully" }`



Pastikan untuk menyesuaikan deskripsi, status code, dan struktur respons sesuai dengan proyek FastAPI Anda.
