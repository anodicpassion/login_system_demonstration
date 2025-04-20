from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
usr_name = ""
story = ["Once upon a time, there were three little pigs who lived with their mother. The time came for them to leave "
         "and build their own homes. The first little pig was lazy and decided to build his house out of straw, "
         "thinking it would be quick and easy. The second little pig was a bit more diligent and chose to build his "
         "house with sticks, which took a little more effort. The third little pig was wise and hardworking, "
         "so he built his house with bricks, which took a lot of time and effort. Soon after, a big bad wolf came "
         "along and saw the first little pig's straw house. He huffed and puffed and blew the house down easily. The "
         "first little pig ran to his brother's house made of sticks. But the wolf was determined and huffed and "
         "puffed again, blowing the stick house down as well. The two little pigs then sought refuge in the third "
         "little pig's brick house. When the wolf arrived at the brick house, he tried to blow it down but couldn't. "
         "The third little pig had built a strong and sturdy house. Frustrated, the wolf tried various tactics to get "
         "inside, but the pig outsmarted him at every turn. The wolf eventually gave up and went away, unable to harm "
         "the three little pigs. The three little pigs learned that hard work, diligence, and making the right "
         "choices pay off. They lived happily ever after in their safe and secure brick house, knowing that they had "
         "overcome the big bad wolf.",
         "Once upon a time, there was a speedy hare who loved boasting about his lightning-fast speed. He would often "
         "mock the slow and steady turtle, making fun of his sluggish pace. The turtle, however, remained calm and "
         "took the hare's taunts with a grain of salt.One day, the hare challenged the turtle to a race, believing he "
         "would win effortlessly. The turtle, accepting the challenge, suggested a route that was long but "
         "straightforward. The hare eagerly agreed, confident that victory was guaranteed.On the day of the race, "
         "a crowd gathered to witness the much-anticipated contest. As the race started, the hare bolted ahead, "
         "leaving the turtle far behind. Overwhelmed by his own speed, the hare grew arrogant and decided to take a "
         "nap under a shady tree, thinking he had plenty of time to spare.Meanwhile, the persistent turtle continued "
         "plodding along, determined to give his best despite being slow. While the hare dozed off, the turtle slowly "
         "but steadily progressed along the racecourse, never losing sight of the finish line.When the hare woke up "
         "from his nap, he was startled to find the turtle closing in on the finish line. Realizing his careless "
         "mistake, the hare sprinted as fast as he could, but it was too late. The turtle had crossed the finish "
         "line, winning the race.The crowd erupted into cheers, amazed by the turtle's perseverance and consistency. "
         "The hare, humbled and embarrassed, admitted his foolishness and congratulated the turtle on his victory. "
         "From that day forward, the hare learned the importance of humility and respecting others, while the turtle "
         "proved that slow and steady progress can lead to success. The turtle and the hare became friends, "
         "each valuing the unique qualities of the other. They often teamed up, combining the turtle's patience and "
         "the hare's swiftness to accomplish various tasks together. Their unlikely friendship served as a reminder "
         "that everyone has their strengths, and by working together, they can achieve great things.",
         "Once upon a time, there was a sweet little girl named Little Red Riding Hood. She earned her name because "
         "she always wore a beautiful red hooded cape that her grandmother had made for her. One day, Little Red "
         "Riding Hood's mother asked her to visit her sick grandmother, who lived deep in the forest.Little Red "
         "Riding Hood happily agreed and set off on her journey with a basket of freshly baked goodies for her "
         "grandmother. Her mother warned her to stay on the path and not to talk to strangers. Little Red Riding Hood "
         "promised to be careful and skipped along the winding path through the woods.As she strolled through the "
         "forest, enjoying the sounds of nature, Little Red Riding Hood encountered a sly wolf. The wolf, "
         "knowing about her grandmother, came up with a mischievous plan. He pretended to be friendly and asked her "
         "where she was going.In her innocence, Little Red Riding Hood trusted the wolf and told him about her sick "
         "grandmother. The cunning wolf suggested that she take a detour to pick some flowers for her grandmother, "
         "while he hurriedly went to the grandmother's house to get there before her.Unaware of the wolf's true "
         "intentions, Little Red Riding Hood happily veered off the path to gather flowers.",
         "Once upon a time, in a peaceful pond, there lived a contented little frog and a proud bull. The frog was "
         "humble and enjoyed his simple life, while the bull boasted about his strength and size.One day, a terrible "
         "drought struck the land, causing the pond to dry up. The frog, worried about their survival, hopped around "
         "in search of a solution. He came across a nearby well filled with water. The frog excitedly told the bull "
         "about the well and suggested they move there to survive the drought.The bull, arrogant and dismissive, "
         "scoffed at the idea. He believed his size and strength would overcome any challenge. Ignoring the frog's "
         "advice, he decided to stay in the parched pond, convinced that rain would come soon.As days passed, "
         "the frog thrived in the well, enjoying the plentiful water and sustenance it provided. The bull, "
         "on the other hand, grew weaker and thinner with each passing day, deprived of water and food.Finally "
         "realizing his mistake, the bull approached the frog, humbled and desperate for help. He acknowledged the "
         "frog's wisdom and asked for assistance in reaching the well. The frog, compassionate and forgiving, "
         "agreed to help.With the frog's guidance, the bull managed to reach the well. He drank the water eagerly, "
         "rejuvenating his strength and vitality. The bull felt a deep sense of gratitude toward the frog, "
         "realizing the value of humility and listening to others.From that day forward, the bull and the frog became "
         "steadfast friends. They shared the water from the well, looking out for one another. The bull learned to "
         "appreciate the frog's wisdom and kindness, while the frog admired the bull's newfound humility.Together, "
         "they faced the challenges of the drought, supporting each other and finding strength in their friendship. "
         "Their story spread throughout the animal kingdom, teaching others the importance of humility, cooperation, "
         "and the wisdom of listening to those who may know better.And so, the bull and the frog lived harmoniously, "
         "their bond a testament to the power of humility and the strength found in unity."]


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return render_template("dashboard.html", usr_name= username, story=story[random.randint(0, 3)])
        else:
            error = 'Invalid username or password.'
            return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            error = 'Username already exists.'
            return render_template('register.html', error=error)

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
