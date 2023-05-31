import io
import os
import csv
import json
import boto3
import urllib.parse

s3 = boto3.client('s3')

def get_books_handler(event, context):

    status_code, books_data = read_s3_data()
    response = format_response(status_code, books_data)

    return response

def get_books_by_id_handler(event, context):

    book_id = urllib.parse.unquote(event['pathParameters']['book_id'])
    status_code, books_data = read_s3_data(book_id)
    response = format_response(status_code, books_data)

    return response

def read_s3_data(book_id=None):

    csv_file = s3.get_object(Bucket=os.environ['S3_BUCKET_NAME'], Key=os.environ['S3_BUCKET_KEY'])

    csv_response = csv_file['Body'].read()
    stream = io.StringIO(csv_response.decode('utf-8-sig'))
    reader = csv.DictReader(stream)

    book_list = []
    for row in reader:
        # Check if no book_id has been passed, or if an book_id has been passed and is equal to the row's id
        if book_id is None or row['book_id'] == book_id:
            book_list.append(row)
    # If no book_id was passed, return the entire list
    if book_id is None:
        return 200, book_list
    else:
        # If only one book in book_list, a book_id was passed and the given book was found
        if len(book_list) == 1:
            return 200, book_list[0]
        else:
            # If book_id was passed and the book_list does not contain exactly one book, something went wrong    
            error_message = {"error":"Book not found."}
            return 404, error_message

def format_response(status_code, response_body):
    return {
        'statusCode': status_code,
        'headers': {
            'Access-Control-Allow-Methods': 'GET,OPTIONS',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(response_body)
    }