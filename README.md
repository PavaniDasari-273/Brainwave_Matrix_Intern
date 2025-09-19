# 📰 Fake News Detection using Machine Learning

## 📌 Overview

Fake news spreads rapidly on digital platforms, influencing opinions and creating misinformation.
This project aims to **detect whether a news article is Real or Fake** using **Machine Learning & Natural Language Processing (NLP)** techniques.

I also built an **interactive Streamlit Web App** that allows users to enter any news text and instantly check its authenticity.

---

## ⚡ Features

* ✅ Detects if a given news article is **Real** or **Fake**
* ✅ Preprocessing with tokenization, stopword removal & lemmatization
* ✅ Feature extraction using **TF-IDF Vectorization**
* ✅ Trained **Logistic Regression model** for classification
* ✅ Interactive UI built with **Streamlit**

---

## 🛠 Tech Stack

* **Python 3**
* **Streamlit** – Web App Framework
* **Scikit-learn** – ML Algorithms
* **Joblib** – Model persistence
* **Pandas / Numpy** – Data handling
* **NLTK** – Text Preprocessing

---

## 📂 Project Structure

```
├── app.py                 # Streamlit web app  
├── lr_model.jb            # Trained Logistic Regression model  
├── vectorizer.jb          # TF-IDF Vectorizer  
├── requirements.txt       # Required dependencies  
├── dataset/               # News dataset (Fake & Real)  
└── README.md              # Project documentation  
```

---

## 🚀 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Fake-News-Detection.git
   cd Fake-News-Detection
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open the link shown in the terminal (default: `http://localhost:8501`)

---

## 📸 Screenshots



---

## 🔮 Future Enhancements

* Implement **Deep Learning models (LSTM, BERT)** for better accuracy
* Deploy on **Heroku/Streamlit Cloud** for public access
* Add real-time news scraping & fact-check integration

---

## 🙏 Acknowledgement

Special thanks to **Brainwave Matrix Solutions** for giving me this project.

---

## 📌 Author

👩‍💻 Pavani Dasari

📫 Connect with me: [LinkedIn](www.linkedin.com/in/pavani-dasari-691bb5321) | [GitHub](https://github.com/PavaniDasari-273)

---






