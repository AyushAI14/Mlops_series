from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def form_page():
    return """
        <html>
            <head>
                <title>Enter Your Name</title>
            </head>
            <body>
                <h2>Welcome</h2>
                <form action="/submit" method="post">
                    <input type="text" name="name" placeholder="Enter your name">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    """

@app.post("/submit")
async def handle_form(name: str = Form(...)):
    return {'Message': f'Hello {name}'}

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=5000)
