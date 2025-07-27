# Simple CT Scanner Simulation

This project simulates a basic CT (computed tomography) scanner using the Radon transform. It demonstrates how an image can be reconstructed from its projections taken at multiple angles.

---

## 🔍 Description

- Uses a Shepp-Logan phantom image (standard synthetic image for CT)
- Simulates CT projections (sinogram) via Radon transform
- Reconstructs the original image using inverse Radon (filtered back projection)
- Visualizes:
  - Original image
  - Sinogram
  - Reconstructed image

---

## 📦 Requirements

Install with:

`bash
pip install -r requirements.txt
