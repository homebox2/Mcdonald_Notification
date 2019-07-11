mcdonald-deploy:
	zip -r ../McDonald-Notification.zip ./ -x "*.git*" -x ".DS_Store" -x ".idea*"
	aws lambda update-function-code --function-name McDonald-Notification --zip-file fileb://../McDonald-Notification.zip
	rm ../McDonald-Notification.zip

happy-food-deploy:
	zip -r ../Happy-Food-Notification.zip ./ -x "*.git*" -x ".DS_Store" -x ".idea*"
	aws lambda update-function-code --function-name happy_food_notification --zip-file fileb://../Happy-Food-Notification.zip
	rm ../Happy-Food-Notification.zip