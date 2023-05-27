CSS_SELECTORS = {
    "token": "input[type=hidden]", # all submissions
    "form_name": "input[name=FormName]", # all submissions
    "title": "#Name input", # thread, question, event
    "game": "#Category .GameCategory input[type=hidden]", # thread, question, event
    "category": "#Category .Category input[type=hidden]", # thread, question, event
    "text": "#Article .Source textarea", # thread, question, event
    "subtitle": "#Description input", # thread, question
    "access": "#Status input", # thread, question, event
    "toc": "#TableOfContentsToggle input", # thread, event
    "analytics": "#AnalyticsToggle input", # thread, question, event
    "comments": "#CommentsMode input", # thread, question
    "start_date_month": "#StartDate select", # values: 1-12; event
    "start_date_day": "#StartDate select:nth-child(2)", # values: 1-31; event
    "start_date_year": "#StartDate select:nth-child(3)", # values: 1990-<current+10>; event
    "start_date_hour": "#StartDate select:nth-child(5)", # values: 0-23; event
    "start_date_minute": "#StartDate select:nth-child(7)", # values: 0-55, step: 5; event
    "end_date_month": "#EndDate select", # values: 1-12; event
    "end_date_day": "#EndDate select:nth-child(2)", # values: 1-31; event
    "end_date_year": "#EndDate select:nth-child(3)", # values: 1990-<current+10>; event
    "end_date_hour": "#EndDate select:nth-child(5)", # values: 0-23; event
    "end_date_minute": "#EndDate select:nth-child(7)", # values: 0-55, step: 5; event
    "timezone": "#Timezone select", # format: <continent>/<country> and 'UTC'; event
    "repeat": "#Repeat select", # values: never, daily, weekly, monthly, yearly; event
    "location": "#Location input", # event
    "image": "#Image input[type=hidden]", # event
    "type": "#Type select", # ware
    "pending_message": "#PendingMessage .Source textarea", # ware
    "delivered_message": "#DeliveredMessage .Source textarea", # ware
    "screenshots": "#Screenshots input[type=hidden]", # ware
    "request_requirements": "#Requirements div.WysiwygList", # request
    "code": "#Code textarea", # script
    "who_is_the_creator": "#WhoIsTheCreator input[type=hidden]", # script
    "submission_authors": "g_sInputName[ ]*=[ ]*\".*\"\;", # RegEx; script
    "language": "#Language select", # script
    "comment_instructions": "#CommentInstructions .Source textarea", # script
    "studio": "#Studio select", # script
    "license": "#License .Source textarea", # script
    "license_checklist": "#LicenseChecklist input", # script
    "requirements": "#Requirements input[type=text]", # script
    "contest": "#Contest select", # script
    "jam": "#Jam select", # script
    "project": "#Project select", # script
}
