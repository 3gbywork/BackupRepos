import urllib.request
import base64
import json
import io
import os
import sys

# personal public access token
USER=''
TOKEN=''
GIT_API_URL='https://api.github.com'

def main(argv):
    if len(argv) > 1:
        user=argv[1]
    else:
        user=input("enter username: ").strip()
        if not user:
            print("username can't be null")
            sys.exit(1)
    
    print("\n================================")
    print("list public repos for the user: %s" % user)
    repos=getRepos(user)
    for name,url in repos:
        print("name: %-30s url: %s" % (name,url))
    print("================================\n")

    input("press enter to clone or update all repos...")
    cloneOrUpdateRepos(repos)

def cloneOrUpdateRepos(repos):
    for name,url in repos:
        print("\n================================")
        if os.path.exists(name):
            print("repo: %s has exists, will update" % name)
            os.system("cd %s & git pull" % name)
        else:
            print("repo: %s not exists, will clone" % name)
            os.system("git clone %s" % url)
        print("================================\n")

def getRepos(user):
    resp = getApi('/users/%s/repos' % user)
    return [(x["name"],x["clone_url"]) for x in json.load(io.StringIO(resp))]

def getApi(url):
    try:
        req=urllib.request.Request(GIT_API_URL+url)
        if USER and TOKEN:
            print("authorization with %s-%s" % (USER, TOKEN))
            b64str=base64.encodestring(bytes('%s/token:%s' % (USER, TOKEN), 'utf-8')).decode('utf-8').replace('\n', '')
            req.add_header("Authorization", "Basic %s" % b64str)
        resp=urllib.request.urlopen(req)
        cnt=resp.read().decode('utf-8')
        resp.close()
        return cnt
    except:
        print('failed to get api request from %s' % url)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        sys.exit(2)        