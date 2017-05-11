# Elasticsearch_Mysql

We will use logstash in order to sync Mysql to ElasticSearch.

The following blok diagram explains the role of JDBC connector plugin in mygrating data from a JDBC supported database:
https://qbox.io/img/blog/mysql-logstash1.png


run the command: 

/usr/share/logstash/bin -f sync_mysql.conf

and then:

curl -XGET 'http://localhost:9200/lat_lon_hozo/_search?pretty'


The result below:



{
  "took" : 58,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 905,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4lgf7sMJd61GBq3",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:21.869Z",
          "@version" : "1",
          "lon" : 105.80999755859375,
          "id" : 1476766,
          "lat" : 21.352699279785156
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4lgf7sMJd61GBq-",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:21.879Z",
          "@version" : "1",
          "lon" : 105.80999755859375,
          "id" : 1476773,
          "lat" : 21.355199813842773
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4lgf7sMJd61GBrG",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:21.887Z",
          "@version" : "1",
          "lon" : 105.80599975585938,
          "id" : 1476781,
          "lat" : 21.347700119018555
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4lgf7sMJd61GBrM",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:21.921Z",
          "@version" : "1",
          "lon" : 105.81099700927734,
          "id" : 1476787,
          "lat" : 21.354000091552734
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4lgf7sMJd61GBrW",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:21.928Z",
          "@version" : "1",
          "lon" : 105.80599975585938,
          "id" : 1476797,
          "lat" : 21.350099563598633
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4lgf7sMJd61GBrX",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:21.929Z",
          "@version" : "1",
          "lon" : 105.81099700927734,
          "id" : 1476798,
          "lat" : 21.345699310302734
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4lgf7sMJd61GBrZ",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:21.930Z",
          "@version" : "1",
          "lon" : 105.81099700927734,
          "id" : 1476800,
          "lat" : 21.347400665283203
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4lgf7sMJd61GBrl",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:21.957Z",
          "@version" : "1",
          "lon" : 105.80999755859375,
          "id" : 1476812,
          "lat" : 21.355100631713867
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4vsf7sMJd61GBrq",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:23.361Z",
          "@version" : "1",
          "lon" : 105.81400299072266,
          "id" : 1476817,
          "lat" : 21.34939956665039
        }
      },
      {
        "_index" : "lat_lon_hozo",
        "_type" : "data",
        "_id" : "AVvrZ4vsf7sMJd61GBrw",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2017-05-09T04:11:23.364Z",
          "@version" : "1",
          "lon" : 105.80999755859375,
          "id" : 1476823,
          "lat" : 21.353500366210938
        }
      }
    ]
  }
}

Search title gan nhat ban kinh 1km:

hieunc@elasticsearch-server Elasticsearch_Mysql]$ curl -XPOST 'http://localhost:9200/tasks/_search?pretty' -d '{
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
}'



Ket qua:


{
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

