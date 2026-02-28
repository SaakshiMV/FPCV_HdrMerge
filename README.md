# HDR Streamlit App 🌄

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-app-red)
![OpenCV](https://img.shields.io/badge/opencv-contrib-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

An interactive **High Dynamic Range (HDR) image merging application** built with **Streamlit**.

This app simulates multiple exposures from a single image, merges them into an HDR image using OpenCV, and applies tone mapping — all in real time through a clean browser interface.

---

## 🖼 Preview

<img width="1780" height="369" alt="HDR Preview" src="https://github.com/user-attachments/assets/40e3cc7f-8f5e-458b-8b50-fb8e3326aa7f" />

---

## ✨ Overview

Traditional HDR photography requires multiple images captured at different exposures.  
This application simulates that process from a **single base image**, allowing users to:

- Generate synthetic exposures (dark, mid, bright)
- Merge them into HDR using **MergeDebevec**
- Apply tone mapping for visual display
- Experiment interactively with exposure and gamma controls

It’s ideal for:

- Learning HDR fundamentals
- Understanding exposure fusion
- Experimenting with tone mapping parameters

---

## 🚀 Features

✔ Upload **any JPG/PNG image**  
✔ Simulate **3 exposure levels** (Dark / Mid / Bright)  
✔ HDR merge using **OpenCV MergeDebevec**  
✔ Tone mapping options:
   - **Durand method** (if OpenCV contrib is installed)
   - **Safe fallback normalization** (cross-platform compatible)  
✔ Interactive **exposure factor sliders**  
✔ Adjustable **gamma correction**  
✔ Side-by-side visualization of:
   - Base image  
   - All simulated exposures  
   - Final HDR output  
✔ Download tone-mapped HDR image  
✔ Fully cross-platform (Windows / Linux / macOS)

---

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/HDR_Streamlit.git
cd HDR_Streamlit
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

Streamlit will automatically open the app in your default browser.

---

## 🧭 How to Use

1. Launch the Streamlit app
2. Upload a base image
3. Adjust:

   * Dark exposure factor
   * Bright exposure factor
   * Gamma correction
4. View simulated exposures and HDR result instantly
5. Download the final tone-mapped HDR image

---

## 📂 Project Structure

```
HDR_Streamlit/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md
├── data/                  # Optional input images
│   └── example.jpg
└── output_images/         # Generated HDR outputs (auto-saved)
```

---

## ⚙️ Technical Notes

* HDR merging is performed using **OpenCV MergeDebevec**
* Tone mapping uses:

  * **Durand operator** (if `opencv-contrib-python` is installed)
  * Fallback normalization for universal compatibility
* Designed to run entirely from the **terminal / command prompt**
* No GPU required

---

## 📦 Dependencies

* Python 3.8+
* Streamlit
* OpenCV (`opencv-contrib-python` recommended)
* NumPy
* Pillow

Install manually if needed:

```bash
pip install streamlit opencv-contrib-python numpy pillow
```

---

## 🔮 Possible Enhancements

* Real multi-image HDR input (true exposure stacks)
* Additional tone mapping operators (Reinhard, Mantiuk)
* Histogram visualization
* Exposure presets
* Save exposure stack as ZIP

---

## 📜 License

This project is open-source. Consider adding an MIT License file if not already included.
