# Google-Solution-23

### Our Theme ${\color{green}AQI \space : \space World's \space Climate \space Through \space Your \space Lens }$
-**Introduction:**
In a world threatened by air pollution, understanding air quality is crucial. The Air Quality Index (AQI) is a tool, offering insights into pollution levels and associated health risks.

-**Exploration of AQI Components:**
AQI measures various pollutants like particulate matter, ozone, carbon monoxide, sulfur dioxide, and nitrogen dioxide, explaining their sources and health effects.

-**Calculation and Interpretation:**
The methodology behind AQI calculation, pollutant weighting, and category implications, ranging from "Good" to "Hazardous," is crucial for public health awareness.

-**Data Collection and Monitoring:**
Examining AQI data sources, including government agencies, monitoring stations, and satellite observations, highlights the need for real-time monitoring and data transparency.

-**Global Perspectives:**
Comparing AQI systems worldwide reveals insights into cultural, geographical, and regulatory factors affecting air quality management and international cooperation.

-**Health Impacts and Mitigation Strategies:**
The health consequences of exposure to various AQI levels, coupled with effective mitigation strategies like emission controls and urban planning, underscore the importance of AQI.

-**Empowering Public Awareness:**
AQI plays a critical role in raising public awareness about air pollution through educational initiatives, community engagement, and digital platforms.

-**Case Studies and Future Outlook:**
Illustrative city and regional success stories demonstrate the impact of measures to improve air quality, offering insights into future trends in air quality management.

Conclusion:
As we strive for clean air for future generations, AQI's significance in fostering global collaboration and prioritizing public health cannot be overstated, ensuring a healthier, more sustainable world.

### SDGs We Addressed
<details open><summary><b>Sustainable Cities and Communities (11)</b></summary>
  
The Sustainable Development Goal (SDG) 11 aims to make cities and human settlements inclusive, safe, resilient, and sustainable. It targets issues such as access to adequate housing, sustainable transport, green spaces, and slum upgrading. The goal also emphasizes the importance of reducing the environmental impact of cities, including air pollution and waste management. 
</details>
<details><summary><b>Climate action (13)</b></summary>
  SDG 13 focuses on urgent action to combat climate change and its impacts. It emphasizes the need for countries to strengthen resilience and adaptive capacity to climate-related disasters. This goal also highlights the importance of integrating climate change measures into national policies, strategies, and planning.
</details>
<details><summary><b>Life On Land (15)</b></summary>
  SDG 15, Life on Land, aims to protect, restore, and promote sustainable use of terrestrial ecosystems, emphasizing the importance of biodiversity conservation and combating land degradation.
In our project, we leverage image processing technology to monitor and assess the impact of human activities on terrestrial ecosystems, aligning with SDG 15's goals of sustainable land use and biodiversity preservation.
</details>

### Brief Approach
- **Objective:** Deploy optimized CNN models for image processing using Streamlit, fine-tuning them with boosting algorithms, and specifying hyperparameters like Adam learning rate as 0.001.

- **Steps:**
  1. **Dataset Preparation:** Gather and preprocess a diverse image dataset.
  2. **Model Selection:** Choose InceptionV3, RCNNs, and VGG16.
  3. **Model Training:** Implement and train models, fine-tuning with boosting algorithms.
  4. **Performance Evaluation:** Assess model performance using standard metrics.
  5. **Deployment with Streamlit:** Create a user-friendly web app interface.
  6. **Integration:** Deploy fine-tuned models within the Streamlit app.
  7. **Testing and Validation:** Ensure functionality and performance meet expectations.
  8. **Documentation:** Document the process, results, and recommendations.
</details>

 - **Approach of code:**

  1. Tensorflow 
  2. Keras
  3. Numpy
  4. Pandas
  5. Matplotlib
  6. Seaborn
  7. Streamlit
  8. VGG16
  9. InceptionV3
  10. Boosting algo
  11. OpenCV

This approach ensures efficient deployment of optimized CNN models, facilitating seamless image processing tasks for end-users.
- **Information about the Approach**
  - **Air Polution**
     High air pollution levels, indicated by elevated Air Quality Index (AQI), can adversely affect vegetation, including lichens. Lichens are particularly sensitive to air quality changes. Increased pollutants like sulfur dioxide and nitrogen oxides can harm lichens, leading to reduced diversity and abundance. Monitoring AQI is crucial for understanding and mitigating the impact of air pollution on ecosystems. 
VGG16 (a convolutional neural network) and R-CNN (Region-based Convolutional Neural Network) can be employed in the study of Air Quality Index (AQI) through image analysis. VGG16 can help with feature extraction from air quality images, while R-CNN can identify and classify regions of interest within those images, such as pollution sources or affected areas. This integration of deep learning models facilitates automated analysis, aiding in the assessment and prediction of AQI based on visual data.
  - **VGG16**
    1. *Architecture*: VGG16's uniform architecture, with 3x3 filters in convolutional layers and 2x2 pooling layers, stands out for its simplicity and clarity.
    2. *Depth*: While relatively shallow compared to modern architectures, VGG16's 16 layers contributed to its computational cost and effectiveness.
    3. *Performance*: VGG16 achieved state-of-the-art results on ImageNet, demonstrating the power of its design and depth.
    4. *Legacy*: VGG16 has influenced subsequent architectures and remains a reference point in understanding convolutional neural network design.
  - **RCNN and it's Hyper Parameters**
     1.	 *Image Preprocessing*: Parameters for resizing, normalization, and preparing images for CNN input.
     2.	 *Region Proposal*: Parameters for generating proposals, like proposal number and overlap threshold.
     3.	 *CNN Architecture*: Parameters for CNN design, including layer count, filter size, and channel number.
     4.	 *Training*: Parameters for training, such as learning rate, batch size, and epochs.
     5.  *Region Pooling*: Parameters for feature extraction from proposals, like pooling region size.
     6.	 *Loss Function*: Parameters for defining error weights in the loss function.

Tuning these hyperparameters is crucial for R-CNN performance. Manual tuning and automated techniques are used.
   
     

### Resources
* **Dataset used:** Air Pollution Image Dataset from India and Nepal. 
Kaggle. https://doi.org/10.34740/KAGGLE/DS/3152196

### Contributors
- Anidipta Pal
- Ankana Datta
- Anjishnu Mukherjee
- Ananyo Dasgupta
