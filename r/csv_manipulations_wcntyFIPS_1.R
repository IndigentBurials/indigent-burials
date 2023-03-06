data_loc <- ("C:/Users/visot/OneDrive/Documents/GitHub/indigent-burials/python/data")
setwd(data_loc)
getwd()
require(data.table)

indigent_burials_5 <- fread("indigent_burials_main.csv", 
          stringsAsFactors = F, 
          data.table = F,
          colClasses=list(character=c(1)))

veiw <- indigent_burials_5




names(indigent_burials_5)[7] <- c("J")

indigent_burials_EDIT$CntyFIPS <- indigent_burials_5$J 

categories <- unique(indigent_burials_5$J)
veiw <- categories
categories<-as.data.frame(categories)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Fresno, CA","Fresno County, California", indigent_burials_5$J)
indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Dona Ana, NM", "Dona Ana County, New Mexico", indigent_burials_5$J)
indigent_burials_5$J <- ifelse(indigent_burials_5$J == "King County", "King County, Washington", indigent_burials_5$J)
indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Yakima County", "Yakima County, Washington", indigent_burials_5$J)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Hart Island", "Hart Island, Bronx County, New York", indigent_burials_5$J)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Chicago, Cook County", "Cook County, Chicago, Illinois", indigent_burials_5$J)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Riverside County", "Riverside County, Montana", indigent_burials_5$J)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Orange County", "Orange County, California", indigent_burials_5$J)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Pima County", "Pima County, Arizona", indigent_burials_5$J)

indigent_burials_5$J <- ifelse(indigent_burials_5$J == "Bernalill0", "Bernalillo County, New Mexico", indigent_burials_5$J)






categories1 <- unique(indigent_burials_5$J)
veiw <- categories1

categories1<-as.data.frame(categories1)


indigent_burials_5$GeoCoding <- indigent_burials_5$J 

categories2 <- unique(indigent_burials_5$County)
veiw <- categories2

categories2<-as.data.frame(categories2)

indigent_burials_5$County <- paste0(indigent_burials_5$County, " County")



indigent_burials_5$County  <- ifelse(indigent_burials_5$County == "-- County", " ", indigent_burials_5$County)

indigent_burials_5$County  <- ifelse(indigent_burials_5$County == " County", " ", indigent_burials_5$County)


categories2 <- unique(indigent_burials_5$County)
veiw <- categories2

categories2<-as.data.frame(categories2)


categories3 <- unique(indigent_burials_5$State)
veiw <- categories3
categories3<-as.data.frame(categories3)

indigent_burials_5$data <- paste(indigent_burials_5$County, indigent_burials_5$State, sep=", ")

categories4 <- unique(indigent_burials_5$data)
veiw <- categories4
categories4<-as.data.frame(categories4)

categories5 <- unique(indigent_burials_5$GeoCoding)
veiw <- categories5
categories5<-as.data.frame(categories5)


indigent_burials_5$GeoCoding[indigent_burials_5$GeoCoding == 'Dignity Memorial'] <- indigent_burials_5$data

indigent_burials_5$GeoCoding[indigent_burials_5$GeoCoding == 'Bernalill0'] <- indigent_burials_5$data

indigent_burials_5$GeoCoding[indigent_burials_5$GeoCoding == 'National Missing and Unidentified Persons System'] <- indigent_burials_5$data
indigent_burials_5

categories5 <- unique(indigent_burials_5$GeoCoding)
veiw <- categories5
categories5<-as.data.frame(categories5)

indigent_burials_5$GeoCoding  <- ifelse(indigent_burials_5$GeoCoding == "Los Angeles, California", "Los Angeles County, California", 
                                        indigent_burials_5$GeoCoding)

categories5 <- unique(indigent_burials_5$GeoCoding)
veiw <- categories5
categories5<-as.data.frame(categories5)

#indigent_burials_5$GeoCoding[indigent_burials_5$GeoCoding == 'Oregon'] <- indigent_burials_5$data
#indigent_burials_5$GeoCoding[indigent_burials_5$GeoCoding == 'Oakland'] <- indigent_burials_5$data
#indigent_burials_5

#categories6 <- unique(indigent_burials_5$GeoCoding)
#veiw <- categories6
#categories6<-as.data.frame(categories6)


data_loc <- ("C:/Users/visot/OneDrive/Documents/GitHub/indigent-burials/python/data")
setwd(data_loc)
getwd()
require(data.table)

FIPS <- fread("USA_Counties_formatching.csv", 
                            stringsAsFactors = F, 
                            data.table = F,
                            colClasses=list(character=c(1)))

veiw <- FIPS
  
  
FIPS$all <- paste(FIPS$NAME, FIPS$STATE_NAME, sep=", ")





#full_data <- merge(FIPS,
              #     indigent_burials_5,
              #     by.x="GeoCoding",
               #    by.y="all")
#fix it with One-to-Many Left Join / Merge in Data.Table in R!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

indigent_burials_5$CntyFips <- indigent_burials_5$GeoCoding

indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Cook County, Chicago, Illinois", "31", indigent_burials_5$CntyFips)

indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "King County, Washington", "33", indigent_burials_5$CntyFips)

indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Dona Ana County, New Mexico", "13", indigent_burials_5$CntyFips)
indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Fresno County, California", "19", indigent_burials_5$CntyFips)
indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Hart Island, Bronx County, New York", "5", indigent_burials_5$CntyFips)

indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Los Angeles County, California", "37", indigent_burials_5$CntyFips)

indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Yakima County, Washington", "77", indigent_burials_5$CntyFips)
indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Riverside County, Montana", "65", indigent_burials_5$CntyFips)

indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Orange County, California", "59", indigent_burials_5$CntyFips)

indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Pima County, Arizona", "19", indigent_burials_5$CntyFips)

indigent_burials_5$CntyFips  <- ifelse(indigent_burials_5$CntyFips == "Bernalillo County, New Mexico", "1", indigent_burials_5$CntyFips)


categories6 <- unique(indigent_burials_5$CntyFips)
veiw <- categories6
categories6<-as.data.frame(categories6)

