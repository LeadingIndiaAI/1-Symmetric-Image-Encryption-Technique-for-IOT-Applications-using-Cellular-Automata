package com.example.image_upload;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.net.Uri;
import android.provider.MediaStore;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBar;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;
import android.graphics.BitmapFactory;


import com.google.android.gms.tasks.Continuation;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.FirebaseApp;
import com.google.firebase.storage.FileDownloadTask;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.ListResult;
import com.google.firebase.storage.OnPausedListener;
import com.google.firebase.storage.OnProgressListener;
import com.google.firebase.storage.StorageException;
import com.google.firebase.storage.StorageMetadata;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.UploadTask;

import java.io.IOException;
import java.util.UUID;

public class MainActivity extends AppCompatActivity {

    // views for button
    private Button btnSelect, btnUpload,btndownload,btndecrypt;
    ProgressDialog prgDialog;
    // view for image view
    private ImageView imageView;

    // Uri indicates, where the image will be picked from
    private Uri filePath;

    // request code
    private final int PICK_IMAGE_REQUEST = 22;

    // instance for firebase storage and StorageReference
    FirebaseStorage storage = FirebaseStorage.getInstance();
    StorageReference storageRef = storage.getReference();

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ActionBar actionBar = getSupportActionBar();
        actionBar.hide();
        //ActionBar actionBar = getSupportActionBar();
        //ColorDrawable colorDrawable
         //       = new ColorDrawable(
         //       Color.parseColor("#0F9D58"));
        //actionBar.setBackgroundDrawable(colorDrawable);

        // initialise views
        btnSelect = findViewById(R.id.btnChoose);
        btnUpload = findViewById(R.id.btnUpload);
        imageView = findViewById(R.id.imgView);
        btndownload = findViewById(R.id.buttonPicture);
        btndecrypt= findViewById(R.id.encPicture);
        // get the Firebase storage reference
        //storage = FirebaseStorage.getInstance();
        //storageReference = storage.getReference();

        // on pressing btnSelect SelectImage() is called

       btnSelect.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v)
            {
               SelectImage();
           }
        });

        // on pressing btnUpload uploadImage() is called
       btnUpload.setOnClickListener(new View.OnClickListener() {
            @Override
           public void onClick(View v)
           {
                uploadImage();
            }
       });

        btndownload.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v)
            {
                downloadImage();
            }
        });
        btndecrypt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v)
            {
                downloadImage2();
            }
        });
    }

    // Select Image method
    private void SelectImage()
    {

        // Defining Implicit Intent to mobile gallery
        Intent intent = new Intent();
        intent.setType("image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        startActivityForResult(
                Intent.createChooser(
                        intent,
                        "Select Image from here..."),
                PICK_IMAGE_REQUEST);
    }

    // Override onActivityResult method
    @Override
    protected void onActivityResult(int requestCode,
                                    int resultCode,
                                    Intent data)
    {

        super.onActivityResult(requestCode,
                resultCode,
                data);

        // checking request code and result code
        // if request code is PICK_IMAGE_REQUEST and
        // resultCode is RESULT_OK
        // then set image in the image view
        if (requestCode == PICK_IMAGE_REQUEST
                && resultCode == RESULT_OK
                && data != null
                && data.getData() != null) {

            // Get the Uri of data
            filePath = data.getData();
            try {

                // Setting image on image view using Bitmap
                Bitmap bitmap = MediaStore
                        .Images
                        .Media
                        .getBitmap(
                                getContentResolver(),
                                filePath);
                imageView.setImageBitmap(bitmap);
            }

            catch (IOException e) {
                // Log the exception
                e.printStackTrace();
            }
        }
    }

    // UploadImage method
    private void uploadImage()
    {
        if (filePath != null) {

            // Code for showing progressDialog while uploading
            final ProgressDialog progressDialog = new ProgressDialog(this);
            progressDialog.setTitle("Uploading...");
            progressDialog.show();
            //prgDialog.setMessage("Uploading...");


            // Defining the child of storageReference
            StorageReference ref = storageRef.child("images/" + UUID.randomUUID().toString());

            //prgDialog.setMessage("djihuh...");
            // adding listeners on upload
            // or failure of image
            ref.putFile(filePath).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
                                @Override
                                public void onSuccess(
                                        UploadTask.TaskSnapshot taskSnapshot)
                                {
                                   // prgDialog.setMessage("dismiss...");
                                    progressDialog.dismiss();
                                    Toast.makeText(MainActivity.this,
                                                    "Image Uploaded!!",
                                                    Toast.LENGTH_SHORT).show();
                                }
                            })

                    .addOnFailureListener(new OnFailureListener() {
                        @Override
                        public void onFailure(@NonNull Exception e)
                        {

                            // Error, Image not uploaded
                            progressDialog.dismiss();
                            Toast
                                    .makeText(MainActivity.this,
                                            "Failed " + e.getMessage(),
                                            Toast.LENGTH_SHORT)
                                    .show();
                        }
                    })
                    .addOnProgressListener(
                            new OnProgressListener<UploadTask.TaskSnapshot>() {

                                // Progress Listener for loading
                                // percentage on the dialog box
                                @Override
                                public void onProgress(
                                        UploadTask.TaskSnapshot taskSnapshot)
                                {
                                    double progress
                                            = (100.0
                                            * taskSnapshot.getBytesTransferred()
                                            / taskSnapshot.getTotalByteCount());
                                    progressDialog.setMessage(
                                            "Uploaded "
                                                    + (int)progress + "%");
                                }
                            });
        }
    }

    private void downloadImage()
    {
        final ProgressDialog progDialog = new ProgressDialog(this);
        progDialog.setTitle("Encrypting...");
        progDialog.show();
        // Create a storage reference from our app
        StorageReference storageRef = storage.getReference();

// Or Create a reference to a file from a Google Cloud Storage URI
        StorageReference gsReference =
                storage.getReferenceFromUrl("gs://image-uploading-cca33.appspot.com/images/test_5.jpg");


        /*In this case we'll use this kind of reference*/
//Download file in Memory
        StorageReference islandRef = storageRef.child("images/test_5.jpg");

        final long ONE_MEGABYTE = 1024 * 1024;
        islandRef.getBytes(ONE_MEGABYTE).addOnSuccessListener(new OnSuccessListener<byte[]>() {
                                                                          @Override
                                                                          public void onSuccess(byte[] bytes) {
                                                                              // Data for "images/island.jpg" is returns, use this as needed
                                                                              Bitmap bitmap = BitmapFactory.decodeByteArray(bytes, 0, bytes.length);
                                                                              imageView.setImageBitmap(bitmap);
                                                                              progDialog.dismiss();
                                                                              Toast.makeText(MainActivity.this,
                                                                                      "Image Encrypted!!",
                                                                                      Toast.LENGTH_SHORT).show();
                                                                          }
                                                                      }).addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                // Handle any errors
                // Error, Image not uploaded
                progDialog.dismiss();
                Toast
                        .makeText(MainActivity.this,
                                "Failed " + e.getMessage(),
                                Toast.LENGTH_SHORT)
                        .show();

            }
        });
    }

    private void downloadImage2()
    {
        final ProgressDialog progDialog = new ProgressDialog(this);
        progDialog.setTitle("Decrypting...");
        progDialog.show();
        // Create a storage reference from our app
        StorageReference storageRef = storage.getReference();

// Or Create a reference to a file from a Google Cloud Storage URI
        StorageReference gsReference =
                storage.getReferenceFromUrl("gs://image-uploading-cca33.appspot.com/images/test_5_result.png");


        /*In this case we'll use this kind of reference*/
//Download file in Memory
        StorageReference islandRef = storageRef.child("images/test_5_result.png");

        final long ONE_MEGABYTE = 1024 * 1024;
        islandRef.getBytes(ONE_MEGABYTE).addOnSuccessListener(new OnSuccessListener<byte[]>() {
            @Override
            public void onSuccess(byte[] bytes) {
                // Data for "images/island.jpg" is returns, use this as needed
                Bitmap bitmap = BitmapFactory.decodeByteArray(bytes, 0, bytes.length);
                imageView.setImageBitmap(bitmap);
                progDialog.dismiss();
                Toast.makeText(MainActivity.this,
                        "Image Decrypted!!",
                        Toast.LENGTH_SHORT).show();
            }
        }).addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                // Handle any errors
                // Error, Image not uploaded
                progDialog.dismiss();
                Toast
                        .makeText(MainActivity.this,
                                "Failed " + e.getMessage(),
                                Toast.LENGTH_SHORT)
                        .show();

            }
        });
    }
}
