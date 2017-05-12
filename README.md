# Elasticsearch_Mysql

This document is about Elasticsearch Server , IP: 35.187.213.244.

**1.Requirements:**

   We need Elasticsearch, logstash, JDBC plugin installed on Elasticsearch Server.
   
     -install java
     
      sudo yum install java-1.8.0-openjdk.x86_64
   
     
     -check: java -version
   
     
     -Logstash Installation:
     
      rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
   
      
      Add the following in your /etc/yum.repos.d/ directory in a file with a .repo suffix, for example logstash.repo
   
     
      [logstash-5.x]
      name=Elastic repository for 5.x packages
      baseurl=https://artifacts.elastic.co/packages/5.x/yum
      gpgcheck=1
      gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
      enabled=1
      autorefresh=1
      type=rpm-md
   
     
      -sudo yum install logstash 
      
      Elasticsearch Installation:
       
      -wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.3.noarch.rpm
       
      -sudo rpm -ivh elasticsearch-1.7.3.noarch.rpm
       
      -sudo systemctl enable elasticsearch.service
       
      JDBC plugin:
       
      
  If all is OK, when we run : curl -XGET 'http://localhost:9200' we will se:
  
      `{
        "name" : "node-1",
        "cluster_name" : "my-application",
        "cluster_uuid" : "quaRDS_WSW2qP1LmoV0ypw",
        "version" : {
          "number" : "5.3.2",
          "build_hash" : "3068195",
          "build_date" : "2017-04-24T16:15:59.481Z",
          "build_snapshot" : false,
          "lucene_version" : "6.4.2"
        },
        "tagline" : "You Know, for Search"
      }

  We have to mapping before adding data in Elasticsearch, if not the error: "Can't merge a non object mapping with an  object mapping" will happening. 

**2. Description:**

   We will use logstash in order to sync Mysql to ElasticSearch.

   The following blok diagram explains the role of JDBC, logstash to migrate data from Mysql to ElasticSearch server:
   
     
     https://qbox.io/img/blog/mysql-logstash1.png
  

   In order to sync data from Mysql server to ElasticSearch server, we need configure a logstash file. Here it is sync_mysql.conf.
   
   After that, run command:

    /usr/share/logstash/bin -f sync_mysql.conf

   and then:

    curl -XGET 'http://localhost:9200/lat_lon_hozo/_search?pretty'


   The result is below:

 `````{
  "took" : 5,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 1000000,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2077",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.707Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.34939956665039
          },
          "id" : 2077,
          "place" : "Dong Da",
          "title" : "tiep thi"
        }
      },
```      {````
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2079",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.707Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.35219955444336
          },
          "id" : 2079,
          "place" : "Bach Khoa",
          "title" : "IT"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2083",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.707Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.81400299072266,
            "lat" : 21.350400924682617
          },
          "id" : 2083,
          "place" : "Dong Da",
          "title" : "IT"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2087",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.708Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.35540008544922
          },
          "id" : 2087,
          "place" : "Hai Ba Trung",
          "title" : "tiep thi"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2088",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.708Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.81400299072266,
            "lat" : 21.347299575805664
          },
          "id" : 2088,
          "place" : "Hai Ba Trung",
          "title" : "tiep thi"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2102",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.708Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80500030517578,
            "lat" : 21.352500915527344
          },
          "id" : 2102,
          "place" : "Truong Chinh",
          "title" : "sua chua do dien"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2111",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.709Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.351699829101562
          },
          "id" : 2111,
          "place" : "Dong Da",
          "title" : "Boc vac"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2116",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.709Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80999755859375,
            "lat" : 21.351699829101562
          },
          "id" : 2116,
          "place" : "Hai Ba Trung",
          "title" : "Boc vac"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2123",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.712Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80899810791016,
            "lat" : 21.355300903320312
          },
          "id" : 2123,
          "place" : "My Dinh",
          "title" : "don nha"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        ``"_id" : "2127",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.712Z",
          "@version" : "1",``
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.350500106811523
          },
          "id" : 2127,
          "place" : "My Dinh",
          "title" : "tiep thi"
        }
      }
    ]
  }
}
`````


   **Search title gan nhat ban kinh 1km:**

     curl -XPOST 'http://localhost:9200/tasks/_search?pretty' -d '{

     "query": {
    "function_score": {
       "functions": [
           {
            "gauss": {
               "location": {
                  "scale": "1km",
                  "origin": [21.351699829101562, 105.80599975585938]
                            }
                      }
             }
          ]
     }
  }
}'`


   Outcome:


````{
  "took" : 1117,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 1000000,
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2077",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.707Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.34939956665039
          },
          "id" : 2077,
          "place" : "Dong Da",
          "title" : "tiep thi"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2079",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.707Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.35219955444336
          },
          "id" : 2079,
          "place" : "Bach Khoa",
          "title" : "IT"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2083",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.707Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.81400299072266,
            "lat" : 21.350400924682617
          },
          "id" : 2083,
          "place" : "Dong Da",
          "title" : "IT"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2087",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.708Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.35540008544922
          },
          "id" : 2087,
          "place" : "Hai Ba Trung",
          "title" : "tiep thi"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2088",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.708Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.81400299072266,
            "lat" : 21.347299575805664
          },
          "id" : 2088,
          "place" : "Hai Ba Trung",
          "title" : "tiep thi"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2102",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.708Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80500030517578,
            "lat" : 21.352500915527344
          },
          "id" : 2102,
          "place" : "Truong Chinh",
          "title" : "sua chua do dien"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2111",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.709Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.351699829101562
          },
          "id" : 2111,
          "place" : "Dong Da",
          "title" : "Boc vac"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2116",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.709Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80999755859375,
            "lat" : 21.351699829101562
          },
          "id" : 2116,
          "place" : "Hai Ba Trung",
          "title" : "Boc vac"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2123",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.712Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80899810791016,
            "lat" : 21.355300903320312
          },
          "id" : 2123,
          "place" : "My Dinh",
          "title" : "don nha"
        }
      },
      {
        "_index" : "tasks",
        "_type" : "task",
        "_id" : "2127",
        "_score" : 0.0,
        "_source" : {
          "@timestamp" : "2017-05-11T09:14:06.712Z",
          "@version" : "1",
          "location" : {
            "lon" : 105.80799865722656,
            "lat" : 21.350500106811523
          },
          "id" : 2127,
          "place" : "My Dinh",
          "title" : "tiep thi"
        }
      }
    ]
  }
```````
