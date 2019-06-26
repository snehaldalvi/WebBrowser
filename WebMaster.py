import webbrowser

sm_list=["facebook","twitter","instagram","youtube"]
se_list=["google","yahoo","bing","duckduckgo"]
forum_list=["quora","medium"]

def facebook(a): 
    b="https://www.facebook.com/"+a
    return b

def twitter(a):
    b="https://twitter.com/search?q="+a
    return b

def instagram(a):
    b="https://www.instagram.com/"+a
    return b

def quora(a):
    b="https://www.quora.com/search?q="+a
    return b

def google(a):
    b="https://www.google.co.in/search?q="+a
    return b

def wikipedia(a):
    b="https://en.wikipedia.org/wiki/"+a
    return b

def duckduckgo(a):
    b="https://duckduckgo.com/?q="+a
    return b

def medium(a):
    b="https://medium.com/search?q="+a
    return b

def yahoo(a):
    b="https://in.search.yahoo.com/search?p="+a
    return b

def youtube(a):
    b="https://www.youtube.com/results?search_query="+a
    return b

def other(a,b):
    c="https://www.google.co.in/search?q="+a+" "+b
    return c

def socialMedia():
	print("""
		* Facebook
		* Twitter 
		* Instagram
		* YouTube""")

	value=input("Enter your choice: ") #Ask for user choice
    
	if value.lower()==sm_list[0]:  	#match with Facebook
		search=input("Enter Faceboook username: ")
		url=facebook(search)		#call facebook() 
		return url
    
	elif value.lower()==sm_list[1]:
		search=input("Enter Twitter username: ")
		url=twitter(search)
		return url
    
	elif value.lower()==sm_list[2]:
		search=input("Enter Instagram username: ")
		url=instagram(search)
		return url
   
	elif value.lower()==sm_list[3]:
		search=input("What you want to search : ")
		url=youtube(search)
		return url
		
	else:									#not matched
        #asked for Social Media Username
		search=input("Enter "+" "+ value +" "+ "username: ") 
		url=other(value,search)			#call other()
		return url

def searchEngine():
	search=input("What you want to search?? ")
	print("""
		* DuckDuckGo
		* Google
		* Yahoo
		* Bing""") 

	value=input("Enter your choice: ") 	#Ask for user choice
	
	if value.lower()==se_list[0]:		#matched with Google
		url=google(search)				#call Google
		return url
    
	elif value.lower()==se_list[1]:
		url=yahoo(search)
		return url
    
	elif value.lower()==se_list[2]:
		url=bing(search)
		return url
    
	elif value.lower()==se_list[3]:
		url=duckduckgo(search)
		return url
		
	else:
		url=other(search,value)
		return url

def forums():
	search=input("Enter Question: ")
	
	print("""
		* Quora
		* Medium""") 
	value=input("Enter your choice: ") #asked for user choice
	   
	if value.lower()==forum_list[0]:
		url=quora(search)
		return url
    
	elif value.lower()==forum_list[1]:
		url=medium(search)
		return url
    
	else:
		url=other(search,value)
		return url	

def browser():
    flag=True		#initially flag set to True
    while(flag!=False):	#execute while block till flag set to False
        print("""
        1. Social Media
        2. Search?
        3. Ask Question""")
        choice=(input("Enter Your Choice, (1/2/3): ")) #asked for user choice
        #matched with socialMedia 
        if int(choice) == 1: 
            #call socialMedia and stored return value in url
            url=socialMedia()
            #open new tab in browser with passed url
            webbrowser.open_new(url)
        elif int(choice) == 2:			
            url=searchEngine()
            webbrowser.open_new(url)
        elif int(choice) == 3:
            url=forums()
            webbrowser.open_new(url)
        else:
            print("Give correct input!!")	
				
        op=input("Continue (y/n): ")	#if user wants to search again.

        if op.lower() == 'y':
            flag == True
        else:
            print("Good Bye!")
            exit()	
browser()				#code terminated.
