import httpx
import typer

# Chuck Norris jokes API URL. Documentation: https://api.chucknorris.io/
API_URL = "https://api.chucknorris.io/jokes"

# Accept a plain text request, the subject of the joke search.

app = typer.Typer()

def fetch(httpx_client: httpx.Client, subject: str) -> str:
    response = httpx_client.get(f"{API_URL}/search", params={"query": subject})
    response.raise_for_status()
    return response.json()

@app.command()
def main(subject: str):
    httpx_client = httpx.Client()
    fetch(httpx_client, subject)

if __name__ == "__main__":
    app()