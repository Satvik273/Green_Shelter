from datetime import datetime

sample_products = [
    {
        "name": "Cow Dung Bricks",
        "description": "Lightweight, thermally insulating, and naturally antibacterial bricks made from processed cow dung.",
        "price": 15,
        "image": "images/gallery/cow-dung/natural_plaster.jpg",
        "category": "construction",
        "features": "Thermal Insulation,Antibacterial,Lightweight",
        "unit": "per brick"
    },
    {
        "name": "Bamboo Composite Materials",
        "description": "High-strength composite materials made from engineered bamboo for versatile construction applications.",
        "price": 950,
        "image": "images/gallery/bamboo/bamboo_framework.jpg",
        "category": "bamboo",
        "features": "High Strength,Renewable,Versatile",
        "unit": "per panel"
    },
    {
        "name": "Structural Reed Panels",
        "description": "Eco-friendly panels made from compressed reed, suitable for walls and insulation in green buildings.",
        "price": 450,
        "image": "images/products/reed_panels.jpg", # NOTE: Add this image to static/images/products/
        "category": "construction",
        "features": "Eco-Friendly,Insulating,Sustainable",
        "unit": "per panel"
    },
]

sample_posts = [
    {
        "title": "The Green Future of India Isn't from Abroad",
        "content": "<p>A hard truth for our LinkedIn feeds: Those impressive green building innovation technologies from other countries? They are often not scalable or cost-effective for India. We're celebrating technologies that simply will not work here in our country or may take decades to be implemented.</p>"
                "<p><strong>The real revolution is happening in our own backyard.</strong></p>"
                "<p>Engineers at IIT Delhi are pioneering incredible, carbon-negative seismic resistant building techniques using our country's most abundant locally available bio-materials as Construction raw materials: <strong>cow dung, sarkanda, and bamboo</strong>.</p>"
                "<p>These are not just green ideas; they are practical, affordable solutions made for India, by India. It is time we champion our own homegrown genius and elevate these innovations to the global Centre stage.</p>",
        "image": "images/blogs/blog1/image1.jpg",
        "excerpt": "Discover how homegrown innovation is shaping the future of sustainable construction in India."
    },
    {
        "title": "Construction Waste: From Dream Home to Nightmare",
        "content": (
            "<p>India's construction boom is building our future, but it's also piling up a silent threat. "
            "Annually, our nation generates an estimated 150-500 <em>million tonnes</em> of Construction & Demolition (C&D) waste, "
            "with alarming daily figures like Delhi's 5,500-6,000 tonnes. The stark reality? Only a fraction of this colossal waste is ever recycled. 🏗️➡️ landfill!</p>"
            "<p>This isn't just a distant problem; it's a direct threat returning to impact our lives. Unchecked C&D waste fuels:</p>"
            "<ul>"
            "<li><strong>Environmental & Health Hazards:</strong> Unleashing toxic dust and fumes into our air 💨, contaminating our vital land and water 💧, and exacerbating urban flooding – all directly impacting public health. 😷</li>"
            "<li><strong>Resource Depletion:</strong> Driving unsustainable extraction of virgin materials, eroding our natural reserves and ecological balance. 🌳📉</li>"
            "<li><strong>Climate Impact:</strong> Significantly increasing greenhouse gas emissions, accelerating climate change that threatens our very existence. 🌡️🌍</li>"
            "</ul>"
            "<h3>The Urgent Solution: Build Green, Live Safe! 🌱🏡</h3>"
            "<p>We must redefine how we build. The answer lies in embracing <em>biodegradable, locally available green construction materials</em>. "
            "Imagine homes built with innovative alternatives that drastically cut waste, minimize carbon footprints, and actively contribute to a healthier environment.</p>"
            "<p>By prioritizing circular economy practices ♻️, enforcing robust recycling mandates, and incentivizing green building innovation, "
            "we can transform this looming crisis into a cornerstone for a healthier, more sustainable India. It's time to build not just homes, but a safer future for all. ✨</p>"
            "<hr><p><em><strong>Trivia:</strong> A 100 sq.yard house generates 3.4 Tonnes - 5.5 Tonnes of Construction Waste during its construction and 10 Tonnes - 20 Tonnes of Demolition Waste when it is demolished. "
            "Think, how much you are responsible in doing so?</em></p>"
        ),
        "image": "images/blogs/blog2/constructionwaste.jpg",
        "excerpt": "The hidden environmental cost of construction and how green materials offer a solution."
    }
]

sample_reviews = [
    {"name": "Alice Brown", "rating": 5, "comment": "Amazing products! The quality is outstanding.", "avatar": "images/avatars/avatar1.jpg"},
    {"name": "Bob Wilson", "rating": 4, "comment": "Great sustainable options. Will definitely order again.", "avatar": "images/avatars/avatar2.jpg"}
]

sample_projects = [
    {"name": "Eco-Friendly Home in the Hills", "description": "A residential project using bamboo framework and natural plaster, designed for minimal environmental impact.", "image": "images/projects/project1.jpg"},
    {"name": "Sustainable Community Center", "description": "A community building constructed with locally sourced materials, promoting green architecture.", "image": "images/projects/project2.jpg"},
    {"name": "Green Resort Cottages", "description": "A series of eco-resort cottages built with our signature bamboo framework and cow-dung plaster.", "image": "images/projects/project3.jpg"}
]

sample_team = [
    {
        "name": "Vaishali Bansal",
        "position": "Co-Founder and CEO",
        "bio": "My 15-year career in Power, Oil & Gas, Refinery, Chemical, and Mining industries has now evolved into a personal mission. Rooted in my NIT Kurukshetra and IIT Delhi education, I'm now fusing engineering and ecology to build green, breathing shelters and lead the way to a carbon-negative future.",
        "image": "images/team/member1.jpg",
        "linkedin_url": "https://www.linkedin.com/in/vaishali-bansal-5270b673/",
    },
    {
        "name": "Prof. Suresh Bhalla",
        "position": "Co-Founder and Chief Technology Mentor",
        "bio": "Renowned IIT Delhi Professor and a top 2% world scientist, Prof. Bhalla is the founding President of the Indian Structural Health Monitoring Society. His expertise in SHM and patented technologies are vital to our mission.",
        "image": "images/team/member2.jpg",
        "linkedin_url": "https://www.linkedin.com/in/sbhallaiitd/"
    }
]

sample_gallery_images = [
    {"path": "images/gallery/construction/finished.jpg", "title": "Finished Project", "category": "Construction"},
    {"path": "images/gallery/cow-dung/natural_plaster.jpg", "title": "Cow Dung Brick", "category": "Cow-Dung"},
    {"path": "images/gallery/construction/Picture1.png", "title": "Bamboo Prototype", "category": "Bamboo"},
    {"path": "images/gallery/construction/Picture2.png", "title": "Prototype", "category": "Construction"},
    {"path": "images/gallery/construction/Picture3.png", "title": "Cow Dung Brick Prototype", "category": "Construction"},
    {"path": "images/gallery/construction/Picture4.png", "title": "Bamboo Prototype", "category": "Bamboo"},
    {"path": "images/gallery/construction/Picture5.png", "title": "Prototype", "category": "Construction"},
    {"path": "images/gallery/construction/Picture6.png", "title": "Cow Dung Brick Prototype", "category": "Construction"},
]

sample_faqs = [
    {"question": "Is this technology fire resistance proof?", "answer": "Yes, Our technology provides better fire resistance than conventional RCC construction after treatment."},
    {"question": "Are the structures made from this technology earthquake resistant?", "answer": "Yes, the technology is earthquake resistant."},
    {"question": "How much more expensive is this technology construction as compared to conventional RCC Construction?", "answer": "This technology shall be more pocket friendly as compared to  conventional RCC Construction."},
    {"question": "How many storeys can be built using this technology?", "answer": "You can make good G+2 house using this technology."},
    {"question": "Are the cowdung bricks prone to easy damage?", "answer": "No, the cowdung bricks are as good as red bricks and provide better fire resistance and water resistance."},
    {"question": "Are these structures sufficiently thermally resistant w.r.t outside temperature?", "answer": "The natural bio-materials used in our technology provide natural thermal resistance to your homes with a temperature difference of around 7-11 Degrees Celsius. That also means lesser use of air conditioners in summers and heaters in winters."},
]

sample_services = [
    {"name": "Sustainable Seismic Resistant Construction", "description": "Consultancy for designing and implementing construction technology that is both eco-friendly and resilient to seismic events.", "icon": "fas fa-hard-hat"},
    {"name": "Structural Health Monitoring (SHM)", "description": "Expert guidance on implementing SHM systems to ensure the long-term safety and integrity of your structures.", "icon": "fas fa-heartbeat"},
    {"name": "Structural Design", "description": "Comprehensive structural design services focusing on the use of natural and sustainable materials.", "icon": "fas fa-ruler-combined"}
]

sample_awards = [
    {"title": "Sustainable Business Award 2024", "organization": "Green Business Council", "description": "Recognized for exceptional commitment to sustainable practices in bamboo cultivation.", "year": "2024"},
    {"title": "Innovation in Natural Building", "organization": "Green Building Institute", "description": "Award for pioneering natural building technologies with bamboo and cow dung.", "year": "2023"},
    {"title": "Community Impact Award", "organization": "Local Chamber of Commerce", "description": "Honored for creating sustainable employment opportunities in the community.", "year": "2023"}
]

sample_media = [
    {
        "title": "Eco-friendly homes using bamboo and cow dung: IIT Delhi's innovative approach",
        "source": "Live Hindustan",
        "url": "https://www.livehindustan.com/ncr/new-delhi/story-eco-friendly-homes-using-bamboo-and-cow-dung-iit-delhi-s-innovative-approach-201744370302472.amp.html",
        "description": "An article from Live Hindustan detailing the innovative and sustainable construction methods being developed at IIT Delhi."
    }
]

sample_endorsements = [
    {"name": "IIT Delhi", "logo": "images/endorsements/iit_delhi_logo.png", "url": "https://home.iitd.ac.in/"},
    {"name": "Department of Science and Technology", "logo": "images/endorsements/dst_logo.png", "url": "https://dst.gov.in/"},
    {"name": "Startup India", "logo": "images/endorsements/startup_india_logo.png", "url": "https://www.startupindia.gov.in/"}
]

sample_achievements = [
    {"title": "Indian Patent Application", "description": "Application No. 202211056213", "icon": "fas fa-award"},
    {
        "title": "Alignment with UN Sustainable Development Goals",
        "description": "Prof. Suresh Bhalla's research on Fibre Reinforced Bamboo Composite (FRBC) is linked to UN Sustainable Development Goals (SDGs), highlighting the global relevance of our carbon-negative construction research.",
        "icon": "fas fa-globe-americas"
    }
]