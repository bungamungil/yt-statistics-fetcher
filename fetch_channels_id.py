from google.oauth2 import service_account
import gspread
import os


def auth_google():
    """
    Authenticate with Google and return the token
    """ 
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_CREDENTIALS")
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return credentials


def read_rows_from_google_sheet(sheet_id):
    """
    Read rows from a Google Sheet
    """
    gc = gspread.authorize(auth_google())
    sh = gc.open_by_key(sheet_id)
    worksheet = sh.get_worksheet_by_id(int(os.getenv("GOOGLE_SHEET_WORKSHEET_ID")))
    rows = worksheet.get_all_values()
    return rows


def fetch_channels_id():
    rows = read_rows_from_google_sheet(os.getenv("GOOGLE_SHEET_ID"))
    map_channel_id = lambda row: row[0]
    return list(map(map_channel_id, rows))
