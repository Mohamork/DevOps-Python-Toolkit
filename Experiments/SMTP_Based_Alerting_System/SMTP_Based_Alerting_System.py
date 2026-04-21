import win32evtlog
import win32evtlogutil

def get_event_logs(log_type="Application", server="localhost"):
    # 1. Open the log
    hand = win32evtlog.OpenEventLog(server, log_type)
    
    # 2. Set flags: Backwards read (newest first) and Sequential read
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    
    try:
        while True:
            # 3. Read a batch of events
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            if not events:
                break
                
            for event in events:

                if event.EventType == win32evtlog.EVENTLOG_ERROR_TYPE:
  
                    # 4. Extract data
                    print(f"Time: {event.TimeGenerated}")
                    print(f"Source: {event.SourceName}")
                    print(f"Event ID: {event.EventID}")
                    
                    # 5. Format the actual event message
                    msg = win32evtlogutil.SafeFormatMessage(event, log_type)
                    print(f"Message: {msg}\n{'-'*30}")
                
    finally:
        win32evtlog.CloseEventLog(hand)

if __name__ == "__main__":
    get_event_logs()