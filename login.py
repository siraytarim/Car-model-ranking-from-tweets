from playwright.sync_api import sync_playwright
import os

def save_session():
    print("Sistemdeki Orijinal Chrome başlatılıyor...")

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    if not os.path.exists(chrome_path):
        print("HATA: Chrome.exe bulunamadı! Lütfen dosya yolunu kontrol et.")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=chrome_path,
            headless=False,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )

        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        try:
            print("Twitter'a gidiliyor...")
            page.goto("https://twitter.com/login", timeout=60000)

            print("-" * 50)
            print("LÜTFEN DİKKAT:")
            print("Bu senin gerçek Chrome tarayıcın olduğu için Twitter seni daha az şüpheli görecek.")
            print("Giriş yap ve işlemi bitirince buraya gelip ENTER'a bas.")
            print("-" * 50)

            input("Giriş yaptıktan sonra ENTER'a basmak için bekleniyor...")

            context.storage_state(path="twitter_auth.json")
            print("BAŞARILI: Oturum kaydedildi!")

        except Exception as e:
            print(f" HATA: {e}")

        finally:
            browser.close()


if __name__ == "__main__":
    save_session()