# Elasticsearch_Mysql

We will use logstash in order to sync Mysql to ElasticSearch.

The following blok diagram explains the role of JDBC connector plugin in mygrating data from a JDBC supported database:
https://qbox.io/img/blog/mysql-logstash1.png


run the command: 

/usr/share/logstash/bin -f sync_mysql.conf

and then:

curl -XGET 'http://localhost:9200/lat_lon_hozo/_search?pretty'
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


