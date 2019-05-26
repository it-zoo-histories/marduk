preparing-dataset:
	npx chatito ./train/beforeGenerateDataset/chatitoEntry.chatito --format=rasa --outputPath=./train

train-nlu:
	python -m rasa_nlu.train -c configuration/conf.nlu.yml --data train/rasa_dataset_training.json -o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d train/domains.yml -s train/story.md -o models/current/dialogue -c configuration/policies.yml