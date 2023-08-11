resource "kubernetes_deployment" "flask-deployment"{
    metadata {
      name = "flask-deployment"
      labels = {
        "app"="flask"
      }
    }
    spec{
        replicas = 2
        selector {
          match_labels = {
              "app" = "flask"
          }
        }
        template {
          metadata {
            labels={
                "app"="flask"
            }
          }
          spec{
            container{
               name ="flask" 
               image="beatrix1997/flask_web_scraper:1.00"
               port{
                container_port=5000
               }
            }
          }
        }
    }

}