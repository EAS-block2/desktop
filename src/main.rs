use reqwest;
use std::{process::*, str, thread, time::Duration};
fn main() {
    let mut active = false;
    let mut lastactive = false;
    let mut browser_id = 0;
    let mut lbody: String= String::new();
    println!("user is: {}",get_user());
    let url = format!("http://easrvr:8000/pc/{}", get_user());
    loop {
    let body: String; 
    match reqwest::blocking::get(url.as_str()){
        Ok(out) => {body = out.text().unwrap();}
        Err(_) => {body = String::from("fault");}}
    match body.as_str(){
        "unauthorized" => {println!("unauth error!");break;}
        "clear" => active = false,
        "fault" => active = lastactive,
        _ => active = true,
    }
    println!("active:{}, body: {}", &active, &body);
    if body != lbody && browser_id != 0{
        println!("Here I go Killing again!");
        if cfg!(target_os = "windows"){Command::new("taskkill")
        .arg("/PID").arg(browser_id.to_string()).spawn().unwrap();}
        else {Command::new("kill").arg(browser_id.to_string())
        .spawn().unwrap();}
        browser_id = 0;
        thread::sleep(Duration::from_millis(200));
    }
    if active && (!lastactive || (body != lbody)){
        lastactive = true;
        browser_id = Command::new("firefox")
            .arg("--kiosk")
            .arg(&body).spawn().unwrap().id();
    }
    else if !active && lastactive{
        lastactive = false;
    }
    else{
        thread::sleep(Duration::from_secs(2));
    }
    lbody = body;
    println!("PID is: {}",&browser_id);
}}

fn get_user() -> String{
    let output = Command::new("whoami")
    .output()
    .expect("failed to get username");
    let mut retn = str::from_utf8(&output.stdout).unwrap().to_string();
    if cfg!(target_os = "windows"){
        let tmp: Vec<&str> = retn.split('\\').collect();
        retn = tmp[1].to_string();
    }
retn
}