library(rtweet)

# Accessing Twitter APIs require these keys and tokens
consumer_key <- "z1BD0Ve29tjorbsAhww9cptHh"
consumer_secret <- "MabrL9Fj2an40weqifg9e1hYtLLyHStzMYuK8ijc2WluiSjdMX"
access_token <- "1095681775098048512-UVirSgwpToXdBB25V6lLnEUKpk7t3x"
access_secret <- "Zj8BamGbYQaGQjsUO4Oi7in9vsaVBgARqf1BeEIofONeV"

# Sends request to generate OAuth 1.0 tokens
create_token(
  app = "MapR",
  consumer_key = consumer_key,
  consumer_secret = consumer_secret,
  access_token = access_token,
  access_secret = access_secret)

#keywords <- "Mueller probe OR Mueller investigation OR Russia investigation"

#keywords <- "Trump campaign OR 2020Election OR president campaign"

#keywords <- "fox news OR foxnews"

#keywords <- "Democrats"

keywords <- "pete buttigieg"

## search for tweets sent from the US
rt <- search_tweets(keywords, include_rts = FALSE, 
                    retryonratelimit = TRUE,
                    geocode = lookup_coords("usa"),
                    n = 30000)

# saving all the tweets data into a csv file
write_as_csv(rt, "full_data_topic5.csv" , prepend_ids = TRUE, na = "", fileEncoding = "UTF-8")

# remove duplicate tweets
rt_dup <- duplicated(rt$text)
rt_unique <- rt[!rt_dup,]

# saving all the tweets data into a csv file
save_as_csv(rt_unique, paste("unique_data_topic5.csv"), prepend_ids = TRUE, na = "",
            fileEncoding = "UTF-8")

data_tweet <- read.csv(file = 'unique_data_topic5.csv')
data_tweet <- rt_unique[,c("text")]
write.table(data_tweet, file = "data_topic5.csv", sep=",",  col.names=FALSE, row.names = FALSE)
