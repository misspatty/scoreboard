from google.appengine.ext import webapp2
class User(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('A post occured')
    
    def get(self):
        self.response.out.write('<html><body><h1><b>Login/Registration Page</b></h1></body></html>')
    
        self.response.out.write(""" <script>function validateForm(){
                var i = document.forms["log"]["username/email"]["password"].value;
                if(i == ""){
                    alert("Username or Password must be filled out)
                    return false;
                }
                }
            </script>
            <div class = "Login/Registration">
                <form name="log" action="login.php" method="post"
                <b>Username/Email:</b><br>
                <input type="text", "email" name="username/email"><br>
                <b>Password:</b><br>
                <input type="password" name="password"><br>
                <input type="submit" value="Submit">
                </form>
            </div>

            <h2>Registration</h2>
            <div class = "Login/Registration">
                <form name="regist" action="login.php" method="post">
                <b>Full Name:</b><br>
                <input type="text" name="fullname" required><br>
                <b>Email:</b><br>
                <input type="email" name="email" required><br>
                <b>Date of Birth:</b><br>
                <input type="date" name="dob" required><br>
                <b>Username:</b><br>
                <input type="text" name="username" required><br>
                <b>Password:</b><br>
                <input type="password" name="password" minlength="8" required><br>
                <input type="submit" value="Submit">
            </div>""")
    app = webapp2.WSGIApplication([('/', Home),
                                   ("/User", User),
                                   ('/Categories', Categories)], debug = True)    