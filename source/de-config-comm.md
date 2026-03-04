# de_comm.config.module.json Configuration File

A file called **de_comm.config.module.json** exists in **/home/pi/drone_engage/de_comm/**
This file is written in JSON format. However, you can still add comments to the file.
To those who do not know JSON just consider it a text file that you need to edit only few lines in it.

## Accessing the Configuration File

Login to your Raspberry-PI board using ssh.

```bash
ssh pi@raspberry_pi_ip_address
```

Navigate to the configuration directory:

```bash
cd /home/pi/drone_engage/de_comm/
ls
```

Open the configuration file:

```bash
nano de_comm.config.module.json
```

## Configuration Fields

| Field Name | Description | Example |
|------------|-------------|---------|
| **module_id** | A name and GUID for this module | "MT_1", "COMM_MAIN" |
| **unit_type** | Type of unit. Use "control_unit" for drone modules | "control_unit" |
| **s2s_udp_listening_ip** (*) | IP address for the de_comm module to communicate with other modules | "127.0.0.1" if all modules on same board, else "0.0.0.0" |
| **s2s_udp_listening_port** (*) | UDP port used to communicate with other modules | "60000" |
| **s2s_udp_packet_size** (*) | Maximum size of UDP packets, should be same value in all modules | "8192" |
| **auth_ip** (*) | Authentication server IP address | "127.0.0.1", "andruav.com", "droneengage.com" |
| **auth_port** (*) | Authentication server port (number, not string) | 19408 |
| **auth_verify_ssl** (*) | Enable SSL verification for authentication | false |
| **ignore_original_comm_server** (*) | Don't authenticate and connect directly to a drone server | false |
| **root_certificate_path** (*) | Path to SSL certificate (required if auth_verify_ssl is true) | "./root.crt" |
| **userName** (M) | Your account username | "user@example.com" |
| **accessCode** (M) | Your account access code | "your_access_code" |
| **unitID** (M) | A readable name for your drone that will be displayed | "drone1", "D1-Copter" |
| **groupID** (*) | Group identifier for your drone | "1" |
| **unitDescription** (M) | A brief single line description of vehicle | "My X8 Drone" |
| **logger_enabled** (*) | Enable logging (creates log files in Logs folder) | false |
| **logger_debug** (*) | Enable debug logging | false |
| **ping_server_rate_in_ms** (*) | Ping rate to the server in milliseconds | 1500 |
| **max_allowed_ping_delay_in_ms** (*) | Maximum allowed ping delay before restart attempts | 5000 |
| **max_offline_count** (*) | Maximum failed reconnection attempts before app exits | 5 |
| **led_pins_enabled** (*) | Enable power LED indicator (GPIO module only) | true |
| **buzzer_pins_enabled** (*) | Enable buzzer indicator (GPIO module only) | true |

## Legend

- `(*)` You can keep default value unless you have specific requirements
- `(M)` You need to change it based on your account

## Important Notes

> **Important:** If you change **unitDescription** and **unitID** then you need to delete file `de_comm.local`
> Use `rm de_comm.local` to delete it.

**Note:** **userName** and **accessCode** can be generated from your DroneEngage account.

## Example Configuration

```json
{
    /*
        This is a JSON file with ability to add c-like comments.
    */
    
    // A name and GUID for this module
    "module_id"                 : "MT_1",
    "unit_type"                 : "control_unit",
    
    // IP & Port Communication Module is listening to.
    "s2s_udp_listening_ip"      : "0.0.0.0",
    "s2s_udp_listening_port"    : "60000",  
    "s2s_udp_packet_size"       : "8192",

    // Drone-Engage Communication Server Connection
    "auth_ip"                       : "127.0.0.1",
    "auth_port"                     : 19408,
    "auth_verify_ssl"               : false,
    "ignore_original_comm_server"   : false,
    
    // SSL certificate path (optional if auth_verify_ssl == true)
    "root_certificate_path"         : "./root.crt",

    "userName"                  :"your_email@example.com", 
    "accessCode"                :"your_access_code",
    "unitID"                    :"drone_cairo",
    "groupID"                   :"1",
    "unitDescription"           :"My Drone Unit 1",

    // Logger Section
    "logger_enabled"            : false,
    "logger_debug"              : false,

    // Connection management
    "ping_server_rate_in_ms": 1500,
    "max_allowed_ping_delay_in_ms": 5000,
    "max_offline_count": 5,

    // Hardware indicators (GPIO module only)
    "led_pins_enabled" : true,
    "buzzer_pins_enabled" : true
}
```

## SSL Configuration

If you need to connect to a server with SSL verification enabled:

1. Set `"auth_verify_ssl": true`
2. Provide the path to your SSL certificate in `"root_certificate_path"`
3. Ensure the certificate file is accessible by the application

## Connection Troubleshooting

If you experience connection issues:

1. Check that `auth_ip` and `auth_port` are correct
2. Verify your `userName` and `accessCode` are valid
3. Adjust `ping_server_rate_in_ms` and `max_allowed_ping_delay_in_ms` if needed
4. Monitor `max_offline_count` to prevent excessive restarts
5. Check firewall settings for UDP port `s2s_udp_listening_port`
