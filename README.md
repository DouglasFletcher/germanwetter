# germanwetter
collect dwd weather

1. get weather data from public ftp server (ftp:dwd - deutsche Wetter Dienst)
2. download both weather and station metadata
3. extract to flatfile for import into staging process
4. staging suggestions: 
      i. merging weather data daily or weekly
      ii. adding metadata via SCD (slowly changing dimensions) star schema
      iii. dimensions: period, variable name, stationmeta
