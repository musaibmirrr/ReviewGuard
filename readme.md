ReviewGuard: AI-Driven Fake Review Detection System

#Overview
ReviewGuard is an intelligent Fake Review Detection System designed to maintain the integrity of user reviews on e-commerce platforms. Built using Django, MongoDB, and TextBlob, the system employs Sentiment Analysis to filter out potentially fraudulent reviews, ensuring that only authentic, verified reviews from genuine customers are displayed. This solution improves user trust and enhances the overall shopping experience.
The project features a user-friendly shop interface for customers and a powerful admin panel for managing products, orders, and reviews. ReviewGuard distinguishes between ordinary and verified users, ensuring accurate and trustworthy reviews, and provides session persistence across admin and shop interfaces.

#Key Features
AI-Powered Fake Review Detection: Detect and remove suspicious reviews using TextBlob sentiment analysis.
Admin Dashboard: Manage users, products, orders, and reviews through a secure, easy-to-use admin interface.
Verified Buyer Reviews: Only customers who have purchased a product can leave a review, with a "Verified" badge attached.
Seamless Session Handling: Shop users and admin users can switch between roles without disrupting session data.
Product and Review Management: Admins can add, update, and delete products, while customers can browse products and leave reviews.

#Tech Stack
Backend: Django (Python 3.12+)
Frontend: HTML5, CSS3, JavaScript, Bootstrap
Database: MongoDB (via Djongo)
Machine Learning: TextBlob for Sentiment Analysis
Session Management: Django Sessions with custom session handling for user and admin roles

#How It Works

For Users:
Shop and Purchase: Users can browse products and complete purchases.
Review System: Verified buyers can leave reviews on purchased products, they will be given a badge to verify that a user has purchased the product before submiting a review. Those users who have not purchased the product, there review will go sentiment analysis and based on that result our system decided whether its too much positive or negative and hence not display those reviews.
Seamless Sessions: If a user switches to the admin interface after logging in as a shop user, the session persists, allowing them to return to the shop without re-login.

For Admins:
Product Management: Admins can add, edit, and remove products from the database.
Review Analysis: Admins can review user feedback and approve or delete fake reviews flagged by the system.
User and Order Management: Track users, view orders, and manage the e-commerce platform through the admin interface.

#IP Approach
Our system can fetch the ip of the user even though proxies are used, and if the count exeeds 3, he/she cannot make a review anymore.

#Installation Instructions

Create a virtual environment:
python -m venv venv

Activate virtual environment:
#on Mac source venv/bin/activate   # On Windows: venv\Scripts\activate

Install required dependencies:
pip install -r requirements.txt

#conclusion
ReviewGuard has integrated sentiment analysis and ip approach to maximize the detection for fake reviews and hence providing a way to ensure integrity and credibility for the system.

