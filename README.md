# **HDR Streamlit App**

Interactive HDR Image Merge with simulated exposures and tone mapping.

Merge multiple exposures from a single image into HDR and visualize the results with **Streamlit**.

---

## **Features**

* Upload **any base image** (JPG/PNG)
* Simulates **3 exposures** (dark, mid, bright)
* HDR merge using **OpenCV MergeDebevec**
* Tone mapping with:

  * **Durand** (if available)
  * **Fallback normalization** (cross-platform safe)
* Interactive **sliders for exposure factors and gamma**
* Side-by-side display of **all exposures + HDR output**
* **Download** the HDR tone-mapped image
* Fully **CMD and cross-platform compatible**

---

## **Project Structure**

```
HDR_Streamlit/
│
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── data/                  # Optional: upload your base images here
│   └── example.jpg
└── output_images/         # HDR outputs will be saved here automatically
```

---

## **Demo**

**Before:** Base image

**Simulated Exposures:** Dark / Mid / Bright

**HDR Output:** Tone-mapped HDR result

*(Images displayed side-by-side in the Streamlit app)*

---

## **Installation & Run**

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/HDR_Streamlit.git
cd HDR_Streamlit
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

4. Upload a base image in the browser → adjust exposures + gamma → see HDR result → download the image.

---

## **Notes**

* Works entirely in **CMD / terminal** (Windows, Linux, Mac)
* HDR tone mapping uses **Durand method** if OpenCV contrib package is installed.
* Fallback normalization ensures **compatibility across all systems**.
* You can **adjust exposure factors and gamma** interactively for better HDR results.

---

## **Dependencies**

* Python 3.8+
* [Streamlit](https://streamlit.io/)
* [OpenCV](https://opencv.org/) (`opencv-contrib-python` recommended)
* NumPy
* Pillow

---

