# The YAML Syntax
This is a YAML primer that should quickly enable users to pick up the YAML language and start using it in the various devops tools.

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
```
app: user-authentication
port: 9000
version: 1.7
```

We have different data types here. The first one is a string. Strings DON'T  HAVE TO be enclosed in quotes but you can use them if you want to. If you have to use special characters like "\n" for example, you have to use quotes though.

- comments:
To create a comment  you use the "#" symbol on a new line.
Words preceded by a "#" sign will be interpreted as comments 


### Objects:
To group together a list of key-value pairs you can create an object, by indenting the key-value pairs and enclosing them in an object like this:

```
# object microservice
microservice:
    app: user-authentication
    port: 9000
    version: 1.7
```

Indentation is very important in YAML, just like in python. All key-value pairs of an object must have the same level of indentation.

- Some useful YAML linters are: https://rhysd.github.io/actionlint/  (for github actions and  https://codebeautify.org/YAML-validator?utm_content=cmp-true)

### lists:
You can create lists simply by using dashes:
```
# object microservice
microservice:
    - app: user-authentication
      port: 9000
      version: 1.7
```
 Important that the attributes stay at the same indentation level

Here is a piece of YAML code:
```
YAML: 
  - slim and flexible
  - better for configuration
object:
	key: value
    ```

And here is its equivalent in JSON
```
 "YAML": [
    "slim and flexible",
    "better for configuration"
  ],
  "object": {
    "key": "value"}```

### Booleans
Accepted Booleans are "yes/no" or "true/false" or "on/off":

```
microservice:
    - app: user-authentication
      port: 9000
      version: 1.7
      deployed: off
```

## More on Lists
The above example was an object that contained a list with a single object.

### Lists of objects
We can also define lists of objects more generically by adding a dash to every new object of the list.
```
microservice:
    - app: user-authentication
      port: 9000
      version: 1.7
      deployed: off
    - app: shopping-cart
      port: 9001
      version: 1.9
```
A microservice object which has a key called microservice and a value that is a list that contains two objects. Here is the equivalent in JSON:
```
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
```

### Lists of simple objects
```
microservices:
    - user-authentication
    - shopping-cart
```

### List of lists
We can also define lists of lists like so:
```
microservices:
    - user-authentication
      versions:
      - 1.9
      - 2.0
```
You can also use square brackets instead of dashes:
```
microservices:
    - user-authentication
      versions:[1.9, 2.0]
```
Equivalent in JSON:
```
{
  "microservices": [
    "user-authentication versions:[1.0,2.0]"
  ]
}
```

## Real YAML example with a Kubernetes Configuration File:
<<<<<<< HEAD
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
=======
Here is an example of a real YAML file that is a Kubernetes configuration file:
```
apiVersion: v1
kind: Pod
metadata:
    name: nginx
    labels:
        app: nginx
spec:
    containers:
    - name: ninginx
      image: nginx
      ports:
      - containerPort: 80
      volumneMouts:
      - name: nginx-vol
        mountPath: /usr/nginx/html
    - name: sidecar-container
      image: curl/images/curl
      command: ["/bin/sh"]
      args: ["-c", "echo Hello from the sidecar container; sleep 300"]
```

What we have here are:
- Key-value pairs
- metadata =  object
- labels =  object
- spec = object
-  containers = list of objects
- ports =  list
-  volumeMounts =  list of objects

###  Multiline Strings
Multiline strings are created by passing the "|" (pipe) symbol in front of the key,
and writing the new string in indendented new lines:

```
multilineString: |
    this is a multiline
    string. On two lines
```
If you have a long string which SHOULD be interpreted as a SINGLE LINE string but for readability you want to write it as a multiline string, you will use the ">" instead:
```
multilineString: >
    this is a multiline
    string. On two lines
```
This is the same as writing:
```
multilineString: this is a multiline string. On two lines
```

Here is an example of a config file:
```
apiVersion: v1
kind: ConfigMap
metadata:
    nameL mosquitto-config-file
data:
    # this code shouldbe executed one line at a time hence the pipe
    mosquitto.conf: |
        log_dest stdout
        log_type all
        log_timestamp true
        listener 9001
```

Here is another example, where it executes a shell command and calls a shell script. You can actually
put an entire shell script into a pipe command
```
command:
    - sh
    - c
    - |
      #!/usr/bin/env bash e
      http (){
        local path="${1}"
        set -- -XGET -s --fail
        # some more stuff here
        curl -k "s@" "http://localhost:5601${path}"
      }
      http "app/kibana"
```

## Environment Variables
You can access environment variables of a yaml file with the "$" (dollar sign) symbol:

```
command:
    - /bin/sh
    - -ec
    - >-
      mysql -h 127.0.0.1 -u root -p$MYSQL_ROOT_PASSWORD -e "SELECT 1"
```

## YAML placeholders
Rather than writing variables inside, you can define placeholders with double curly braces. The inside can be defined with tempalte generation
```
apiVersion: v1
kind: Service
metadata:
    name: {{.Values.service.name}}
spec:
    selector:
        app: {{.Values.service.app}}
    ports:
        - protocol: TCP
          port: {{.Value.service.targetport}}
```

## multiple YAML components:
You can write out different multiple YAML components in a single file with a line separator that consists of three dashes like this"---":

```
apiVersion: v1
kind: ConfigMap
metadata:
    name: mosquitto-config-file
data:
    mosquitto.conf: |
        log_dest stdout
        log_type all
        log_timestamp true
        listener 9001

# separator where the second component begins
---
apiVersion: v1
kind: Secret
metadata:
    name: mosquitto-secret-file
type: Opaque
data:
# some more config stuff here
```

Finally, it is worth mentioning that altough Kubernetes Configuration Files are typically written in YAML, Kubernetes also supports writing configuration files in JSON 
>>>>>>> a80614235469c6b62322d9585268d0b47f4ecea4
