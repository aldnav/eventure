Eventure: Activity Streams in Django
---
Eventure provides generic solution to logging activities.

> "In its simplest form, an activity consists of an actor, a verb, and an object. It tells the story of a person performing an action on or with an object -- "Geraldine posted a photo" or "John shared a video". In most cases these elements will be explicitly declared, but they may also be implied."  
~ Atom Activity Streams Spec

Specifications is based on the [Atom Activity Streams Spec](http://activitystrea.ms/specs/atom/1.0/)

* activity -- Atom Activity Streams app
* eventure -- Demo project
* extra -- Demo site

---
#### Application
##### Implied activity shorthand  
Follows the form `<actor> <verb> <object>`:  
Activity: `<wendy> <liked> a <tweet>`
```python
...
from activity import Activity, Verb
...
add = Verb.objects.create(name='liked')
activity = Activity.objects.create(
  actor=user,
  object_ref=tweet,
  verb=add,
  title='{} {} a {}'.format(user, add, tweet)
)
activity.title
# wendy liked a tweet
```

##### Full activity entry  
Follows the form `<actor> <verb> <object> <target>`:  
Activity: `<wendy> <added> <Only Hope> to <playlist>`
```python
...
from activity import Activity, Verb
...
add = Verb.objects.create(name='added')
activity = Activity.objects.create(
  actor=user,
  object_ref=song,
  verb=add,
  target=playlist,
  title='{} {} a {}'.format(user, add, song)
)
activity.title
# wendy added Only Hope to playlist
```


#### TO DO
* Generate Representations:  
  * JSON
  * XML
  * RSS
  * Metatags
* Verb tenses
* Better documentation
