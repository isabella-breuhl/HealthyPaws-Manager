from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3

# Define database file path
DB_FILE = 'healthypaws.db'

# HTTPRequestHandler class
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Serve the index.html file
            with open('HPM.html', 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path.startswith('/run_query/'):
            # Extract the query name from the URL path
            query_name = self.path.split('/')[-1]

            # Initialize database connection
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()

            # Execute the appropriate SQL query based on query_name
            if query_name == 'query21.sql':
                cursor.execute("SELECT FirstName, LastName, Phone, Name FROM Owner NATURAL JOIN Pet WHERE Owner.Username IN ( SELECT Username FROM Pet GROUP BY Username HAVING COUNT(*) == 1) ORDER BY LastName ASC")
            elif query_name == 'query22.sql':
                cursor.execute("SELECT Pet.Name, Appointment.Time, Appointment.Date FROM Pet JOIN Appointment WHERE Appointment.PetId == Pet.PetId AND Appointment.Date BETWEEN date('now') AND DATE('now', '+14 days') ORDER BY Appointment.Date, Appointment.Time")
            elif query_name == 'query23.sql':
                cursor.execute("SELECT Pet.Name, Pet.Birthday FROM Pet JOIN Record WHERE Record.PetId == Pet.PetId AND Pet.Birthday BETWEEN DATE('now') AND DATE('now', '+30 days') AND Record.Location == '3103 Aurora Road, Joy Washington' GROUP BY Pet.Name HAVING COUNT(*) > 1 ORDER BY Birthday ASC")
            # Add more elif blocks for other queries

            # Fetch and format the results
            results = cursor.fetchall()
            formatted_results = [dict(zip([col[0] for col in cursor.description], row)) for row in results]

            # Close database connection
            conn.close()

            # Send response with JSON data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(formatted_results).encode())

def run():
    print('Starting server...')

    # Server settings
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on port 8000')

    # Run server
    httpd.serve_forever()

if __name__ == '__main__':
    run()
