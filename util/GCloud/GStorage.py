from google.cloud import storage


class Util():
    def create_bucket(self,bucket_name):
        """Creates a new bucket."""

        storage_client = storage.Client()
        storage_client.create_bucket(bucket_name)

    def list_blobs(self,bucket_name):
        """Lists all the blobs in the bucket."""

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blobs = bucket.list_blobs()
        return blobs

        # for blob in blobs:
        #     print(blob.name)

    def upload_blob(self,bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)

    def delete_blob(self,bucket_name, blob_name):
        """Deletes a blob from the bucket."""

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.delete()

    def delete_bucket(self,bucket_name):
        """Deletes a bucket. The bucket must be empty."""

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        bucket.delete()
        # print('Bucket {} deleted'.format(bucket.name))

    def blob_metadata(self,bucket_name, blob_name):
        """Prints out a blob's metadata."""

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.get_blob(blob_name)
        return blob.name

    # print('Blob: {}'.format(blob.name))
