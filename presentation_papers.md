# Presentation Papers for Research Project Diagrams

This document provides a professional overview of each architectural and structural diagram used in the "Leaf Disease Detection" project.

---

## 1. CNN Architecture Diagram (MobileNetV2 based)
**Objective:** To illustrate the deep learning pipeline responsible for processing leaf images and extracting disease characteristics for classification.

### Key Components:
- **Input Layer:** Receives the raw leaf image.
- **Data Pipeline:** Performs resizing, normalization, and data augmentation.
- **Model Core:** Employs convolutional layers for feature extraction followed by Global Average Pooling.
- **Output Layer:** Provides a Softmax probability distribution over detected disease classes.

**Presentation Note:** This diagram effectively visualizes the system's internal flow by showing the hierarchical transformation of data from raw pixels to a clinical diagnosis.

---

## 2. UML Class Diagram
**Objective:** To describe the static structure of the application from an Object-Oriented Programming (OOP) perspective.

### Key Components:
- **LeafDetectorApp:** The central controller managing the interaction between logic and data.
- **CNNModel:** Encapsulates model weight loading and inference logic.
- **PlantPreprocessor:** Handles all image transformations before inference.
- **Entities (Treatment/KnowledgeBase):** Represent the data-centric models derived from the MySQL database.

**Presentation Note:** The Class Diagram demonstrates the modularity and scalability of the software architecture, ensuring that each component has a single, well-defined responsibility.

---

## 3. UML Use Case Diagram
**Objective:** To map the functional requirements and determine how different actors interact with the Leaf Disease Detection System.

### Key Components:
- **Primary Actor (Farmer/Researcher):** Executes core tasks like capturing images and viewing treatment results.
- **Secondary Actor (ML Model/Database):** Supplies the intelligence for detection and persistent data for treatments.
- **Relationships:** Uses `<<include>>` for mandatory preprocessing and `<<extend>>` for optional treatment retrieval.

**Presentation Note:** This diagram provides a stakeholder-level view of the system, identifying all possible operational scenarios and actor boundaries.

---

## 4. Entity-Relationship Diagram (ERD)
**Objective:** To represent the relational database schema used for managing disease knowledge and treatment strategies.

### Key Components:
- **Treatments Table:** Stores technical and organic treatment protocols linked by a unique `disease_key`.
- **KnowledgeBase Table:** Serves as a localized encyclopedia for farmers, containing categorized guides and media.
- **Notation:** Uses standard academic PK (Primary Key) and data type notations for MySQL compatibility.

**Presentation Note:** The ERD highlights the system's ability to store and retrieve cross-referenced botanical data, ensuring that the farmer receives the right treatment for the right diagnosis.

---
