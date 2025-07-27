import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, iradon
from skimage.transform import resize

# ----- مرحله ۱: آماده‌سازی تصویر فانتوم -----
image_size = 256
phantom = shepp_logan_phantom()
phantom = resize(phantom, (image_size, image_size), mode='reflect', anti_aliasing=True)

# ----- مرحله ۲: تولید سینوگرام با تبدیل Radon -----
theta = np.linspace(0., 180., max(phantom.shape), endpoint=False)
sinogram = radon(phantom, theta=theta, circle=True)

# ----- مرحله ۳: بازسازی تصویر با تبدیل معکوس Radon -----
reconstruction = iradon(sinogram, theta=theta, filter_name='ramp', circle=True)

# ----- مرحله ۴: نمایش نتایج -----
fig, axes = plt.subplots(1, 3, figsize=(12, 4.5))
axes[0].set_title("Original Phantom")
axes[0].imshow(phantom, cmap=plt.cm.Greys_r)
axes[0].axis('off')

axes[1].set_title("Sinogram (Radon Transform)")
axes[1].imshow(sinogram, cmap=plt.cm.Greys_r,
               extent=(0, 180, 0, sinogram.shape[0]), aspect='auto')
axes[1].set_xlabel('Angle (degrees)')
axes[1].set_ylabel('Projection position')

axes[2].set_title("Reconstructed Image")
axes[2].imshow(reconstruction, cmap=plt.cm.Greys_r)
axes[2].axis('off')

plt.tight_layout()
plt.savefig("ct_simulation_output.png")
plt.show()