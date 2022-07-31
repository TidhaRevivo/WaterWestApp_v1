package com.example.waterwest;


import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import exportkit.figma.R;


public class AlertActivity extends AppCompatActivity {
    Button Home;
    private View _bg__alerts_ek2;
    private View rectangle_40;
    private View rectangle_39;
    private TextView alerts_ek3;
    private ImageView untitled_design__3__2;
    private View rectangle_37;
    private TextView water_is_running_low_;
    private TextView _16_7_22;
    private TextView resolved;
    private View rectangle_40_ek1;
    private TextView you_might_have_a_leak_;
    private TextView _19_7_22;
    private TextView resolved_ek1;
    private View rectangle_41;
    private TextView water_is_running_low__ek1;
    private TextView _22_7_22;
    private TextView resolved_ek2;
    private View rectangle_42;
    private TextView water_is_flowing_;
    private TextView just_now;
    private TextView active;
    private ImageView rectangle_42_ek1;
    private TextView log_out;
    private ImageView icon_ek1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.alert_activity);


        _bg__alerts_ek2 = (View) findViewById(R.id._bg__alerts_ek2);
        rectangle_40 = (View) findViewById(R.id.rectangle_40);
        rectangle_39 = (View) findViewById(R.id.rectangle_39);
        alerts_ek3 = (TextView) findViewById(R.id.alerts_ek3);
        untitled_design__3__2 = (ImageView) findViewById(R.id.untitled_design__3__2);
        rectangle_37 = (View) findViewById(R.id.rectangle_37);
        water_is_running_low_ = (TextView) findViewById(R.id.water_is_running_low_);
        _16_7_22 = (TextView) findViewById(R.id._16_7_22);
        resolved = (TextView) findViewById(R.id.resolved);
        rectangle_40_ek1 = (View) findViewById(R.id.rectangle_40_ek1);
        you_might_have_a_leak_ = (TextView) findViewById(R.id.you_might_have_a_leak_);
        _19_7_22 = (TextView) findViewById(R.id._19_7_22);
        resolved_ek1 = (TextView) findViewById(R.id.resolved_ek1);
        rectangle_41 = (View) findViewById(R.id.rectangle_41);
        water_is_running_low__ek1 = (TextView) findViewById(R.id.water_is_running_low__ek1);
        _22_7_22 = (TextView) findViewById(R.id._22_7_22);
        resolved_ek2 = (TextView) findViewById(R.id.resolved_ek2);
        rectangle_42 = (View) findViewById(R.id.rectangle_42);
        water_is_flowing_ = (TextView) findViewById(R.id.water_is_flowing_);
        just_now = (TextView) findViewById(R.id.just_now);
        active = (TextView) findViewById(R.id.active);
        rectangle_42_ek1 = (ImageView) findViewById(R.id.rectangle_42_ek1);
        log_out = (TextView) findViewById(R.id.log_out);
        icon_ek1 = (ImageView) findViewById(R.id.icon_ek1);


        //custom code goes here
        Home = findViewById(R.id.HomeBtn);
        Home.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent intent = new Intent(AlertActivity.this, MainActivity.class);
                startActivity(intent);
            }
        });



    }}
