# Flight Deals Finder

A Python project that searches for flight prices and sends an SMS alert when it finds a fare below the target price stored in a Sheety spreadsheet.

## Features

- Reads destination cities and target prices from a Sheety spreadsheet.
- Searches Google Flights results through SerpApi.
- Finds the lowest available flight price.
- Updates the spreadsheet when a cheaper flight is found.
- Sends an SMS notification through Twilio.
- Caches flight-search requests to reduce repeated API calls.

## Project Structure

```text
flight-deals-start/
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- A Sheety account and spreadsheet
- A SerpApi API key
- A Twilio account for SMS notifications

## Setup

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   python3 -m pip install requests requests-cache python-dotenv twilio
   ```

5. Create your environment file by copying the example:

   ```bash
   cp .env.example .env
   ```

6. Add your own credentials and configuration values to `.env`. Do not upload this file to GitHub.
7. Make sure your Sheety spreadsheet has the expected destination data, including `city`, `iataCode`, `lowestPrice`, and `id`.
8. Run the program:

   ```bash
   python main.py
   ```

## Environment Variables

See `.env.example` for the required variable names:

- `SHEETY_USERNAME` and `SHEETY_PASSWORD` — Sheety authentication, if required by your setup.
- `SHEETY_ENDPOINT` — the endpoint for your Sheety prices sheet.
- `SERPAPI_API_KEY` — SerpApi key used for flight searches.
- `TWILIO_SID`, `TWILIO_AUTH_TOKEN` — Twilio account credentials.
- `TWILIO_VIRTUAL_NUMBER`, `TWILIO_VERIFIED_NUMBER` — Twilio sender and recipient numbers.

## Notes

- This project makes requests to external services and requires valid API credentials.
- API response formats, account permissions, and service pricing/limits may change.
- The current search settings in `main.py` use London Heathrow (`LHR`) as the origin and search dates starting tomorrow through roughly six months ahead.
- SMS alerts require a properly configured Twilio account and verified recipient where applicable.
