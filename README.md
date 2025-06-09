## Mitigating Latency under High Concurrency: A Messaging-Driven Architecture for AI Inference Workloads

Synchronous architectures, such as conventional RESTful APIs, face significant challenges in responsiveness and availability when handling long-running computational tasks like AI inference, particularly under high concurrency. This repository presents an asynchronous, messaging-driven architecture designed to overcome these limitations. We conducted a comparative analysis of our proposed system, which utilizes a message broker and a persistent data store, against a traditional REST-based approach using a simulated AI workload. The results demonstrate that our architecture maintains constant, sub-second initial response times, thereby ensuring continuous endpoint availability. In contrast, the performance of the synchronous REST API degraded significantly as concurrent requests increased. By decoupling the initial request from the final result delivery, our approach enhances system scalability and improves the user experience for time-intensive operations.

### proposed system
![](proposed_system.PNG)
The inference process is built on a modular and scalable architecture to support asynchronous task execution.
- A Flask-based web service is responsible for receiving user inputs and initiating the inference workflow.
- A Redis NoSQL database, deployed within a Docker container, temporarily stores user inputs and prediction results.
- A cloud-based RabbitMQ system, implementing the AMQP protocol, manages message delivery between producers (web service) and consumers (background workers).
- The pre-trained AI model, trained on a task-specific dataset, performs the inference and returns results through the system pipeline.

## the command to install the libraries
pip install flask redis pika requests
## External Tools
- Redis Server (should be running locally on port 6379)
- RabbitMQ Cloud instance (uses a CloudAMQP connection)
