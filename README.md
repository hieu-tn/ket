## SERVER (Django) ##

#### DONE ####
* registration 
    * get verification code by sms/email (target should be username later)
    * verify code
    * register with verified username + password
* log in
    * do challenge if not confirmed
    * else response access token
* forgot password
    * send new password by sms/email (prefer sms)
    * change password once login
* change password

#### TODO ####
- mfa???
- sms service
    - SNS? / Twilio?
- disable "long time no see" user:
    - cronjob?
    - check condition when user login?

- - - -

## APP (Angular) ##

#### Done ####

#### TODO ####
- setup project
- config

- - - -

## DEPLOYMENT ##

#### DONE ####

#### TODO ####
- k8s
