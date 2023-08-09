# The YAML Syntax

## What is YAML?
YAML is a serialization language, just like JSON and XML. A serialization language is a standard format to transfer data, between applications written in different technologies.

The name YAML stands for "YAML ain't markup language". 
 - You can create files with either the "YAML" extension or the "yml" extension, they are the same.

 It is a very intuitive and human readable language which is why it is used to write configuration files for a lot of the popular devops tools used today.

 ## YAML use cases
 YAML is used in
 - docker compose files
 - ansible 
 - prometheus
 - Kubernetes

 ## Basic YAML Syntax

#### simple key-value pair:
Here is an example of how to write some key value pairs in YAML:
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

Indentation is very important in YAML, just like in python. All key-value pairs of an object must have the same level of indentation.

- Some useful YAML linters are: https://rhysd.github.io/actionlint/  (for github actions and  https://codebeautify.org/YAML-validator?utm_content=cmp-true)

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

Here is a piece of YAML code:
<code>
YAML: 
  - slim and flexible
  - better for configuration
object:
	key: value
    </code>

And here is its equivalent in JSON
<code>
 "YAML": [
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

## More on Lists
The above example was an object that contained a list with a single object.

### Lists of objects
We can also define lists of objects more generically by adding a dash to every new object of the list.
<code>
microservice:
    - app: user-authentication
      port: 9000
      version: 1.7
      deployed: off
    - app: shopping-cart
      port: 9001
      version: 1.9
</code>
A microservice object which has a key called microservice and a value that is a list that contains two objects. Here is the equivalent in JSON:

<code>
{
  "microservice": [
    {
      "app": "user-authentication",
      "port": 9000,
      "version": 1.7,
      "deployed": "off"
    },
    {
      "app": "shopping-cart",
      "port": 9001,
      "version": 1.9
    }
  ]
}
</code>

### Lists of simple objects
<code>
microservices:
    - user-authentication
    - shopping-cart
<code>

### List of lists
We can also define lists of lists like so:
<code>
microservices:
    - user-authentication
      versions:
      - 1.9
      - 2.0
</code>

You can also use square brackets instead of dashes:
<code>
microservices:
    - user-authentication
      versions:[1.9, 2.0]
</code>

Equivalent in JSON:
<code>
{
  "microservices": [
    "user-authentication versions:[1.0,2.0]"
  ]
}
</code>

## Real YAML example with a Kubernetes Configuration File:
Let's look at an example of a real YAML file. This is a configuration file for Kubernetes:
<code>
apiVersion:1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
  - name: nginx-container
    image: nginx
    ports: 
    - containerPort: 80
    volumneMounts:
    - name: nginx-vol
      mountPath: /user/nginx/html



</code>

We have:
- key-value pairs
- metadata = object
- labels = object
- spec = object
- containers =  lists of objects
- ports = list
- volumeMounts =  Lists of Objects