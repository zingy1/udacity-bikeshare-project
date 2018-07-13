
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np
from datetime import datetime as dt


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[3]:


MONTHS = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6, 'all': 'all'}


# In[4]:


DAYS= {"mon" : 1, "tue" :2, "wed" : 3, "thur" :4, "friday": 5, "sat" :6, "sun": 7, 'all':[1,2,3,4,5,6,7]}


# In[5]:


def get_raw_data():
    chicago_df=pd.read_csv("chicago.csv")
    new_york_city_df=pd.read_csv("new_york_city.csv")
    washington_df=pd.read_csv("washington.csv")

    chicago=input("Do you want to see chicago raw data ? type either yes or no :").lower()
    if chicago =="yes":
        print(chicago_df.head(5))
    elif chicago=="no":
        print("check next city")

    new_york_city=input("Do you want to see new york city raw data ? type either yes or no :").lower()
    if new_york_city =="yes":
        print(new_york_city_df.head(5))
    elif new_york_city=="no":
        print("check next city")

    washington=input("Do you want to see washington raw data ? type either yes or no :").lower()
    if washington =="yes":
        print(washington_df.head())
    elif new_york_city=="no":
        print("Let us explore more")
    return 


# In[6]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            
    city = ""
    while city.lower() not in CITY_DATA.keys():
        city= input("which city do you want to explore? : Chicago, New York or Washington:")
    
        if city.lower() in CITY_DATA.keys():
            city = city.lower()
    
        else:
            print ("City not included. state whether Chicago, New York or washington")


    # get user input for month (all, january, february, ... , june)
            
    month="" 
        
    while month.lower() not in MONTHS.keys():
        month = input('Which month would you like to explore? Options are All, January, February, March, April, May or June)')
        
        if month.lower() in MONTHS.keys():
            month = month.lower()
        
        else:
            print ("Month not included. Please try :january, february, march, april, may, june")
            
    day = ""
    while day.lower() not in DAYS.keys():
        day = input(' which day of  the week day you want to analyze?'' You can type \'all\' again to apply no day filter. \n(e.g. Mon, Tue, Wed, Thur, Friday, Sat, Sun:) \n> ')
    
        if day.lower() in DAYS.keys():
            day = day.lower()
        
        else:
            print ("Day  not included. Please try : Mon, Tue, Wed, Thur, Friday, Sat, Sun")

    print('-'*40)
    return city, month, day


# In[7]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour  
    df["End Time"]=pd.to_datetime(df["End Time"])
    df["month"] = df["End Time"].dt.month
    df["day_of_week"] = df["End Time"].dt.weekday_name
    df["hour"] = df["End Time"].dt.hour
     # filter by month if applicable
    if month != 'all':
        month =  list(MONTHS.index()).index(month) +1 
        df= df[df['month'] == month ]
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]


    return df


# In[8]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The highest  common of the month is :", most_common_month)


    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The highest common day of the  week is :", most_common_day_of_week)


    # display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    The_most_commonly_used_start_station= df["Start Station"].value_counts().reset_index['index'][0]
    print ("The most commonly used station in your city is ", The_most_commonly_used_start_station)
    
    # display most commonly used end station
    
    The_most_commonly_used_end_station= df["End Station"].value_counts().reset_index['index'][0]
    print ("The most commonly used station in your city is ", The_most_commonly_used_end_station)
    # display most frequent combination of start station and end station trip
    The_most_frequent_start_end_station_trip= df.groupy(["Start Station", "End Station"]).mode()
    print("The most frequent Start Station is {} while the most frequent End station is {} ".format(The_most_commonly_used_start_station[0],The_most_commonly_used_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[10]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_travel_time= df["Trip Duration"].sum()
    print ("Total duration time covered is ", Total_travel_time)

    # display mean travel time
    Mean_travel_time= df["Trip Duration"].mean()
    print ("The average mean for the travel time is ", Mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[11]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    User_counts=df["User Type"].value_counts()
    # Display counts of gender
 
 
    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[12]:


def get_user_gender(df):
    # Display counts of gender
    if 'Gender' in df.columns:
        user_stats_gender(df)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


# In[13]:


def get_user_birth(df):
    # Display counts of birth
    if 'Birth Year' in df.columns:
        user_stats_birth(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[14]:


def main():
    
    while True:
        get_raw_data()
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_user_gender(df)
        get_user_birth(df)
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

