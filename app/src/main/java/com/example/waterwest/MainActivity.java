package com.example.waterwest;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import exportkit.figma.R;

public class MainActivity extends AppCompatActivity {
    Button LitersBtn, AlertBtn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        AlertBtn = findViewById(R.id.AlertBtn);
        AlertBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent intent = new Intent(MainActivity.this,AlertActivity.class);
                startActivity(intent);
            }
        });

        LitersBtn = findViewById(R.id.LitersBtn);
        LitersBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent intent = new Intent(MainActivity.this,WaterUsageActivity.class);
                startActivity(intent);
            }
        });
    }
}