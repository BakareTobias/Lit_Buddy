import json
import requests
from keybert import KeyBERT
import spacy
nlp = spacy.load("en_core_web_md")
""" keyword = 'machine learning'
springer_key = '8acabdf7c7db9349af44366e28f722e1'



url = f"https://api.springernature.com/meta/v2/json?q={keyword}&api_key={springer_key}&s=1&p=2"

response = requests.get(url)
data = (response.json())

#data
    #apiMessage
    #query
    #result
    #records-> abstract
    #facets
title = data['records']
abstract = data['records'][1]['abstract']

for i,item in enumerate(data['records']):
    print({
        f'{i}':[item['title'],item['abstract'],item['doi'],item['url'][0]['value']]
        })
    print() """

Obstacle_Detection_0 = """  The recent advancements in Artificial Intelligence and robotics have
                            highlighted the need for human-centered systems in industrial automation. As research and application
                            of Collaborative Robots become more prevalent, it is increasingly important to ensure their ability
                            to safely and efficiently navigate dynamic environments. This publication presents a modular
                            ROS-based system that leverages 3D computer vision to enhance obstacle detection and avoidance.
                            The integration of depth sensing and 3D object detection facilitates enhanced autonomy and safety
                            in Collaborative Robot applications. The results of the tests demonstrate that the system is capable
                            of achieving promising outcomes with low-budget sensing hardware. This provides a solid foundation 
                            for future enhancements in accuracy and flexibility, as well as the integration into other robotic systems."""

Obstacle_Detection_1 = """  As autonomous driving technology evolves, ensuring car dependability and safety is crucial. The versatile
                            Quanser Car (Q-car) platform provides an ideal testing ground for driverless vehicles. This research focuses
                            on enhancing self-driving car safety by implementing an effective obstacle detection system. The study aims 
                            to improve obstacle recognition in self-driving Q-Cars by integrating depth cameras with MATLAB Simulink.
                            Depth cameras offer advantages over yolo v5, providing vital three-dimensional environmental data essential 
                            for accurate obstacle detection and distance measurement. The research explores depth camera usage in driverless 
                            cars, detailing their integration into the Q-Car platform via Simulink. Additionally, it investigates how depth 
                            cameras can enhance safety features, especially collision avoidance. By leveraging depth cameras and MATLAB Simulink, 
                            the project aims to significantly boost autonomous vehicle safety and reliability on the Q-car platform, potentially 
                            advancing autonomous driving technology and fostering the development of safer self-driving cars."""

Obstacle_Detection_2 = """  Navigation in cluttered underwater environments is challenging, especially when there are constraints on communication
                            and self-localisation, and there is clutter in the environment. In this paper, we first studied the connection between
                            everyday activity of dog walking and the cooperative underwater obstacle avoidance problem. Inspired by this analogy, 
                            we propose a novel dog walking paradigm and implement it in a multi-agent underwater system. Simulations were conducted
                            across various scenarios, with performance benchmarked against traditional methods utilising Image-Based Visual 
                            Servoing in a multi-agent setup. The results indicate that our dog-walking-inspired paradigm significantly enhances 
                            cooperative behavior between agents and outperforms the existing approach in navigating through obstacles."""

Ultrasonic_Sensor_0 = """   In today’s evolving urban landscape, garbage management has emerged as a critical challenge for environmental 
                            sustainability and public health. Traditional waste collection involves manual inspection, where individuals 
                            check for waste accumulation, which is time-consuming and complex. To address this problem and assist waste 
                            management staff by saving time and reducing unnecessary trips, an intelligent dustbin prototype is proposed. 
                            This system allows workers to focus their efforts only when necessary, improving efficiency in waste collection. 
                            The intelligent dustbin prototype uses Internet of Things (IoT) components including NodeMCU ESP8266 microcontroller, 
                            HC-SR04 ultrasonic sensor, and Neo 6M GPS module to monitor garbage levels, track dustbin locations, and notify 
                            authorities if the garbage exceeds a threshold. The prototype is integrated with two in-built mobile applications: 
                            the Blynk App for real-time garbage level monitoring and the Telegram App, where a bot sends alerts and dustbin 
                            locations to waste management staff. This aids efficient waste management and improves collection and resource 
                            distribution."""

Ultrasonic_Sensor_1 = """After reading this chapter, the reader should be able."""

Ultrasonic_Sensor_2 = """Sonochemistry, specifically dependent on acoustic cavitation, has transformed chemical engineering through its possibilities of provocation of localized temperature and pressure. This chapter will discuss sonochemical technology, specifically ultrasonic reactors, which include ultrasonic baths, horns, and multiple-frequency flow cell reactors. Bubble dynamics are modeled according to the Rayleigh-Plesset equation together with the role of frequency, temperature, pressure, liquid, reactor geometry, and the transducer’s position. It has been used in nanoparticle preparation, nanoemulsion process, filtration process, ultrasonic 
atomization, and improvement of reaction rates in polymerization process, catalysis process, and enzymatic process. The chapter also discusses mass transfer modeling, namely the diffusion-limited model for vapor transport, ultrasound generation methods, piezoelectric and magnetostrictive transducers. Comparisons of sonochemistry with other hybrid technologies in controlling air contamination and biological wastewater treatment are also provided to highlight the importance of sonochemistry in developing more sustainable and innovative chemical engineering methods."""

A_Mobile_Robot_0 = """This chapter is dedicated to induced antifragility. Here, we discuss the benefits of input distribution irregularities based on emergent system 
dynamics in a feedback loop with a controller that drives the system towards a prescribed dynamics. We consider methods for detecting, analyzing, modelling, and controlling road traffic, robotics, and industrial control systems’ antifragility."""

A_Mobile_Robot_1 = """This study presents an adaptive positioning method for mobile cobots using a vision-based correction system integrated into a UR10 robotic arm. 
The approach involves two-stage positioning: the AMR (MiR100) docks at an initial location, then the vision system detects a reference marker to establish a local coordinate frame for precise task execution. This compensates for global positioning errors, enhancing repeatability and accuracy. Experimental validation on a CNC workstation confirmed improved alignment precision over standard AMR methods. The results highlight the potential of vision-based adaptive positioning for high-precision mobile cobot applications in dynamic industrial environments."""

A_Mobile_Robot_2 = """Mobile robot navigation is a constantly evolving field that is adopting new paradigms along the way, and recent methods, such as Transformer-based models, have helped facilitate advancements in perception and decision-making tasks in this decade alone. This paper explores modern scene understanding techniques, including Contrastive Language-Image Pretraining (CLIP) and its role in improving semantic scene comprehension for various indoor environments. Existing benchmarking methods for evaluating autonomous mobile robot navigation performance are limited in accommodating the dynamic nature of real-world scenarios. Therefore, a set of metrics is proposed for robust evaluation, highlighting the need for standardized frameworks that meet modern expectations. Furthermore, a multimodal robot navigation model is introduced; it consists of visual and laser data combined with semantic embeddings to augment navigation performance. The proposed model and metrics aim to contribute to better benchmarking standards for indoor robot navigation systems."""

abstracttt = "Fire-fighters face several risks on the job like burns, heat exhaustion, and also exposure to high levels of carbon monoxide and other toxic hazards that put them at greater risk. This system is designed with the help of a Raspberry Pi module, which is integrated with an ultrasonic sensor to avoid obstacles and a Pi camera to detect fire or smoke using the YOLOv2 Convolutional Neural Network. Live video streaming is also provided and can be accessed by the nearest firefighting station through a web page. An aluminium sheet is used to make the body of the robotic system, protecting it from high temperatures up to 700 °C. This intelligent robotic system performs many tasks, reduces damage caused by fire, and helps in saving the lives of human fire-fighters."
model = KeyBERT()
x = 'Obstacle Detection Using Ultrasonic Sensor For A Mobile Robot'
results = (model.extract_keywords(abstracttt, keyphrase_ngram_range=(1,2),stop_words='english'))
print(results)

def ranking_abstracts(RESULTS,topic):
	#Combine them in a hybrid scoring system:
	#1.	Exact overlap boost  phrases that exactly appear in the topic/abstract get a high weight (say +2).
	#2.	Semantic similarity score  compute cosine similarity of each phrase to the topic and/or the original abstract, normalize to [0,1].
	#3.	Aggregate scoring 
	#•	For each abstract, sum overlap_score + similarity_score.
	#•	Normalize by number of phrases, so long abstracts dont dominate unfairly.
	#4.	Rank abstracts by this hybrid score.
	
    doc_topic = nlp(topic.lower())
    abstract_scores_ranked = {}

     
    for key in RESULTS:
        abstract = RESULTS[key][1]
        abstract_score = 0
        results = (model.extract_keywords(abstract, keyphrase_ngram_range=(1,2),stop_words='english'))
        keyphrase_list = []
        for tup in results:
            keyphrase_list.append(tup[0])

        for keyphrase in keyphrase_list:
            #+2 if keyphrases are in topic
            if keyphrase in topic.lower():
                abstract_score+= 2


            #similarity scoring
            keyphrase = nlp(keyphrase)
            similarity = doc_topic.similarity(keyphrase)
            abstract_score += similarity

        #score_normalization
        abstract_score_normalized = abstract_score/len(keyphrase_list)
        #print(f'for {key}:{keyphrase_list} ,score {abstract_score} normalized to {abstract_score_normalized}')
        RESULTS[key].append(abstract_score_normalized)
        #print(RESULTS)
    RESULTS =dict(sorted(RESULTS.items(), key=lambda x: x[1][-1], reverse=True))
    return RESULTS

RESULTS = {
    "Obstacle Detection_0": [
        "Computer Vision-Based Environmental Perception for a Collaborative Robot",
        "The recent advancements in Artificial Intelligence and robotics have highlighted the need for human-centered systems in industrial automation. As research and application of Collaborative Robots become more prevalent, it is increasingly important to ensure their ability to safely and efficiently navigate dynamic environments. This publication presents a modular ROS-based system that leverages 3D computer vision to enhance obstacle detection and avoidance. The integration of depth sensing and 3D object detection facilitates enhanced autonomy and safety in Collaborative Robot applications. The results of the tests demonstrate that the system is capable of achieving promising outcomes with low-budget sensing hardware. This provides a solid foundation for future enhancements in accuracy and flexibility, as well as the integration into other robotic systems.",
        "10.1007/978-3-032-03515-8_38",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-032-03515-8_38"
    ],
    "Obstacle Detection_1": [
        "Obstacle Detection and Enhanced Safety for Self-driving Automobiles (ODESSA)",
        "As autonomous driving technology evolves, ensuring car dependability and safety is crucial. The versatile Quanser Car (Q-car) platform provides an ideal testing ground for driverless vehicles. This research focuses on enhancing self-driving car safety by implementing an effective obstacle detection system. The study aims to improve obstacle recognition in self-driving Q-Cars by integrating depth cameras with MATLAB Simulink. Depth cameras offer advantages over yolo v5, providing vital three-dimensional environmental data essential for accurate obstacle detection and distance measurement. The research explores depth camera usage in driverless cars, detailing their integration into the Q-Car platform via Simulink. Additionally, it investigates how depth cameras can enhance safety features, especially collision avoidance. By leveraging depth cameras and MATLAB Simulink, the project aims to significantly boost autonomous vehicle safety and reliability on the Q-car platform, potentially advancing autonomous driving technology and fostering the development of safer self-driving cars.",
        "10.1007/978-3-031-93688-3_26",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-031-93688-3_26"
    ],
    "Obstacle Detection_2": [
        "Fully Distributed Cooperative Multi-agent Underwater Obstacle Avoidance",
        "Navigation in cluttered underwater environments is challenging, especially when there are constraints on communication and self-localisation, and there is clutter in the environment. In this paper, we first studied the connection between everyday activity of dog walking and the cooperative underwater obstacle avoidance problem. Inspired by this analogy, we propose a novel dog walking paradigm and implement it in a multi-agent underwater system. Simulations were conducted across various scenarios, with performance benchmarked against traditional methods utilising Image-Based Visual Servoing in a multi-agent setup. The results indicate that our dog-walking-inspired paradigm significantly enhances cooperative behavior between agents and outperforms the existing approach in navigating through obstacles.",
        "10.1007/978-3-032-01486-3_28",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-032-01486-3_28"
    ],
    "Ultrasonic Sensor_0": [
        "Prototype Design and Implementation of an IoT Based Intelligent Dustbin for Smart City",
        "In today’s evolving urban landscape, garbage management has emerged as a critical challenge for environmental sustainability and public health. Traditional waste collection involves manual inspection, where individuals check for waste accumulation, which is time-consuming and complex. To address this problem and assist waste management staff by saving time and reducing unnecessary trips, an intelligent dustbin prototype is proposed. This system allows workers to focus their efforts only when necessary, improving efficiency in waste collection. The intelligent dustbin prototype uses Internet of Things (IoT) components including NodeMCU ESP8266 microcontroller, HC-SR04 ultrasonic sensor, and Neo 6M GPS module to monitor garbage levels, track dustbin locations, and notify authorities if the garbage exceeds a threshold. The prototype is integrated with two in-built mobile applications: the Blynk App for real-time garbage level monitoring and the Telegram App, where a bot sends alerts and dustbin locations to waste management staff. This aids efficient waste management and improves collection and resource distribution.",
        "10.1007/978-3-032-00777-3_10",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-032-00777-3_10"
    ],
    "Ultrasonic Sensor_1": [
        "PMC Peripheral Interfacing",
        "After reading this chapter, the reader should be able.",
        "10.1007/978-3-031-85944-1_4",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-031-85944-1_4"
    ],
    "Ultrasonic Sensor_2": [
        "Sonochemistry in Chemical Engineering",
        "Sonochemistry, specifically dependent on acoustic cavitation, has transformed chemical engineering through its possibilities of provocation of localized temperature and pressure. This chapter will discuss sonochemical technology, specifically ultrasonic reactors, which include ultrasonic baths, horns, and multiple-frequency flow cell reactors. Bubble dynamics are modeled according to the Rayleigh-Plesset equation together with the role of frequency, temperature, pressure, liquid, reactor geometry, and the transducer’s position. It has been used in nanoparticle preparation, nanoemulsion process, filtration process, ultrasonic atomization, and improvement of reaction rates in polymerization process, catalysis process, and enzymatic process. The chapter also discusses mass transfer modeling, namely the diffusion-limited model for vapor transport, ultrasound generation methods, piezoelectric and magnetostrictive transducers. Comparisons of sonochemistry with other hybrid technologies in controlling air contamination and biological wastewater treatment are also provided to highlight the importance of sonochemistry in developing more sustainable and innovative chemical engineering methods.",
        "10.1007/978-3-031-91656-4_3",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-031-91656-4_3"
    ],
    "A Mobile Robot_0": [
        "Induced Antifragility",
        "This chapter is dedicated to induced antifragility. Here, we discuss the benefits of input distribution irregularities based on emergent system dynamics in a feedback loop with a controller that drives the system towards a prescribed dynamics. We consider methods for detecting, analyzing, modelling, and controlling road traffic, robotics, and industrial control systems’ antifragility.",
        "10.1007/978-3-031-90425-7_4",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-031-90425-7_4"
    ],
    "A Mobile Robot_1": [
        "Adaptive Positioning of a Mobile Robot for Precise Workstation Operation",
        "This study presents an adaptive positioning method for mobile cobots using a vision-based correction system integrated into a UR10 robotic arm. The approach involves two-stage positioning: the AMR (MiR100) docks at an initial location, then the vision system detects a reference marker to establish a local coordinate frame for precise task execution. This compensates for global positioning errors, enhancing repeatability and accuracy. Experimental validation on a CNC workstation confirmed improved alignment precision over standard AMR methods. The results highlight the potential of vision-based adaptive positioning for high-precision mobile cobot applications in dynamic industrial environments.",
        "10.1007/978-3-032-01517-4_26",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-032-01517-4_26"
    ],
    "A Mobile Robot_2": [
        "Toward Semantic Scene Understanding: Benchmarking for Mobile Robot Navigation Indoors",
        "Mobile robot navigation is a constantly evolving field that is adopting new paradigms along the way, and recent methods, such as Transformer-based models, have helped facilitate advancements in perception and decision-making tasks in this decade alone. This paper explores modern scene understanding techniques, including Contrastive Language-Image Pretraining (CLIP) and its role in improving semantic scene comprehension for various indoor environments. Existing benchmarking methods for evaluating autonomous mobile robot navigation performance are limited in accommodating the dynamic nature of real-world scenarios. Therefore, a set of metrics is proposed for robust evaluation, highlighting the need for standardized frameworks that meet modern expectations. Furthermore, a multimodal robot navigation model is introduced; it consists of visual and laser data combined with semantic embeddings to augment navigation performance. The proposed model and metrics aim to contribute to better benchmarking standards for indoor robot navigation systems.",
        "10.1007/978-3-031-93825-2_9",
        "http://link.springer.com/openurl/fulltext?id=doi:10.1007/978-3-031-93825-2_9"
    ]
}


""" 
abstract = "In the context of Industry 4.0, Digital Twin (DT) technology offers significant potential to enhance industrial safety. However, its adoption in Process Safety Management (PSM) remains limited, especially in delivering real-time, predictive capabilities. This paper proposes a scalable and adaptive Process Safety Digital Twin (PS-DT) architecture for real-time risk prediction and integrity barrier monitoring in oil and gas operations. The architecture integrates sensor data with a trained Bayesian Network (BN) and a dynamic Bow-Tie model to enable continuous monitoring of failure risks and predictive hazard analysis. The PS-DT system is aligned with major industry standards, including API 754 for Tier 3 safety indicators, API 521 for pressure-relieving scenarios, OSHA 1910.119 for compliance, and the IBM Bow-Tie framework for barrier-based risk visualization. These standards address the limitations of current static risk assessments by enabling dynamic monitoring of barrier degradation and early warnings of hazard escalation. To validate the architecture, a prototype use case is implemented using a Pressure Relief Valve (PRV)—a critical Safety Critical Equipment (SCE)—to simulate barrier impairments and overpressure scenarios. Synthetic time-series data is generated in Python to train the BN, which estimates the probabilities of overpressure events, Loss of Process Containment (LOPC), and other consequences. A dynamic Bow-Tie visualization tracks evolving risk pathways, while interactive dashboards present Tier 3 KPIs, barrier health, and recommended actions to support decision-making. This research demonstrates how the PS-DT system can enhance operational safety by shifting from reactive to proactive risk management. The proposed architecture is modular, ISA-95-aligned, and designed for easy integration with existing plant systems, making it extensible across multiple SCEs and applicable to broader process industries."

results = (model.extract_keywords(abstract, keyphrase_ngram_range=(1,2),stop_words='english'))
print(results) """