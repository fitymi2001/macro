############################### GPT API 세팅 시작

import os
# import openai
# openai.api_key = "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"

# """messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
# ]"""

import time
import pyperclip
import sys
import csv
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtWidgets import QFileDialog

from ui_naver_login import Ui_MainWindow

from bs4 import BeautifulSoup

from threading import Thread  # 멀티 스레딩을 위한 모듈

## 기본 폴더 지정
os.chdir("C:\\D\\coding\\python\\work\\naver_LAST")

###############################################################################

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

def CheckXpath(xpath):
    try:
        return driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return None

class Login_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Login_Window, self).__init__()
        self.setupUi(self)
                
        # 버튼이 클릭되었을 때의 연결
        self.LOGIN_Button.clicked.connect(self.start)

    def start(self):
        driver.get("https://naver.com")
        # id 텍스트 창에 있는 텍스트 가져오기
        my_id = self.N_ID_Input.text()
        my_pw = self.N_PW_Input.text()

        # 백그라운드 스레드에서 Selenium 작업 실행
        def background_login():
            driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click() # 로그인창 클릭
            time.sleep(1)

            pyperclip.copy(my_id)
            driver.find_element(By.XPATH, '//*[@placeholder="아이디"]').send_keys(Keys.CONTROL, 'v') # 아이디 입력

            time.sleep(1)

            pyperclip.copy(my_pw)
            driver.find_element(By.XPATH, '//*[@placeholder="비밀번호"]').send_keys(Keys.CONTROL, 'v') # 비밀번호 입력

            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

            time.sleep(1)
        
        # 백그라운드 스레드 실행
        background_thread = Thread(target=background_login)
        background_thread.start()

    def auto_start(self):
        com_count = self.COM_Count.value() # 스핀 박스 값 가져오기
        driver.get("https://blog.naver.com")
        time.sleep(1)
        
        # 오토 댓글, 공감 시작
        def background_comment():
            for i in range(1, com_count+1):
                if i / 10 != 0:
                    j = i % 10
                else:
                    j = i
                driver.find_element(By.XPATH, f'//*[@id="content"]/section/div[2]/div[{j}]/div[1]/div[1]/a[1]').click()
                time.sleep(0.3)
                driver.switch_to.window(driver.window_handles[1])

                # 현재 주소를 or_url 로 저장 ( 중복 대조와 마무리 작업 때 사이트 추가를 위함 )
                or_url = driver.current_url
                    
                try:
                    # 파일 열기
                    df = pd.read_csv('websites.csv')
                    # 파일 읽기
                    print(df)
                except FileNotFoundError:
                    df = pd.DataFrame({'URL':['https://blog.naver.com']})
                    df.to_csv('websites.csv', index=False)
                                        
                # 현재 웹사이트와 대조
                if or_url not in df['URL'].values:
                    try:
                        # mainFrame 프레임 요소 찾기
                        main_frame = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="mainFrame"]'))
                        )
                        
                        # mainFrame 프레임으로 전환
                        iframe_url = driver.find_element(By.XPATH, '//*[@id="mainFrame"]')
                        url = iframe_url.get_attribute("src")
                        
                        # 프레임 내부에서 필요한 작업 수행
                        # 예를 들어, 프레임 내의 요소를 찾아 조작하는 등의 작업 수행
                        
                    except Exception as e:
                        print("mainFrame을 찾을 수 없거나 접근할 수 없습니다.", e)           
                    
                    
                    driver.get(url)
                    
                    driver.implicitly_wait(10)

                    # 페이지 소스 가져오기
                    page_source = driver.page_source

                    # BeautifulSoup을 사용하여 파싱
                    soup = BeautifulSoup(page_source, 'html.parser')

                    # se-main-container 클래스를 가진 태그 찾기
                    main_container_tag = soup.find('div', class_='se-main-container')

                    # 모든 하위 태그의 텍스트 추출
                    all_subcontent_text = main_container_tag.get_text(strip=True)  # 공백 문자 제거 추가

                    print(all_subcontent_text + "\n\n")

                    ### 스크랩한 본문 간략화

                    front_part = all_subcontent_text[:100] # 앞에서 100글자
                    back_part = all_subcontent_text[-100:] # 뒤에서 100글자

                    combined_variable = front_part + back_part

                    print(combined_variable + "\n\n")

                    ############### GPT API 를 이용해 소통

                    messages = []
                    user_content = combined_variable + "라는 블로그 글에 댓글을 달거야. 블로그 이웃이 글을 남기는 것 처럼. 20자 이내로 간단한 코멘트 남겨줘 (특수기호, 따옴표 이런 거 넣지마)"
                    messages.append({"role": "user", "content": f"{user_content}"})

                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=700)

                    gpt_comment = completion.choices[0].message['content'] # gpt 코멘트를 gpt_comment 변수에 문자열 저장

                    print(gpt_comment)
                    print(completion["usage"]) # 토큰 사용량 터미널에 출력

                    time.sleep(2)

                    # 스크롤 내리기
                    scroll_distance = 1000  # 스크롤할 거리(px)
                    script = f"window.scrollBy(0, {scroll_distance});"  # JavaScript 스크립트
                    driver.execute_script(script)

                    time.sleep(3)

                    # 좋아요 버튼 클릭
                    driver.find_element(By.CLASS_NAME, 'u_likeit_list_module').click()

                    # 댓글 버튼 클릭
                    driver.find_element(By.CSS_SELECTOR, '.comment_wrap').click() 

                    time.sleep(3)

                    #댓글에 gpt 코멘트 입력
                    pyperclip.copy(gpt_comment)
                    driver.find_element(By.CSS_SELECTOR, '.u_cbox_text').send_keys(Keys.CONTROL, 'v') 

                    time.sleep(2.3)

                    driver.find_element(By.CSS_SELECTOR, '.u_cbox_btn_upload').click() # 댓글 업로드

                    time.sleep(1)

                    # websites.csv 에 현재 웹사이트 추가
                    f = open('websites.csv', 'a', encoding='utf-8', newline='')
                    wr = csv.writer(f)
                    wr.writerow([or_url])
                    f.close()                    
                    
                    #driver.find_element(By.CSS_SELECTOR, '.u_likeit_list_btn').click() # 공감 클릭
                
                time.sleep(0.6)    
                
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                
                time.sleep(1)
                
                time.sleep(self.COM_Interval.value())
                
        c_background_thread = Thread(target=background_comment)
        c_background_thread.start()
        
    def fri_start(self):
        driver.get("https://blog.naver.com")
        
        def background_friend():
            time.sleep(1)
        
        
        f_background_Thread = Thread(tartget=background_friend)
        f_background_Thread.start()
        
            
def main():
    app = QApplication(sys.argv)
    window = Login_Window()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()