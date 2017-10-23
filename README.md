# Log_Analysis

# __How To Install:__

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2. Download or Clone [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm).
4. Unzip the downloaded file to get __newsdata.sql__.
5. Copy the newsdata.sql file and put it into the same location as __vagrant directory__

# __How To Run:__

1. Launching the Virtual Machine in your computer's command promt:
2. Change directory to __vagrant directory__
3. Launch the Vagrant VM:```$ vagrant up``` 
4. Then Log into VM by using command:```$ vagrant ssh``` 
5. Change directory using ```cd /vagrant```

# Setting up the database and Creating Views:

* Load the data in local database using the command:

  ```psql -d news -f newsdata.sql```
  
* Use ```psql -d news``` to connect to database.

__Create Summary table that has author, title and total views of each article__

```CREATE VIEW Summary AS
SELECT author, title, count (*) as Views
FROM articles, log
WHERE log.path LIKE concat ('%', articles.slug)
GROUP BY articles.title, articles.author
ORDER BY Views DESC;
```


__Create Popular_author table to get all the views on all of the articles of each author__

```CREATE VIEW Popular_Author AS
SELECT Summary.author, SUM(Summary.Views) AS Total_Views
FROM Summary
GROUP BY Summary.author
ORDER BY Total_Views DESC;
```

__Create Access_Summary_By_Date table to get number of errors and number of requests by date__

```CREATE VIEW Access_Summary_By_Date AS 
SELECT  CAST(log.time AS Date) AS Date_Request,
    SUM((CASE WHEN log.status='404 NOT FOUND' then 1
         ELSE 0 END)) AS Total_Errors,
        COUNT(*) AS Total_Requests
FROM log
GROUP BY Date_Request;
```
# See Result:
Make sure you have changed the directory inside **vagrant**

Run ```python log_analysis.py```


