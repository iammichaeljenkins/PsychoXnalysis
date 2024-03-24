from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

def AI(message):
	model = 'ericzzz/falcon-rw-1b-instruct-openorca'
	tokenizer = AutoTokenizer.from_pretrained(model)
	pipeline = transformers.pipeline(
		'text-generation',
		model=model,
		tokenizer=tokenizer,
		torch_dtype=torch.bfloat16,
		device_map='auto',
		truncation=True
	)
	system_message = 'You are a psychological analyst specializing in social media behavior with deep knowledge of human cognition, emotion, and psychology. Provide deep and detailed insights into the psychological makeup of the individuals behind given tweets. Attempt to capture overarching themes and underlying psychological patterns. Conclude with a comprehensive psychoanalysis highlighting key personality traits, emotional states, and potential motivations. Ignore replacement characters.'
	instruction = f'Give a psychological profile of the author of the following tweets utilizing psychological terminology and theories in the context of the author\'s personality, emotions, cognitive processes, and motivators; each of these tweets will be individually in quotations and separated by commas. {message}'
	prompt = f'<SYS> {system_message} <INST> {instruction} <RESP> '

	response = pipeline(
	   prompt,
	   max_new_tokens = 500,
	   repetition_penalty=1.05,
	   pad_token_id = 50256
	)

	response[0]['generated_text'] = response[0]['generated_text'].replace(prompt,"")
	return response[0]['generated_text']
