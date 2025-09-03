from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, make_response, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from datetime import datetime
from slugify import slugify
import os
import time

# Import seed data from the new file
from seed_data import (sample_products, sample_posts, sample_reviews, sample_projects,
                       sample_team, sample_gallery_images, sample_faqs, sample_services,
                       sample_awards, sample_media, sample_endorsements, sample_achievements)

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# --- App Configuration ---
# Use the DATABASE_URL environment variable if it's set (for production on Railway)
# Otherwise, fall back to the local SQLite database for development.
database_url = os.environ.get('DATABASE_URL')

# Add a check for common placeholder values to avoid confusion during development.
if database_url and 'your-production-database-url' in database_url:
    print("\n\033[91mERROR: DATABASE_URL is set to a placeholder value.\033[0m")
    print("For local development, please unset it by running: \033[93m`unset DATABASE_URL`\033[0m")
    print("For production, set it to your actual database connection string.\n")
    exit(1) # Exit with an error code to prevent the app from continuing.

# Add a check for a literal ':port' which causes a ValueError.
if database_url and ':port' in database_url:
    print("\n\033[91mERROR: DATABASE_URL contains an invalid ':port' placeholder.\033[0m")
    print("The port must be a number, not a literal string.")
    print("For local development, please unset the variable: \033[93m`unset DATABASE_URL`\033[0m\n")
    exit(1)

if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url or \
    'sqlite:///' + os.path.join(basedir, 'products.db')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a-default-secret-key-for-development')

# --- Mail Configuration ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_RECIPIENT'] = os.environ.get('MAIL_RECIPIENT', 'ikstech.vaishali@gmail.com')

db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    slug = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    features = db.Column(db.String(200), nullable=True)
    unit = db.Column(db.String(50), nullable=True)

# Blog model
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    slug = db.Column(db.String(220), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    excerpt = db.Column(db.String(300), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    avatar = db.Column(db.String(200), nullable=False, default='images/avatars/default.jpg')

# Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=True, default="#")

# Team Member model
class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    linkedin_url = db.Column(db.String(200), nullable=True)
    twitter_url = db.Column(db.String(200), nullable=True)

# Gallery Image model
class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)

# FAQ model
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.Text, nullable=False)

# Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(100), nullable=False) # e.g., 'fas fa-hard-hat'

# --- New Models for Static Content ---

class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    organization = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.String(4), nullable=False)

class MediaItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Endorsement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), nullable=False)

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(100), nullable=False)


@app.context_processor
def inject_global_vars():
    """Injects global variables into all templates."""
    return dict(
        cache_buster=int(time.time()),
        request=request,
        # Provide a default image for Open Graph tags
        default_og_image=url_for('static', filename='images/logo.png', _external=True)
    )

@app.route("/")
def home():
    title = "GauBaanSa - Sustainable Green Homes with Bamboo & Cow Dung"
    description = "Discover GauBaanSa, an IIT Delhi initiative for sustainable housing. We build carbon-negative, earthquake-safe homes using innovative bamboo and cow dung brick technology."
    return render_template("home.html", title=title, meta_description=description)

@app.route("/about")
def about():
    team_members = TeamMember.query.order_by(TeamMember.id).all()
    title = "About GauBaanSa | Our Mission for Green Construction"
    description = "Meet the team behind GauBaanSa, co-founded by an IIT Delhi professor. Learn about our mission to revolutionize the construction industry with eco-friendly materials."
    return render_template("about.html", title=title, team_members=team_members, meta_description=description)

@app.route("/projects")
def projects_page():
    projects = Project.query.order_by(Project.id).all()
    title = "Our Projects | Sustainable Construction by GauBaanSa"
    description = "Explore our portfolio of green construction projects, showcasing homes and structures built with our innovative bamboo and cow dung materials."
    return render_template("projects.html", title=title, projects=projects, meta_description=description)

@app.route("/products")
def products():
    all_products = Product.query.all()
    all_services = Service.query.order_by(Service.id).all()
    title = "Products & Services | Green Building Materials & Consultancy"
    description = "Browse our sustainable products like cow dung bricks and bamboo composites, and learn about our services including structural design and health monitoring."
    return render_template("products.html", title=title, products=all_products, services=all_services, meta_description=description)

@app.route("/services")
def services():
    # This route renders the same template as products, which includes the services section.
    all_products = Product.query.all()
    all_services = Service.query.order_by(Service.id).all()
    title = "Our Services | Green Construction & Structural Design"
    description = "GauBaanSa offers expert consultancy in sustainable seismic-resistant construction, structural health monitoring (SHM), and green structural design."
    return render_template("products.html", title=title, products=all_products, services=all_services, meta_description=description)

@app.route("/product/<slug>")
def product_detail(slug):
    product = Product.query.filter_by(slug=slug).first_or_404()
    return render_template("product_detail.html", title=product.name, product=product)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    title = "Contact GauBaanSa | Get in Touch"
    description = "Contact GauBaanSa for inquiries about our sustainable construction products, services, or projects. Reach out to our team for collaborations and information."

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        phone = request.form.get('phone')

        # Basic validation
        if not all([name, email, message]):
            flash('Please fill out all required fields.', 'danger')
            return render_template("contact.html", title=title, meta_description=description)

        try:
            msg = Message(
                subject=f"New Contact Form Submission from {name}",
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[app.config['MAIL_RECIPIENT']]
            )
            msg.body = f"""
            You have received a new message from your website's contact form.

            Name: {name}
            Email: {email}
            Phone: {phone or 'Not provided'}

            Message:
            {message}
            """
            mail.send(msg)
            flash('Thank you for your message! We will get back to you soon.', 'success')
        except Exception as e:
            print(f"Email sending failed: {e}") # For debugging on the server
            flash('Sorry, there was an error sending your message. Please try again later.', 'danger')

        return redirect(url_for('contact'))
    return render_template("contact.html", title=title, meta_description=description)

@app.route("/blog")
def blog():
    posts = Blog.query.order_by(Blog.date_posted.desc()).all()
    title = "GauBaanSa Blog | Insights on Sustainable Construction"
    description = "Read the latest articles and insights from the GauBaanSa team on green building technology, sustainable materials, and the future of construction in India."
    return render_template("blog.html", title=title, posts=posts, meta_description=description)

@app.route("/blog/<slug>")
def blog_post(slug):
    post = Blog.query.filter_by(slug=slug).first_or_404()
    return render_template("blog_post.html", title=post.title, post=post)

@app.route("/gallery")
def gallery():
    gallery_images = GalleryImage.query.order_by(GalleryImage.id).all()
    title = "Gallery | See Our Sustainable Projects"
    description = "View our gallery of images showcasing the beauty and versatility of our bamboo and cow dung construction projects and materials."
    return render_template("gallery.html", title=title, gallery_images=gallery_images, meta_description=description)

@app.route("/faq")
def faq():
    faqs = FAQ.query.order_by(FAQ.id).all()
    title = "Frequently Asked Questions (FAQ) | GauBaanSa"
    description = "Find answers to common questions about our green construction technology, including fire resistance, earthquake safety, cost, and material durability."
    return render_template("faq.html", title=title, faqs=faqs, meta_description=description)

@app.route("/reviews")
def reviews():
    all_reviews = Review.query.order_by(Review.date_posted.desc()).all()
    title = "Testimonials | What Our Clients Say"
    description = "Read testimonials and reviews from clients who have chosen GauBaanSa for their sustainable building projects."
    return render_template("reviews.html", title=title, reviews=all_reviews, meta_description=description)

@app.route("/awards")
def awards():
    all_awards = Award.query.order_by(Award.year.desc(), Award.id).all()
    title = "Awards & Recognition | GauBaanSa"
    description = "See the awards and recognition our team and technology have received for innovation in sustainable business and natural building."
    return render_template("awards.html", title=title, awards=all_awards, meta_description=description)

@app.route("/media")
def media():
    media_items = MediaItem.query.order_by(MediaItem.id).all()
    return render_template("media.html", title="Media Center", media_items=media_items)

@app.route("/why-natural")
def why_natural():
    benefits = {
        "bamboo": [
            "Rapid growth and renewability",
            "High tensile strength",
            "Natural pest resistance",
            "Carbon sequestration",
            "Soil conservation"
        ],
        "cow_dung": [
            "Natural binding properties",
            "Thermal insulation",
            "Anti-bacterial properties",
            "Zero carbon footprint",
            "Local resource utilization"
        ]
    }
    title = "Why Natural Materials? | The Benefits of Bamboo & Cow Dung"
    description = "Learn why natural, locally-sourced materials like bamboo and cow dung are superior choices for sustainable, healthy, and resilient buildings."
    return render_template("why_natural.html", title=title, benefits=benefits, meta_description=description)

@app.route("/impact")
def impact():
    title = "Our Impact | Environmental & Social Contributions"
    description = "Discover how GauBaanSa is making a positive environmental and social impact through carbon-negative construction and promoting a circular economy."
    return render_template("impact.html", title=title, meta_description=description)

@app.route("/endorsements")
def endorsements():
    endorsements_list = Endorsement.query.order_by(Endorsement.id).all()
    achievements_list = Achievement.query.order_by(Achievement.id).all()
    return render_template("endorsements.html", title="Endorsements & Achievements | GauBaanSa", endorsements=endorsements_list, achievements=achievements_list)

@app.cli.command("init-db")
def init_db_command():
    """Creates the database tables and seeds them with initial data."""
    db.create_all()
    print("Initialized the database.")

    # Check if database is already seeded to prevent duplicates
    if Product.query.first() and Award.query.first():
        print("Database already appears to be seeded. Skipping.")
        return

    print("Seeding database with initial data...")
    
    for p_data in sample_products:
        p_data['slug'] = slugify(p_data['name'])
        db.session.add(Product(**p_data))

    for p_data in sample_posts:
        p_data['slug'] = slugify(p_data['title'])
        db.session.add(Blog(**p_data))

    db.session.add_all([Review(**p) for p in sample_reviews])
    db.session.add_all([Project(**p) for p in sample_projects])
    db.session.add_all([TeamMember(**p) for p in sample_team])
    db.session.add_all([GalleryImage(**p) for p in sample_gallery_images])
    db.session.add_all([FAQ(**p) for p in sample_faqs])
    db.session.add_all([Service(**p) for p in sample_services])
    db.session.add_all([Award(**p) for p in sample_awards])
    db.session.add_all([MediaItem(**p) for p in sample_media])
    db.session.add_all([Endorsement(**p) for p in sample_endorsements])
    db.session.add_all([Achievement(**p) for p in sample_achievements])

    db.session.commit()
    print("Database seeded successfully.")

@app.route("/subscribe", methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'success': False, 'message': 'An email address is required.'}), 400

    # In a real application, you would save this email to a database table
    # or a third-party mailing list service. For now, we'll just print it.
    print(f"New newsletter subscription from: {email}")

    return jsonify({'success': True, 'message': 'Thank you for subscribing!'})

@app.route('/robots.txt')
def robots_txt():
    """Serves the robots.txt file."""
    sitemap_url = url_for('sitemap', _external=True)
    txt = f"User-agent: *\nAllow: /\n\nSitemap: {sitemap_url}"
    response = Response(txt, mimetype='text/plain')
    return response

@app.route('/sitemap.xml')
def sitemap():
    """Generate sitemap.xml for search engines."""
    pages = []

    # List of static page endpoints
    endpoints = [
        'home', 'about', 'projects_page', 'products', 'services', 'contact',
        'blog', 'gallery', 'faq', 'reviews', 'awards', 'media',
        'why_natural', 'impact', 'endorsements'
    ]
    for endpoint in endpoints:
        pages.append(url_for(endpoint, _external=True))

    # Dynamic routes for products
    for product in Product.query.all():
        pages.append(url_for('product_detail', slug=product.slug, _external=True))

    # Dynamic routes for blog posts
    for post in Blog.query.all():
        pages.append(url_for('blog_post', slug=post.slug, _external=True))

    xml_sitemap = render_template('sitemap_template.xml', pages=pages)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response

if __name__ == "__main__":
    # For local development, use the PORT environment variable if available, otherwise default to 5001.
    # This makes it flexible for different development environments.
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)