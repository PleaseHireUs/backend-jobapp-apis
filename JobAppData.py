class JobAppData:
    def __init__(self, userId, platform, companyName, jobTitle, createdDate,
                 jobStatus, emailId, jobUrl, modifiedDate = None):
        self.userId = userId
        self.platform = platform
        self.companyName = companyName
        self.jobTitle = jobTitle
        self.createdDate = createdDate
        self.jobStatus = jobStatus
        self.emailId = emailId
        self.jobUrl = jobUrl
        self.modifiedDate = modifiedDate

    def to_dict(self):
        return {
            'userId': self.userId,
            'platform': self.platform,
            'companyName': self.companyName,
            'jobTitle': self.jobTitle,
            'createdDate': self.createdDate,
            'jobStatus': self.jobStatus,
            'emailId': self.emailId,
            'jobUrl': self.jobUrl,
            'modifiedDate': self.modifiedDate
        }