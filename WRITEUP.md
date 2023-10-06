# Write-up

## Analyze, choose, and justify the appropriate resource option for deploying the app.

### Appropriate solution
- For the deployment of this exercise, I have selected Azure App Service as the most suitable resource option.

### Reasons for Choosing Azure App Service
- Managed Infrastructure: Azure App Service offers a fully managed infrastructure, taking care of essential tasks such as infrastructure maintenance, security patching, and auto-scaling. This frees me from the burden of handling these operational aspects.

- Language Diversity: Azure App Service provides support for a wide range of programming languages, including .NET, .NET Core, Java, PHP, Python, and more. This flexibility ensures that I can work with the language of my choice, which is Python in this case.

- Rapid Development and Deployment: Azure App Service allows for the rapid development, deployment, and scaling of web applications. It simplifies the deployment process, eliminating the need for complex environment setup, making it an excellent choice, especially when I have limited knowledge in server management.

### Why Not Virtual Machines
- While Virtual Machines (VMs) have their merits, they are not the ideal choice in this scenario due to the following considerations:

- Minimal OS Control: I do not intend to take control of the underlying Operating System or perform manual software installations on the server. Azure App Service abstracts away these tasks, allowing me to focus solely on application development.

- Ease of Deployment: My current level of knowledge may not be sufficient for setting up and configuring a Virtual Machine environment for this application. Azure App Service simplifies deployment, making it more accessible for developers with varying skill levels.

### Justification Based on Cost, Scalability, Availability, and Workflow
- Cost-Efficiency: Azure App Service offers cost-effective plans, including Free and Shared (preview) options for testing and deploying applications. This reduces operational costs compared to managing Virtual Machines.

- Scalability: Azure App Service provides both horizontal and vertical scaling options. Vertical scaling allows for easy adjustment of resources by changing the pricing tier, while horizontal scaling allows me to increase or decrease the number of instances, ensuring the application can adapt to changing demands.

- High Availability: Azure App Service ensures high availability with its global scale. This means I can host my application in Microsoft's global datacenter infrastructure, backed by a high availability Service Level Agreement (SLA).

- Workflow Integration: Azure App Service seamlessly integrates with various development workflows. It supports automated deployments from popular sources such as GitHub, Azure DevOps, and Git repositories. This simplifies the development workflow, enhancing efficiency.

### Considerations for Future App Changes
While Azure App Service is the current choice, certain circumstances may lead me to reconsider this decision:

- Hardware Limitations: If the application experiences substantial growth, requiring more resources and hardware customization, Virtual Machines may become a more suitable option due to their flexibility.

- Advanced Scaling and Control: In cases where advanced scaling or precise control over the environment is needed, Virtual Machines would be a better choice.

- Specialized Software: If specific software installations or configurations are required that are not supported by Azure App Service, opting for Virtual Machines might be necessary.

In conclusion, Azure App Service is the preferred resource option for deploying this exercise due to its managed infrastructure, language diversity, rapid development capabilities, cost-efficiency, scalability, high availability, and seamless workflow integration. However, future changes and specific requirements may prompt a reconsideration of this choice.