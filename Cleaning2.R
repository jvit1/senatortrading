setwd('C:/Users/student/Documents/UVA/Portfolio Projects/Senator Trading/senatortrading/')
data <- read.csv('CongressInvestments2.csv')

#Fixing Name Column
data$Name <- gsub("The Honorable", "", data$Name)
data$Name <- gsub("Mrs.", "", data$Name)
data$Name <- gsub("Ms.", "", data$Name)
data$Name <- gsub("Mr.", "", data$Name)
data$Name <- gsub("\\s*\\([^\\)]+\\)","",data$Name) #Getting rid of repeated name in parenthesis
