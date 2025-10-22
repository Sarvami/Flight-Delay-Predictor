# Flight-Delay-Predictor
Predict flight arrival delays using machine learning. Includes Jupyter Notebook, trained model, and Streamlit app.
Ah — now the problem is **your dataset file is too large for GitHub**. GitHub has a **100 MB limit per file**, and your `data/DelayedFlights.csv` is **234 MB**.

You have a few options:

---

### **Option 1 — Remove the large dataset from Git and push**

1. Remove the dataset from Git tracking (don’t delete it locally):

```bash
git rm --cached data/DelayedFlights.csv
```

2. Commit the change:

```bash
git commit -m "Remove large dataset to comply with GitHub limits"
```

3. Push again:

```bash
git push -u origin main
```

✅ Your repository will now push successfully.

> Note: Users cloning the repo won’t get the dataset. You can provide a **download link** in your README.

---

### **Option 2 — Use Git Large File Storage (Git LFS)**

* Install Git LFS: [https://git-lfs.github.com](https://git-lfs.github.com)
* Track the large file:

```bash
git lfs install
git lfs track "data/DelayedFlights.csv"
git add .gitattributes
git add data/DelayedFlights.csv
git commit -m "Track large CSV with Git LFS"
git push origin main
```

✅ This allows pushing files larger than 100 MB.

---

**Recommendation:** For a portfolio project, usually **Option 1 is simpler** — remove the CSV and provide a download link in your README.

If you want, I can **update your README** with a section telling others how to download the dataset, so your GitHub repo stays under limits. Do you want me to do that?


Exactly — I can rewrite your README so it **removes the large CSV from GitHub** but still tells users how to get it. Here’s a clean version you can replace your current README with:

---

# Flight Delay Predictor

## **Overview**

This project predicts **flight arrival delays** using historical flight data.
It includes:

* Data cleaning and feature engineering in a **Jupyter Notebook**.
* A **Random Forest regression model** to predict arrival delay in minutes.
* A **Streamlit app** for users to input flight details and get delay predictions.

---

## **Project Structure**

```
project_folder/
│
├── notebooks/
│   └── flight_delay_notebook.ipynb   # Data cleaning, feature engineering, model training
│
├── models/
│   └── delay_model.pkl               # Trained Random Forest model
│
├── app/
│   └── app.py                        # Streamlit app for predictions
│
├── data/                             
│   └── (dataset not included due to size) 
│
├── requirements.txt                   # Python dependencies
└── README.md                         # This file
```

---

## **Dataset**

* The original dataset is **large (~235 MB)** and cannot be included in the repo.
* You can download it here: https://www.kaggle.com/datasets/giovamata/airlinedelaycauses?resource=download
* Features used for modeling:

  * `Distance`
  * `DepDelay`
  * `CRS_DEP_HOUR` (scheduled departure hour)
  * Carrier dummies (`UniqueCarrier`)

---

## **How to Run the Notebook**

1. Place the downloaded dataset in the `data/` folder.
2. Open `flight_delay_notebook.ipynb` in Jupyter Notebook.
3. Run all cells in order.
4. The model (`delay_model.pkl`) will be saved in the `models/` folder.

---

## **How to Run the Streamlit App**

1. Navigate to the `app/` folder:

```bash
cd app
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Enter flight details in the sidebar:

   * Distance (miles)
   * Departure Delay (minutes)
   * Scheduled Departure Hour (0–23)
   * Carrier

4. The app outputs the **predicted arrival delay in minutes**.

---

## **Optional Enhancements**

* Add **Weekday** as a feature when retraining the model.
* Add **“Is Delayed?”** classification (>15 minutes).
* Improve UI/UX in the Streamlit app with charts or color-coded outputs.

---

## **Dependencies**

* Python 3.x
* pandas
* numpy
* scikit-learn
* joblib
* streamlit

Install dependencies with:

```bash
pip install -r requirements.txt
```

