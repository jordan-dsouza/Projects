#Query defines and validates query parameters, HTTPException raises HTTP errors:
from fastapi import FastAPI, Query, HTTPException
#CORSMiddlware is security mechanism which restirtcs webpage from making requests to different domain other than original:
#CORS = Cross-Origin Resource Sharing allows client to call API:
from fastapi.middleware.cors import CORSMiddleware
#Import function from excel parser to parse excel file:
from Excel_parser_Iris import load_excel, get_table_names, get_row_names, get_row_sum

#Initialize fast api: 
app = FastAPI()
#Allow any origin (frontend like React/Angular) to make request:
app.add_middleware(CORSMiddleware, allow_origins=["*"])

#Load excel data from path:
EXCEL_PATH = "Data/capbudg.xls"
excel_data = load_excel(EXCEL_PATH)

#API Endpoints with @app.get():

@app.get("/list_tables")
def list_tables():
    return {"tables": get_table_names(excel_data)}

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    if table_name not in excel_data:
        #If no table raise HTTP error:
        raise HTTPException(status_code=404, detail="Table not found")
    return {
        "table_name": table_name,
        "row_names": get_row_names(excel_data, table_name)
    }

@app.get("/row_sum")
def row_sum(
    table_name: str = Query(...),
    row_name: str = Query(...)
):
    if table_name not in excel_data:
        raise HTTPException(status_code=404, detail="Table not found")
    rows = get_row_names(excel_data, table_name)
    if row_name not in rows:
        raise HTTPException(status_code=404, detail="Row not found")
    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": get_row_sum(excel_data, table_name, row_name)
    }

@app.get("/")
def root():
    return {"message": "FastAPI Excel Processor is running"}
