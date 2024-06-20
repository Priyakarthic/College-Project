from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configure OpenAI API
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data['prompt']

        # Generate text
        text_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50
        )

        # Generate image
        image_response = openai.Image.create(
            prompt=prompt,
            max_tokens=50
        )

        return jsonify({
            'text': text_response.choices[0].text.strip(),
            'image': image_response.url
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)