from flask import Flask, render_template, request
import random

app = Flask(__name__)

gemi = {
    "enerji": 100,
    "mesafe": 0,
    "hedef": 500,
    "mesaj": "gemi hazır.",
    "bitti": False,
    "tema": "tema-mavi", # Artık renk kodu yok, tema ismi var
    "yuzde": 0
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        islem = request.form.get("islem")
        
        if islem == "reset":
            gemi.update({"enerji": 100, "mesafe": 0, "bitti": False, "mesaj": "Sıfırlandı!", "tema": "tema-mavi", "yuzde": 0})
        
        elif not gemi["bitti"]:
            if islem == "git":
                gemi["mesafe"] += random.randint(40, 80)
                gemi["enerji"] -= random.randint(15, 25)
                gemi["mesaj"] = "Hızlandık! Motorlar tam güç."
                gemi["tema"] = "tema-yesil"
            
            elif islem == "onar":
                gemi["enerji"] += random.randint(20, 30)
                gemi["mesaj"] = "Onarım yapıldı, enerji arttı."
                gemi["tema"] = "tema-sari"

            if gemi["enerji"] <= 0:
                gemi["enerji"] = 0
                gemi["bitti"] = True
                gemi["tema"] = "tema-kirmizi"
                gemi["mesaj"] = "Enerji bitti! Uzayda kaldık."
            
            if gemi["mesafe"] >= gemi["hedef"]:
                gemi["mesafe"] = gemi["hedef"]
                gemi["bitti"] = True
                gemi["tema"] = "tema-mor"
                gemi["mesaj"] = "Hedefe ulaştık! Görev başarılı."
            
            # Yüzdeyi saf bir sayı olarak hesaplıyoruz
            gemi["yuzde"] = int((gemi["mesafe"] / gemi["hedef"]) * 100)

    return render_template("index.html", v=gemi)

if __name__ == "__main__":
    app.run(debug=True)