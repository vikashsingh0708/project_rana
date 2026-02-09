import qrcode
import os

base_url = "https://YOUR_USERNAME.github.io/evs_assignment/"

plants = [
    "tulsi.html",
    "neem.html",
    "mango.html",
    "rose.html",
    "lotus.html",
    "sunflower.html",
    "peepal.html",
    "bamboo.html",
    "aloevera.html",
    "sheesham.html"
]

output_folder = "qr_codes"

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for plant in plants:
    url = base_url + plant
    qr = qrcode.make(url)
    qr_name = plant.replace(".html", ".png")
    qr.save(os.path.join(output_folder, qr_name))

print("All QR codes generated successfully.")