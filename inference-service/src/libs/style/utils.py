import numpy as np
from PIL import Image
from torchvision import transforms


def load_image(path):
    image = Image.open(path)
    R, G, B = image.split()
    image = Image.merge("RGB", (B, G, R))
    data = np.array(image)

    return data


def saveimg(img, image_path):
    img = img.clip(0, 255)
    img = img.astype(int)
    img = Image.fromarray((img).astype(np.uint8))
    R, G, B = img.split()
    img = Image.merge("RGB", (B, G, R))
    img.save(image_path, format="JPEG", subsampling=0, quality=100)


# Preprocessing ~ Image to Tensor
def itot(img, max_size=None):
    # Rescale the image
    if max_size is None:
        itot_t = transforms.Compose(
            [transforms.ToTensor(), transforms.Lambda(lambda x: x.mul(255))]
        )
    else:
        H, W, C = img.shape
        image_size = tuple([int((float(max_size) / max([H, W])) * x) for x in [H, W]])
        itot_t = transforms.Compose(
            [
                transforms.ToPILImage(),
                transforms.Resize(image_size),
                transforms.ToTensor(),
                transforms.Lambda(lambda x: x.mul(255)),
            ]
        )

    # Convert image to tensor
    tensor = itot_t(img)

    # Add the batch_size dimension
    tensor = tensor.unsqueeze(dim=0)
    return tensor


# Preprocessing ~ Tensor to Image
def ttoi(tensor):
    # Remove the batch_size dimension
    tensor = tensor.squeeze()
    # img = ttoi_t(tensor)
    img = tensor.cpu().numpy()

    # Transpose from [C, H, W] -> [H, W, C]
    img = img.transpose(1, 2, 0)
    return img
