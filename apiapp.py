from fastapi import FastAPI


app = FastAPI()

richest_people_list = {
    "Eloln Musk": "280 Billion USD",
    "Jeff Bezos": "259 Billion USD",
    "Bill Gates": "190 Billion USD",
    "Mark Zuckerberg": "150 Billion USD"
}

@app.get("/richest-people")
def richest_people():
    return richest_people_list