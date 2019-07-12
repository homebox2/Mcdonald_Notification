mcdonald-deploy:
	zip -r ../McDonald-Notification.zip ./ -x "*.git*" -x ".DS_Store" -x ".idea*"
	aws lambda update-function-code --publish --function-name McDonald-Notification --zip-file fileb://../McDonald-Notification.zip
	rm ../McDonald-Notification.zip

happy-food-deploy:
	zip -r ../Happy-Food-Notification.zip ./ -x "*.git*" -x ".DS_Store" -x ".idea*"
	aws lambda update-function-code --publish --function-name happy_food_notification --zip-file fileb://../Happy-Food-Notification.zip
	rm ../Happy-Food-Notification.zip

create-function:
	zip -r ../$(function_name).zip ./ -x "*.git*" -x ".DS_Store" -x ".idea*"
	aws lambda create-function --publish --function-name $(function_name) --runtime python2.7 --role arn:aws:iam::209570776318:role/lambda_function --handler $(handler) --zip-file fileb://../$(function_name).zip
	rm ../$(function_name).zip