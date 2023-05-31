__all__ = [
    "SELECTORS",
]

SELECTORS = {
    "token": "input[type=hidden]",
    "form_name": "input[name=FormName]",
    "title": "#Name input",
    "game": "#Category .GameCategory input[type=hidden]",
    "category": "#Category .Category input[type=hidden]",
    "text": "#Article .Source textarea",
    "subtitle": "#Description input",
    "access": "#Status input",
    "toc": "#TableOfContentsToggle input",
    "analytics": "#AnalyticsToggle input",
    "comments": "#CommentsMode input",
    "start_date_month": "#StartDate select", # 1-12
    "start_date_day": "#StartDate select:nth-child(2)", # 1-31
    "start_date_year": "#StartDate select:nth-child(3)", # 1990-<current+10>
    "start_date_hour": "#StartDate select:nth-child(5)", # 0-23
    "start_date_minute": "#StartDate select:nth-child(7)", # 0-55, step: 5
    "end_date_month": "#EndDate select", # 1-12
    "end_date_day": "#EndDate select:nth-child(2)", # 1-31
    "end_date_year": "#EndDate select:nth-child(3)", # 1990-<current+10>; event
    "end_date_hour": "#EndDate select:nth-child(5)", # 0-23
    "end_date_minute": "#EndDate select:nth-child(7)", # 0-55, step: 5
    "timezone": "#Timezone select", # <continent>/<country> and 'UTC'
    "repeat": "#Repeat select", # never, daily, weekly, monthly, yearly
    "location": "#Location input",
    "image": "#Image input[type=hidden]",
    "type": "#Type select", # ware
    "pending_message": "#PendingMessage .Source textarea",
    "delivered_message": "#DeliveredMessage .Source textarea",
    "screenshots": "#Screenshots input[type=hidden]",
    "request_requirements": "#Requirements div.WysiwygList",
    "code": "#Code textarea",
    "who_is_the_creator": "#WhoIsTheCreator input[type=hidden]",
    "submission_authors": "g_sInputName[ ]*=[ ]*\".*\"\;",
    "language": "#Language select",
    "comment_instructions": "#CommentInstructions .Source textarea",
    "studio": "#Studio select",
    "license": "#License .Source textarea",
    "license_checklist": "#LicenseChecklist input",
    "requirements": "#Requirements input[type=text]",
    "contest": "#Contest select",
    "jam": "#Jam select",
    "project": "#Project select",
}
