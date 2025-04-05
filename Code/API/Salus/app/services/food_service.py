from google import genai

model = genai.Client(api_key="AIzaSyCFjH9sPw5IKRMdNjRuxb3p_qYiEoWium8")


def get_food_name_from_image(image):
    response = model.models.generate_content(
        contents=[
            'Món ăn trong hình ảnh là gì?',
            image,
            'Nhận diện món ăn theo tiếng Việt có dấu.',
            'Theo mẫu này: <Tên món ăn>'
        ],
        model="gemini-2.0-flash"
    )
    return response.text
