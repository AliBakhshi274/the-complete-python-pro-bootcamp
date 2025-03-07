import smtplib
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.com/Armitron-Sport-45-7004BLU-Chronograph/dp/B006ZTJEPC/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.db94be39-53f1-4c79-89b2-88aa81be709e&dib=eyJ2IjoiMSJ9.kg1ybgH5LLeqEte3Iol634KbER90t0ZbLr4PuMJZFgaZCAV6u1aAgc98UfTrsypiNF7vyF0xdcgl2xDfAlg1igHUaxaMzZ3XL6GvPq8QZ36O6XwniRQ-s7DHazWHZNee25l9FnOOndOU5_qi4B-zhyXhQx58o3_MMBNFqJTDxfluB9YKYUzMnEjMpNYYlXnOaHH5jHICAmzqSPL5sBNlQSPPKQsFBa3MQTzT3TJlIC-FPP8uBEQj_ToPdzaVa986WoiTdSJh_wkP5q6qd2qjvWylJ_Re82vLGxWXHLzn0un-wk02GMCsL_MKsm5W-UhxEJGfbYgzkwq_KWfUH-ZtwBzMQelcp5-RHnZtPhhlOMSuzaM5YPGC0q3NsBZQyixYS5twRFjCJ025DiqcWHboD6PhlpviIKH8iwI9ozdb1BuieHi-n45Yq8_KcKq4_hPW.B4X8zWVonDC-WPFfrTyFtQ_GCBUD1X8qBXky_oqi9z4&dib_tag=se&keywords=Boys%2Bwatches&pd_rd_r=588e05d5-d221-4b5d-a731-aad13ca6cd26&pd_rd_w=TeQhv&pd_rd_wg=piPZt&qid=1741180912&sr=8-2&th=1"
email_port_num = os.environ.get("EMAIL_PORT_NUM")
from_addr = os.environ.get("FROM_ADDR")
to_addr = os.environ.get("TO_ADDR")
email_password = os.environ.get("EMAIL_PASSWORD")

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}


response = requests.get(url, headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(name="span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").get_text()
price_as_float = float(price.split("$")[1])
print(price_as_float)

title = soup.find(id="productTitle").get_text()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price_as_float}$!"
    with smtplib.SMTP(host="smtp.gmail.com", port=email_port_num) as connection:
        connection.starttls()
        result = connection.login(user=from_addr, password=email_password)
        connection.sendmail(from_addr,
                            to_addr,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8"))



