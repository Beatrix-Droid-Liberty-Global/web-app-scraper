resource "kubernetes_deployment" "flask-deployment"{
    metadata {
      name = "flask-deployment"
      labels = {
        app="flask"
      }
    }
    spec{
        replicas = 2
        selector {
          match_labels{
            labels{
                app="flask"
            }
          }
        }
        template {
          metadata {
            labels{
                app="flask"
            }
          }
          spec{
            containers{
               name ="flask" 
               image="beatrix1997/flask_web_scraper:1.00"
               ports{
                containerPort=5000
               }
            }
          }
        }
    }

}