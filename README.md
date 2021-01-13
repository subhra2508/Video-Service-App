# Video-Service-App
## This is made by Django,Bootstrap,and Reactjs.
## Model Architechture
######
Membership
    ---slug
    ---type  (free,pro,enterprise)
    ---price
    ---stripe plan id

UserMembership
    -user                      (foreignkey to default user)
    -stripe customer id
    -membership type            (foreignkey to membership)

Subscription
    -user membership
    -stripe subscription id (foreignkey to Usermembership)
    -active

Course
    -slug
    -title
    -description
    -allowed memberships   (foreignkey to membership)

Lesson
    -slug
    -title
    -course  (foreign to course)
    -position
    -video
    -thumbnail  
