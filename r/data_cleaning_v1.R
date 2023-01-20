


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


indigent_burials_5$GeoCoding <- indigent_burials_5$J 



colnames(indigent_burials_5) 


categories2 <- unique(indigent_burials_5$State)
veiw <- categories2
categories2<-as.data.frame(categories2)


indigent_burials_5$State <- ifelse(indigent_burials_5$State == "-99", " ", indigent_burials_5$State)


categories3 <- unique(indigent_burials_5$County)
veiw <- categories3
categories3<-as.data.frame(categories3)

indigent_burials_5$County <- paste0(indigent_burials_5$County, " County")

indigent_burials_5$County <- ifelse(indigent_burials_5$County == "-9 County", " ", indigent_burials_5$County)

indigent_burials_5$County  <- ifelse(indigent_burials_5$County == "-- County", " ", indigent_burials_5$County)

indigent_burials_5$County <- ifelse(indigent_burials_5$County == "Unknown County", " ", indigent_burials_5$County)


indigent_burials_5$date <- paste(indigent_burials_5$State, indigent_burials_5$County, sep=", ")

categories3 <- unique(indigent_burials_5$County)
veiw <- categories3
categories3<-as.data.frame(categories3)


categories4 <- unique(indigent_burials_5$date)
veiw <- categories4
categories4<-as.data.frame(categories4)


indigent_burials_5$date <- ifelse(indigent_burials_5$date == ", ", " ", indigent_burials_5$date)

indigent_burials_5$date <- ifelse(indigent_burials_5$date == ", Bernalillo County", "Bernalillo County", indigent_burials_5$date)

indigent_burials_5$date <- ifelse(indigent_burials_5$date == ", NM County Outside of Bernalillo County", "NM County Outside of Bernalillo County", indigent_burials_5$date)



indigent_burials_5$GeoCoding <- indigent_burials_5$date


categories5 <- unique(indigent_burials_5$GeoCoding)
veiw <- categories5
categories5<-as.data.frame(categories5)









