
library(readxl)
indigent_burials_EDIT <- read_excel("~/GitHub/indigent-burials/PolyaVerVla - 10212022/indigent-burials EDIT.xlsx", 
                                    col_types = c("numeric", "text", "text", 
                                                  "text", "text", "text", "numeric", 
                                                  "numeric", "numeric", "numeric", 
                                                  "numeric", "numeric", "numeric", 
                                                  "numeric", "numeric", "numeric", 
                                                  "numeric", "numeric", "numeric", 
                                                  "numeric", "numeric", "numeric", 
                                                  "text", "text", "text", "text", "text", 
                                                  "text", "text", "text", "text", "numeric", 
                                                  "numeric", "text", "text", "text", 
                                                  "numeric", "numeric", "text"))
View(indigent_burials_EDIT)




indigent_burials_5 <- indigent_burials_EDIT[,-c(1)]



names(indigent_burials_5)[22] <- c("J")

categories <- unique(indigent_burials_5$J)
veiw <- categories

sort(categories(df$J), decreasing = TRUE)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Fresno, CA","Fresno, California", indigent_burials_5$J)
indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Dona Ana, NM", "Dona Ana, New Mexico", indigent_burials_5$J)
indigent_burials_5$J <- ifelse(indigent_burials_5$J == "King County", "King County, Washington", indigent_burials_5$J)
indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Yakima County", "Yakima County, Washington", indigent_burials_5$J)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Hart Island", "Hart Island, Bronx County, New York", indigent_burials_5$J)

categories1 <- unique(indigent_burials_5$J)
veiw <- categories1

categories1<-as.data.frame(categories1)

















