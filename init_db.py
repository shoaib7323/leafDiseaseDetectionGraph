
import mysql.connector
import sys

def init_db():
    print("Connecting to MySQL...")
    # Connect to MySQL server (no database selected yet) to create DB
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            charset='utf8mb4',
            use_unicode=True
        )
        cursor = conn.cursor()
        
        print("Creating database...")
        cursor.execute("DROP DATABASE IF EXISTS plant_disease_db")
        cursor.execute("CREATE DATABASE plant_disease_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        cursor.execute("USE plant_disease_db")
        
        print("Creating table...")
        cursor.execute("""
            CREATE TABLE treatments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                disease_key VARCHAR(255) NOT NULL UNIQUE,
                basic_description_en TEXT,
                basic_description_bn TEXT,
                treatment_immediate_en TEXT,
                treatment_immediate_bn TEXT,
                treatment_chemical_en TEXT,
                treatment_chemical_bn TEXT,
                treatment_organic_en TEXT,
                treatment_organic_bn TEXT,
                treatment_prevention_en TEXT,
                treatment_prevention_bn TEXT
            ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
        """)

        print("Creating knowledge_base table...")
        cursor.execute("""
            CREATE TABLE knowledge_base (
                id INT AUTO_INCREMENT PRIMARY KEY,
                category VARCHAR(50) NOT NULL,
                title_en VARCHAR(255),
                title_bn VARCHAR(255),
                short_desc_en TEXT,
                short_desc_bn TEXT,
                content_en TEXT,
                content_bn TEXT,
                image_url VARCHAR(255)
            ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
        """)
        
        print("Inserting data...")
        # Data to insert
        data = [
            ('Potato___Early_blight', 
             'Fungal infection causing dark spots on older leaves.', 'ছত্রাকজনিত সংক্রমণ যা পুরোনো পাতায় কালো দাগ সৃষ্টি করে।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply copper-based fungicide every 7-10 days.', 'প্রতি ৭-১০ দিনে কপার-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন।',
             'Use neem oil spray or baking soda solution', 'নিম তেল স্প্রে বা বেকিং সোডা দ্রবণ ব্যবহার করুন',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Potato___Late_blight', 
             'Serious fungal disease causing rapid decay.', 'মারাত্মক ছত্রাকজনিত রোগ যা দ্রুত পচন ঘটায়।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply copper-based fungicide every 7-10 days.', 'প্রতি ৭-১০ দিনে কপার-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন।',
             'Use neem oil spray or baking soda solution', 'নিম তেল স্প্রে বা বেকিং সোডা দ্রবণ ব্যবহার করুন',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Potato___healthy', 
             'Plant looks healthy.', 'গাছটি সুস্থ দেখাচ্ছে।',
             'Keep monitoring regularly.', 'নিয়মিত পর্যবেক্ষণ করুন।',
             'Not applicable.', 'প্রযোজ্য নয়।',
             'Maintain good care.', 'ভাল যত্ন বজায় রাখুন।',
             'Keep doing what you are doing.', 'আপনি যা করছেন তা চালিয়ে যান।'),

            ('Tomato___Bacterial_spot', 
             'Bacterial infection causing small dark spots.', 'ব্যাকটেরিয়া সংক্রমণ যা ছোট কালো দাগ সৃষ্টি করে।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply copper-based fungicide every 7-10 days.', 'প্রতি ৭-১০ দিনে কপার-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন।',
             'Use neem oil spray or baking soda solution', 'নিম তেল স্প্রে বা বেকিং সোডা দ্রবণ ব্যবহার করুন',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Tomato___Early_blight', 
             'Fungal infection causing bullseye-pattern spots.', 'ছত্রাকজনিত সংক্রমণ যা ঘনীভূত বলয়ের মতো দাগ সৃষ্টি করে।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply copper-based fungicide every 7-10 days.', 'প্রতি ৭-১০ দিনে কপার-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন।',
             'Use neem oil spray or baking soda solution', 'নিম তেল স্প্রে বা বেকিং সোডা দ্রবণ ব্যবহার করুন',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Tomato___Late_blight', 
             'Water-soaked spots on leaves that turn brown.', 'পাতায় জলভেজা দাগ যা পরে বাদামি হয়ে যায়।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply copper-based fungicide every 7-10 days.', 'প্রতি ৭-১০ দিনে কপার-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন।',
             'Use neem oil spray or baking soda solution', 'নিম তেল স্প্রে বা বেকিং সোডা দ্রবণ ব্যবহার করুন',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Tomato___Leaf_Mold', 
             'Fungal diease causing pale green to yellow spots.', 'ছত্রাকজনিত রোগ যা ফ্যাকাশে সবুজ থেকে হলুদ দাগ সৃষ্টি করে।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply copper-based fungicide every 7-10 days.', 'প্রতি ৭-১০ দিনে কপার-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন।',
             'Use neem oil spray or baking soda solution', 'নিম তেল স্প্রে বা বেকিং সোডা দ্রবণ ব্যবহার করুন',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Tomato___Septoria_leaf_spot', 
             'Fungal disease causing circular spots with dark borders.', 'ছত্রাকজনিত রোগ যা কালো বর্ডারযুক্ত বৃত্তাকার দাগ সৃষ্টি করে।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply copper-based fungicide every 7-10 days.', 'প্রতি ৭-১০ দিনে কপার-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন।',
             'Use neem oil spray or baking soda solution', 'নিম তেল স্প্রে বা বেকিং সোডা দ্রবণ ব্যবহার করুন',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Tomato___Spider_mites Two-spotted_spider_mite', 
             'Tiny pests causing stippling on leaves.', 'ছোট পোকা যা পাতায় ছোট ছোট ছিদ্র সৃষ্টি করে।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply miticide or sulfur dust.', 'মাকড়নাশক বা সালফার ডাস্ট ব্যবহার করুন।',
             'Use neem oil spray.', 'নিম তেল স্প্রে ব্যবহার করুন।',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Tomato___Target_Spot', 
             'Fungal disease causing brown spots with concentric rings.', 'ছত্রাকজনিত রোগ যা ঘনীভূত বলয়যুক্ত বাদামি দাগ সৃষ্টি করে।',
             'Remove affected leaves and improve air circulation', 'আক্রান্ত পাতা সরান এবং বাতাস চলাচল বাড়ান',
             'Apply copper-based fungicide every 7-10 days.', 'প্রতি ৭-১০ দিনে কপার-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন।',
             'Use neem oil spray or baking soda solution', 'নিম তেল স্প্রে বা বেকিং সোডা দ্রবণ ব্যবহার করুন',
             'Ensure proper spacing and avoid overhead watering', 'যথাযথ দূরত্ব বজায় রাখুন এবং উপরের দিক থেকে পানি দেবেন না'),

            ('Tomato___Tomato_Yellow_Leaf_Curl_Virus', 
             'Viral disease causing leaf curling and yellowing.', 'ভাইরাসজনিত রোগ যা পাতা কোঁকড়ানো এবং হলুদ হওয়া সৃষ্টি করে।',
             'Remove affected plants immediately.', 'আক্রান্ত গাছটি অবিলম্বে সরিয়ে ফেলুন।',
             'Control whiteflies with insecticides.', 'কীটনাশক দিয়ে সাদামাছি নিয়ন্ত্রণ করুন।',
             'Use neem oil to repel whiteflies.', 'সাদামাছি তাড়াতে নিম তেল ব্যবহার করুন।',
             'Use virus-resistant varieties.', 'ভাইরাস-প্রতিরোধী জাত ব্যবহার করুন।'),

            ('Tomato___Tomato_mosaic_virus', 
             'Viral disease causing mottled leaves.', 'ভাইরাসজনিত রোগ যা পাতায় মোজাইক নকশা সৃষ্টি করে।',
             'Remove affected plants immediately.', 'আক্রান্ত গাছটি অবিলম্বে সরিয়ে ফেলুন।',
             'Clean tools with disinfectant.', 'সংক্রমণনাশক দিয়ে যন্ত্রপাতি পরিষ্কার করুন।',
             'Wash hands often when handling plants.', 'গাছ ধরার সময় ঘন ঘন হাত ধোন।',
             'Use virus-free seeds.', 'ভাইরাস-মুক্ত বীজ ব্যবহার করুন।'),

            ('Tomato___healthy', 
             'Plant looks healthy.', 'গাছটি সুস্থ দেখাচ্ছে।',
             'Keep monitoring regularly.', 'নিয়মিত পর্যবেক্ষণ করুন।',
             'Not applicable.', 'প্রযোজ্য নয়।',
             'Maintain good care.', 'ভাল যত্ন বজায় রাখুন।',
             'Keep doing what you are doing.', 'আপনি যা করছেন তা চালিয়ে যান।')
        ]
        
        sql = """INSERT INTO treatments (disease_key, 
                basic_description_en, basic_description_bn,
                treatment_immediate_en, treatment_immediate_bn,
                treatment_chemical_en, treatment_chemical_bn,
                treatment_organic_en, treatment_organic_bn,
                treatment_prevention_en, treatment_prevention_bn)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        cursor.executemany(sql, data)
        conn.commit()

        print("Inserting knowledge base data...")
        kb_data = [
            # Disease Encyclopedia
            ('disease_encyclopedia', 'Potato Early Blight', 'আলুর আর্লি ব্লাইট', 
             'Common fungal disease dealing with dark spots.', 'সাধারণ ছত্রাকজনিত রোগ যা কালো দাগ সৃষ্টি করে।',
             '<p><strong>Cause:</strong> Fungus Alternaria solani.</p><p><strong>Symptoms:</strong> Dark, concentric rings on older leaves.</p>',
             '<p><strong>কারণ:</strong> অল্টারনারিয়া সোলানি নামক ছত্রাক।</p><p><strong>লক্ষণ:</strong> পুরোনো পাতায় কালো, ঘনীভূত বলয়।</p>',
             '/static/img/disease_placeholder.svg'),
            
            ('disease_encyclopedia', 'Tomato Late Blight', 'টমেটো লেট ব্লাইট',
             'Serious fungal disease causing rapid decay.', 'মারাত্মক ছত্রাকজনিত রোগ যা দ্রুত পচন ঘটায়।',
             '<p><strong>Cause:</strong> Oomycete Phytophthora infestans.</p><p><strong>Symptoms:</strong> Water-soaked spots on leaves.</p>',
             '<p><strong>কারণ:</strong> ফাইটোফথোরা ইনফেস্টানস।</p><p><strong>লক্ষণ:</strong> পাতায় জলভেজা দাগ।</p>',
             '/static/img/disease_placeholder.svg'),

            # Care Guides
            ('care_guides', 'Tomato Care Guide', 'টমেটো পরিচর্যা নির্দেশিকা',
             'Basic guide for growing healthy tomatoes.', 'সুস্থ টমেটো ফলানোর প্রাথমিক গাইড।',
             '<p>Tomatoes need full sun (6-8 hours) and well-drained soil rich in organic matter. Water consistently to avoid blossom end rot.</p>',
             '<p>টমেটোর জন্য পূর্ণ রোদ (৬-৮ ঘণ্টা) এবং জৈব পদার্থ সমৃদ্ধ সুনিষ্কাশিত মাটি প্রয়োজন। ব্লোজম এন্ড রট এড়াতে নিয়মিত পানি দিন।</p>',
             '/static/img/care_placeholder.svg'),

            ('care_guides', 'Potato Planting Tips', 'আলু রোপণ টিপস',
             'Best practices for planting potatoes.', 'আলু রোপণের সর্বোত্তম পদ্ধতি।',
             '<p>Plant seed potatoes in early spring. Hill soil around stems as they grow to encourage tuber formation.</p>',
             '<p>বসন্তের শুরুতে বীজ আলু রোপণ করুন। কন্দ গঠন উৎসাহিত করতে গাছ বড় হওয়ার সাথে সাথে কান্ডের চারপাশে মাটি তুলে দিন।</p>',
             '/static/img/care_placeholder.svg'),

            # Seasonal Calendar
            ('seasonal_calendar', 'Spring Planting', 'বসন্তকালীন রোপণ',
             'What to plant in Spring (March-May).', 'বসন্তে (মার্চ-মে) কী রোপণ করবেন।',
             '<p>Ideal time for tomatoes, peppers, cucumbers, and beans. Start seeds indoors early or sow directly after frost.</p>',
             '<p>টমেটো, মরিচ, শসা এবং মটরশুটি রোপণের উপযুক্ত সময়। আগে থেকে ইনডোরে বীজ বপন করুন বা তুষারপাতের পর সরাসরি মাটিতে বুনুন।</p>',
             '/static/img/calendar_spring.svg'),

            ('seasonal_calendar', 'Winter Maintenance', 'শীতকালীন রক্ষণাবেক্ষণ',
             'Garden tasks for winter months.', 'শীতের মাসগুলোতে বাগানের কাজ।',
             '<p>Clean up debris, test soil, and plan next year\'s layout. Protect sensitive plants from frost.</p>',
             '<p>আবর্জনা পরিষ্কার করুন, মাটি পরীক্ষা করুন এবং আগামী বছরের পরিকল্পনা করুন। সংবেদনশীল গাছপালা তুষারপাত থেকে রক্ষা করুন।</p>',
             '/static/img/calendar_winter.svg'),

            # Expert Tips
            ('expert_tips', 'Watering Deeply', 'গভীরভাবে সেচ দেওয়া',
             'Why deep watering is better.', 'কেন গভীর সেচ ভালো।',
             '<p>Watering deeply encourages deep root growth, making plants more drought-resistant. Shallow watering leads to weak roots.</p>',
             '<p>গভীরভাবে পানি দিলে শিকড় গভীরে যায়, যা গাছকে খরা-সহনশীল করে তোলে। হালকা সেচ শিকড় দুর্বল করে।</p>',
             '/static/img/tip_water.svg'),
            
            ('expert_tips', 'Crop Rotation', 'ফসল আবর্তন',
             'Preventing soil-borne diseases.', 'মাটিুবাহিত রোগ প্রতিরোধ।',
             '<p>Rotate crops every year. Do not plant tomatoes or potatoes in the same spot for 3 years to avoid blight build-up.</p>',
             '<p>প্রতি বছর ফসল আবর্তন করুন। ব্লাইট রোগ এড়াতে একই স্থানে ৩ বছর ধরে টমেটো বা আলু লাগাবেন না।</p>',
             '/static/img/tip_rotation.svg')
        ]

        kb_sql = """INSERT INTO knowledge_base (
            category, title_en, title_bn, short_desc_en, short_desc_bn, content_en, content_bn, image_url
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        
        cursor.executemany(kb_sql, kb_data)
        conn.commit()
        
        print(f"✅ Success! {cursor.rowcount} records inserted with UTF-8 encoding.")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    init_db()
