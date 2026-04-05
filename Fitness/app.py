from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "fitpulse_secret_key"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/workouts')
def workouts():
    workout_plans = [
        {
            "title": "Beginner Full Body",
            "duration": "30 Minutes",
            "level": "Beginner",
            "description": "A simple full-body workout for beginners with light exercises and stretching."
        },
        {
            "title": "Fat Burn Cardio",
            "duration": "25 Minutes",
            "level": "Intermediate",
            "description": "A cardio-focused plan including jumping jacks, high knees, and mountain climbers."
        },
        {
            "title": "Strength Builder",
            "duration": "40 Minutes",
            "level": "Advanced",
            "description": "A workout plan designed to improve strength using bodyweight and resistance exercises."
        }
    ]
    return render_template('workouts.html', workout_plans=workout_plans)


@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi_value = None
    category = None

    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height_cm = float(request.form['height'])
            height_m = height_cm / 100

            bmi_value = round(weight / (height_m ** 2), 2)

            if bmi_value < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi_value < 25:
                category = "Normal weight"
            elif 25 <= bmi_value < 30:
                category = "Overweight"
            else:
                category = "Obese"

        except ValueError:
            flash("Please enter valid numbers.", "error")

    return render_template('bmi.html', bmi_value=bmi_value, category=category)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        flash(f"Thank you, {name}! Your message has been received.", "success")

    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)