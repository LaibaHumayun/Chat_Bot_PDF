with open('.env', 'w') as f:
    f.write('OPENAI_API_KEY=your_openai_api_key_here\n')
    f.write('LLM_MODEL=gpt-3.5-turbo\n')

print('.env file created successfully') 