import time
import pandas as pd
from playwright.sync_api import sync_playwright

TARGET_URL = "https://x.com/barisunver/status/2004440308935958787?s=46&t=AwSrJo8dsVbI9rliw0-2lw"

SCROLL_COUNT = 300

OUTPUT_FILE = "tweet_replies3.csv"

def scrape_replies():
    print("Veri çekme işlemi başlatılıyor...")

    replies_data = []
    seen_tweets = set()

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False, args=["--start-maximized"])
            # 'twitter_auth.json' dosyasının login.py ile aynı klasörde olduğundan emin ol
            context = browser.new_context(storage_state="twitter_auth.json", no_viewport=True)
            page = context.new_page()
        except FileNotFoundError:
            print("HATA: 'twitter_auth.json' dosyası bulunamadı. Önce login işlemini yapmalısın.")
            return

        print(f"Hedef linke gidiliyor: {TARGET_URL}")
        page.goto(TARGET_URL, timeout=60000)

        page.wait_for_selector('article[data-testid="tweet"]', timeout=15000)
        print("Sayfa yüklendi, yanıtlar toplanıyor...")
        time.sleep(3)

        for i in range(SCROLL_COUNT):
            print(f"🔄 Sayfa kaydırılıyor... ({i + 1}/{SCROLL_COUNT})")

            tweets = page.locator('article[data-testid="tweet"]').all()

            for tweet in tweets:
                try:
                    text_locator = tweet.locator('div[data-testid="tweetText"]')

                    if text_locator.count() == 0:
                        continue

                    text = text_locator.inner_text().replace("\n", " ")

                    user_locator = tweet.locator('div[data-testid="User-Name"]')
                    user_info = user_locator.inner_text().split("\n")
                    handle = user_info[1] if len(user_info) > 1 else "Unknown"

                    time_locator = tweet.locator('time')
                    tweet_time = time_locator.get_attribute("datetime") if time_locator.count() > 0 else "Unknown"

                    unique_id = f"{handle}-{text[:30]}"

                    if unique_id not in seen_tweets:
                        replies_data.append({
                            "User": handle,
                            "Text": text,
                            "Date": tweet_time
                        })
                        seen_tweets.add(unique_id)

                except Exception as e:
                    continue

            page.evaluate("window.scrollBy(0, 1500)")

            time.sleep(2.5)

        browser.close()

    if replies_data:
        df = pd.DataFrame(replies_data)
        df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
        print(f"\n İŞLEM TAMAMLANDI!")
        print(f"Toplam {len(replies_data)} adet yanıt çekildi.")
        print(f"Dosya kaydedildi: {OUTPUT_FILE}")
    else:
        print(
            "\n Hiç veri çekilemedi. Seçiciler (selectors) değişmiş olabilir veya internet bağlantısında sorun var.")


if __name__ == "__main__":
    scrape_replies()