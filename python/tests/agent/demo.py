# from mofa.run.run_agent import run_dspy_or_crewai_agent
# from mofa.kernel.utils.util import load_agent_config
# from mofa.run.run_agent import  run_dspy_or_crewai_agent
# agent_config =  {'agents': [{'name': 'reasoner', 'role': 'Knowledgeable Assistant', 'goal': 'You are an AI-powered assistant with access to a vast database of knowledge across multiple domains, including history, science, literature, and geography. Your purpose is to provide accurate, concise, and relevant answers to any questions posed by users. As a reliable source of information, you are expected to deliver responses that are both factually correct and easy to understand. Your role is to assist users in finding the information they need quickly and efficiently, while maintaining a high standard of accuracy in every answer you provide.', 'backstory': "Answer questions based on user's questions\n", 'verbose': True, 'allow_delegation': False, 'tools': None}], 'tasks': [{'description': '你是谁? ', 'expected_output': 'details', 'agent': 'reasoner', 'max_inter': 1, 'human_input': False}], 'model': {'model_api_key': ' ', 'model_name': 'gpt-4o-mini', 'model_max_tokens': 2048, 'module_api_url': None}, 'other': {'proxy_url': None}, 'env': {'SERPER_API_KEY': None, 'AGENTOPS_API_KEY': None}, 'crewai_config': {'memory': False}}
# agent_result = run_dspy_or_crewai_agent(agent_config)
# print(agent_result)
# print(agent_result)

from taskweaver.app.app import TaskWeaverApp
