# The Yaml Syntax

## What is Yaml?
Yaml is a serialization language, just like JSON and XML. A serialization language is a standard format to transfer data, between applications written in different technologies.

The name yaml stands for "yaml ain't markup language". 
 - You can create files with either the "yaml" extension or the "yml" extension, they are the same.

 It is a very intuitive and human readable language which is why it is used to write configuration files for a lot of the popular devops tools used today.

 ## Yaml use cases
 Yaml is used in
 - docker compose files
 - ansible 
 - prometheus
 - Kubernetes

 ## Yaml Syntax

#### simple key-value pair:
Here is an example of how to write some key value pairs in Yaml:
<code>
app: user-authentication
port: 9000
version: 1.7
</code>

We have different data types here. The first one is a string. Strings DON'T  HAVE TO be enclosed in quotes but you can use them if you want to. If you have to use special characters like "\n" for example, you have to use quotes though.

- comments:
To create a comment  you use the "#" symbol on a new line.
Words preceded by a "#" sign will be interpreted as comments 


### Objects:
To group together a list of key-value pairs you can create an object, by indenting the key-value pairs and enclosing them in an object like this:

<code>
# object microservice
microservice:
    app: user-authentication
    port: 9000
    version: 1.7
</code>

Indentation is very important in Yaml, just like in python. All key-value pairs of an object must have the same level of indentation.

- Some useful Yaml linters are: https://rhysd.github.io/actionlint/  (for github actions and  https://codebeautify.org/yaml-validator?utm_content=cmp-true)


### lists:
You can create lists simply by using dashes:
<code>
# object microservice
microservice:
    - app: user-authentication
      port: 9000
      version: 1.7
</code>
 Important that the attributes stay at the same indentation level

Here is a piece of Yaml code:
<code>
yaml: 
  - slim and flexible
  - better for configuration
object:
	key: value
    </code>

And here is its equivalent in JSON
<code>
 "yaml": [
    "slim and flexible",
    "better for configuration"
  ],
  "object": {
    "key": "value"}</code>

### Booleans
Accepted Booleans are "yes/no" or "true/false" or "on/off":

<code>

microservice:
    - app: user-authentication
      port: 9000
      version: 1.7
      deployed: off
</code>