package com.example.waterwest;

public class Time
{
    private String time;
    private String waterlevel;


    public Time(String time,String waterlevel)
    {
        this.time=time;
        this.waterlevel=waterlevel;
    }
    public Time(){}
    public String GetTime()
    {
        return time;
    }
    public void setTime(String time)
    {
        this.time=time;
    }
    public String GetWaterLevel()
    {
        return waterlevel;
    }
    public void setWaterLevel(String waterlevel)
    {
        this.waterlevel=waterlevel;
    }

}
