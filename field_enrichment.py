FIELD_ENRICHMENT: dict[str, dict] = {
    "@timestamp": {
        "synonyms": ["event time", "occurred at", "log time", "datetime", "when", "timestamp", "time of event", "recorded at"],
        "context_phrases": ["when did this event happen", "filter by time range", "sort by date", "events after a specific time"],
    },
    "acknowledged_by": {
        "synonyms": ["confirmed by", "accepted by", "approved by", "responder", "who acknowledged", "alert owner", "triaged by", "handled by"],
        "context_phrases": ["who acknowledged this alert", "find alerts confirmed by a user", "which analyst responded"],
    },
    "acknowledged_by.keyword": {
        "synonyms": ["confirmed by exact", "exact responder", "acknowledged by raw value"],
        "context_phrases": ["exact match on who acknowledged", "filter by acknowledging user precisely"],
    },
    "analysis.activities": {
        "synonyms": ["detected behaviors", "identified actions", "analysis tasks", "observed activities", "event types", "operations found", "activity list"],
        "context_phrases": ["what activities were detected in analysis", "list identified behaviors", "filter by activity type"],
    },
    "analysis.email_ids": {
        "synonyms": ["email addresses from analysis", "analysed email IDs", "found email accounts", "extracted emails", "email identifiers"],
        "context_phrases": ["what email addresses were found in analysis", "emails discovered during investigation"],
    },
    "analysis.location": {
        "synonyms": ["analysed location", "location from analysis", "detected place", "geographic finding", "location extracted"],
        "context_phrases": ["what location was identified in analysis", "where was this activity detected"],
    },
    "analysis.misc": {
        "synonyms": ["miscellaneous analysis data", "other analysis fields", "extra analysis info", "unclassified analysis", "additional findings"],
        "context_phrases": ["extra data from analysis", "miscellaneous findings", "unclassified analysis output"],
    },
    "analysis.organization": {
        "synonyms": ["company identified", "org found in analysis", "entity", "organization detected", "enterprise name", "corporate entity"],
        "context_phrases": ["which organization was identified", "company found in analysis", "detect organization from content"],
    },
    "analysis.person": {
        "synonyms": ["person identified", "individual detected", "name found", "human entity", "subject name", "identity extracted"],
        "context_phrases": ["who was identified in analysis", "person found in content", "individual name extracted"],
    },
    "analysis.possible_languages": {
        "synonyms": ["detected languages", "language candidates", "possible language", "language guess", "identified language", "content language"],
        "context_phrases": ["what language was detected", "possible languages in the content"],
    },
    "analysis.subjects": {
        "synonyms": ["identified subjects", "topics found", "analysed subjects", "content subjects", "key themes", "entities discussed"],
        "context_phrases": ["what subjects were identified", "topics found during analysis"],
    },
    "analysis.text": {
        "synonyms": ["analysed text content", "text from analysis", "extracted text", "content body", "analysis body text"],
        "context_phrases": ["what text was analysed", "content extracted during analysis"],
    },
    "analysis.urls": {
        "synonyms": ["URLs found in analysis", "links identified", "web addresses", "extracted URLs", "hyperlinks detected"],
        "context_phrases": ["what URLs were found", "links discovered during analysis"],
    },
    "appleak.location": {
        "synonyms": ["Apple leak geolocation", "Apple leak coordinates", "geo point for appleak", "Apple leak GPS"],
        "context_phrases": ["where did the Apple leak originate", "geolocation of Apple leak"],
    },
    "appleak_location": {
        "synonyms": ["Apple leak location flag", "appleak location present", "has Apple location", "Apple location indicator"],
        "context_phrases": ["is there a location for the Apple leak", "does the Apple leak have a location"],
    },
    "capture_filters._id": {
        "synonyms": ["capture filter identifier", "filter ID", "capture rule ID", "interception filter ID"],
        "context_phrases": ["what is the capture filter ID", "find capture filter by ID"],
    },
    "capture_filters._id.keyword": {
        "synonyms": ["exact capture filter ID", "filter ID raw"],
        "context_phrases": ["exact match on capture filter ID"],
    },
    "capture_filters.assign_to": {
        "synonyms": ["filter assigned to", "capture rule owner", "assigned analyst", "filter assignee", "who owns the filter"],
        "context_phrases": ["who is this capture filter assigned to", "analyst assigned to capture rule"],
    },
    "capture_filters.assign_to.keyword": {
        "synonyms": ["exact filter assignee", "assigned to raw"],
        "context_phrases": ["exact match on filter assignee"],
    },
    "capture_filters.casename": {
        "synonyms": ["case name", "investigation name", "case label", "operation name", "case title"],
        "context_phrases": ["what case does this filter belong to", "find filter by case name"],
    },
    "capture_filters.casename.keyword": {
        "synonyms": ["exact case name", "case label raw"],
        "context_phrases": ["exact match on capture filter case name"],
    },
    "capture_filters.comment": {
        "synonyms": ["filter notes", "capture rule comments", "analyst notes on filter", "filter annotation"],
        "context_phrases": ["comments on the capture filter", "analyst notes for this filter"],
    },
    "capture_filters.condition": {
        "synonyms": ["filter condition", "capture rule logic", "filter expression", "filter criteria", "rule condition"],
        "context_phrases": ["what condition does this filter use", "filter matching logic"],
    },
    "capture_filters.name": {
        "synonyms": ["filter name", "capture rule name", "interception filter label", "rule title"],
        "context_phrases": ["name of the capture filter", "find filter by name"],
    },
    "capture_filters.name.keyword": {
        "synonyms": ["exact filter name", "capture filter name raw"],
        "context_phrases": ["exact match on capture filter name"],
    },
    "capture_filters.targetvalue": {
        "synonyms": ["filter target", "capture target value", "interception target", "rule target", "monitored value"],
        "context_phrases": ["what value does this capture filter target", "target being monitored by filter"],
    },
    "categories_suggested": {
        "synonyms": ["suggested tags", "proposed categories", "auto-categorized", "recommended categories", "classification suggestions"],
        "context_phrases": ["what categories were suggested", "auto-suggested classification"],
    },
    "categories_suggested_at": {
        "synonyms": ["when categories were suggested", "suggestion timestamp", "categorized at", "classification time"],
        "context_phrases": ["when were categories suggested", "time of category suggestion"],
    },
    "categories_suggested_by": {
        "synonyms": ["who suggested categories", "categorized by", "classification author", "category suggester"],
        "context_phrases": ["who proposed the categories", "which user or system suggested categories"],
    },
    "datalink.dst_eth": {
        "synonyms": ["destination MAC address", "dst MAC", "destination Ethernet address", "target MAC", "receiver MAC"],
        "context_phrases": ["what is the destination MAC address", "find traffic to a specific MAC"],
    },
    "datalink.eth_protocol": {
        "synonyms": ["Ethernet protocol type", "layer 2 protocol", "eth proto", "frame protocol", "link layer protocol"],
        "context_phrases": ["what Ethernet protocol was used", "layer 2 protocol type"],
    },
    "datalink.eth_type": {
        "synonyms": ["Ethernet type value", "EtherType", "frame type code", "protocol type number"],
        "context_phrases": ["what is the EtherType value", "Ethernet frame type integer"],
    },
    "datalink.link_names": {
        "synonyms": ["link layer names", "data link identifiers", "named links", "interface link names"],
        "context_phrases": ["what are the link names", "data link layer identifiers"],
    },
    "datalink.mpls_labels": {
        "synonyms": ["MPLS label stack", "MPLS tags", "label switched path labels", "MPLS forwarding labels"],
        "context_phrases": ["what MPLS labels are present", "filter by MPLS label"],
    },
    "datalink.src_eth": {
        "synonyms": ["source MAC address", "src MAC", "sender MAC", "originating Ethernet address", "source hardware address"],
        "context_phrases": ["what is the source MAC address", "find traffic from a specific MAC"],
    },
    "datalink.vlan_ids": {
        "synonyms": ["VLAN tags", "VLAN identifiers", "virtual LAN IDs", "802.1Q tags", "network segment IDs"],
        "context_phrases": ["what VLAN is this traffic on", "filter by VLAN ID"],
    },
    "filter_comments": {
        "synonyms": ["filter notes", "rule comments", "analyst filter remarks", "filter annotation"],
        "context_phrases": ["comments attached to filters", "analyst notes on filters"],
    },
    "filter_names": {
        "synonyms": ["filter labels", "rule names", "interception filter titles", "capture rule names"],
        "context_phrases": ["names of filters applied", "which filters matched"],
    },
    "filter_names.keyword": {
        "synonyms": ["exact filter name", "filter label raw"],
        "context_phrases": ["exact match on filter name"],
    },
    "gtp_apn": {
        "synonyms": ["GTP access point name", "mobile APN", "GPRS access point", "cellular APN", "mobile network APN"],
        "context_phrases": ["what APN was used", "mobile access point name"],
    },
    "gtp_imei_sv": {
        "synonyms": ["IMEI software version", "device IMEI SV", "GTP IMEI", "mobile device software version"],
        "context_phrases": ["IMEI software version of device", "device software version identifier"],
    },
    "gtp_imsi": {
        "synonyms": ["IMSI number", "subscriber identity", "mobile subscriber ID", "SIM identity", "international mobile subscriber identity"],
        "context_phrases": ["what is the IMSI", "find traffic by subscriber identity", "mobile user identifier"],
    },
    "gtp_imsi_mcc": {
        "synonyms": ["mobile country code", "MCC", "IMSI country code", "subscriber country code"],
        "context_phrases": ["what country is this subscriber from", "mobile country code from IMSI"],
    },
    "gtp_imsi_mnc": {
        "synonyms": ["mobile network code", "MNC", "IMSI network code", "carrier code", "operator code"],
        "context_phrases": ["what mobile network is this subscriber on", "mobile network code from IMSI"],
    },
    "gtp_msisdn": {
        "synonyms": ["phone number", "MSISDN", "mobile subscriber number", "calling number", "SIM phone number"],
        "context_phrases": ["what is the phone number", "find traffic by MSISDN", "mobile subscriber ISDN number"],
    },
    "gtp_rai_lac": {
        "synonyms": ["location area code", "LAC", "GTP RAI", "routing area location", "cell location code"],
        "context_phrases": ["location area code for this subscriber", "cellular location identifier"],
    },
    "host": {
        "synonyms": ["hostname", "device name", "machine name", "server name", "endpoint name", "host identifier"],
        "context_phrases": ["what host generated this event", "filter by hostname", "source machine name"],
    },
    "host.keyword": {
        "synonyms": ["exact hostname", "host raw value", "machine name exact"],
        "context_phrases": ["exact match on hostname"],
    },
    "imported": {
        "synonyms": ["import flag", "imported record", "was imported", "data import indicator"],
        "context_phrases": ["was this record imported", "import status flag"],
    },
    "language_code": {
        "synonyms": ["language identifier", "language tag", "ISO language code", "detected language code", "lang code"],
        "context_phrases": ["what language code was detected", "ISO code for the language"],
    },
    "language_found": {
        "synonyms": ["detected language", "language identified", "language of content", "content language", "language name"],
        "context_phrases": ["what language was found", "detected language name"],
    },
    "language_score": {
        "synonyms": ["language confidence", "language detection score", "language probability", "detection confidence"],
        "context_phrases": ["how confident is the language detection", "language match score"],
    },
    "md5": {
        "synonyms": ["MD5 hash", "file hash", "checksum", "message digest", "MD5 fingerprint", "hash value", "file fingerprint"],
        "context_phrases": ["what is the MD5 hash", "find by checksum", "file integrity hash", "malware hash lookup"],
    },
    "network.countries": {
        "synonyms": ["network countries", "countries involved", "geographic countries", "IP countries", "nations in traffic"],
        "context_phrases": ["which countries are involved in this traffic", "filter by country"],
    },
    "network.detected_names": {
        "synonyms": ["detected hostnames", "network names found", "resolved names", "identified names in network"],
        "context_phrases": ["what network names were detected", "hostnames identified in traffic"],
    },
    "network.dst_geo_ip.as_org": {
        "synonyms": ["destination AS org", "destination autonomous system", "destination ISP", "dst AS organization"],
        "context_phrases": ["what organization owns the destination IP", "destination ISP or AS"],
    },
    "network.dst_geo_ip.asn": {
        "synonyms": ["destination ASN", "destination autonomous system number", "dst AS number"],
        "context_phrases": ["what is the destination ASN", "filter by destination autonomous system number"],
    },
    "network.dst_geo_ip.city_name": {
        "synonyms": ["destination city", "dst city", "target city", "destination location city"],
        "context_phrases": ["what city is the destination in", "city of the destination IP"],
    },
    "network.dst_geo_ip.country_code": {
        "synonyms": ["destination country code", "dst country code", "target country ISO code"],
        "context_phrases": ["what country code is the destination", "ISO code for destination country"],
    },
    "network.dst_geo_ip.country_name": {
        "synonyms": ["destination country", "dst country", "target country", "country of destination IP"],
        "context_phrases": ["what country is the destination in", "filter by destination country"],
    },
    "network.dst_geo_ip.latitude": {
        "synonyms": ["destination latitude", "dst lat", "destination GPS latitude"],
        "context_phrases": ["latitude of destination IP", "geographic latitude of destination"],
    },
    "network.dst_geo_ip.location": {
        "synonyms": ["destination geo point", "destination coordinates", "dst location", "destination GPS"],
        "context_phrases": ["geolocation of destination IP", "where is the destination IP located"],
    },
    "network.dst_geo_ip.longitude": {
        "synonyms": ["destination longitude", "dst lon", "destination GPS longitude"],
        "context_phrases": ["longitude of destination IP", "geographic longitude of destination"],
    },
    "network.dst_geo_ip.region_name": {
        "synonyms": ["destination region", "dst region", "destination state or province"],
        "context_phrases": ["what region is the destination in", "region of destination IP"],
    },
    "network.dst_host": {
        "synonyms": ["destination hostname", "dst host", "target host", "destination domain", "receiver hostname"],
        "context_phrases": ["what is the destination hostname", "find traffic to a specific host"],
    },
    "network.dst_host.keyword": {
        "synonyms": ["exact destination hostname", "dst host raw"],
        "context_phrases": ["exact match on destination hostname"],
    },
    "network.dst_ip": {
        "synonyms": ["destination IP", "dst IP", "target IP address", "receiver IP", "destination address", "remote IP"],
        "context_phrases": ["what is the destination IP address", "filter by destination IP", "traffic going to this IP"],
    },
    "network.dst_ip_remark": {
        "synonyms": ["destination IP notes", "dst IP annotation", "remarks about dst IP"],
        "context_phrases": ["remarks about the destination IP", "notes on destination IP address"],
    },
    "network.ip_addresses": {
        "synonyms": ["all IP addresses", "IP address list", "IPs in session", "involved IP addresses", "network IPs"],
        "context_phrases": ["what IP addresses are involved", "list all IPs in this session"],
    },
    "network.ip_protocol": {
        "synonyms": ["IP protocol type", "layer 3 protocol", "network protocol", "TCP UDP ICMP", "protocol over IP"],
        "context_phrases": ["what IP protocol is used", "layer 3 protocol type"],
    },
    "network.ip_version": {
        "synonyms": ["IP version", "IPv4 or IPv6", "internet protocol version", "IP stack version"],
        "context_phrases": ["is this IPv4 or IPv6", "filter by IP version"],
    },
    "network.max_frag_data_length": {
        "synonyms": ["max fragment size", "largest fragment", "maximum fragmentation length"],
        "context_phrases": ["maximum fragment data length", "largest IP fragment size"],
    },
    "network.min_frag_data_length": {
        "synonyms": ["min fragment size", "smallest fragment", "minimum fragmentation length"],
        "context_phrases": ["minimum fragment data length", "smallest IP fragment size"],
    },
    "network.src_geo_ip.as_org": {
        "synonyms": ["source AS org", "source autonomous system", "source ISP", "src AS organization"],
        "context_phrases": ["what organization owns the source IP", "source ISP or AS"],
    },
    "network.src_geo_ip.asn": {
        "synonyms": ["source ASN", "source autonomous system number", "src AS number"],
        "context_phrases": ["what is the source ASN", "filter by source autonomous system number"],
    },
    "network.src_geo_ip.city_name": {
        "synonyms": ["source city", "src city", "originating city", "city of source IP"],
        "context_phrases": ["what city is the source in", "city of the source IP"],
    },
    "network.src_geo_ip.country_code": {
        "synonyms": ["source country code", "src country code", "originating country ISO code"],
        "context_phrases": ["what country code is the source", "ISO code for source country"],
    },
    "network.src_geo_ip.country_name": {
        "synonyms": ["source country", "src country", "originating country", "country of source IP"],
        "context_phrases": ["what country is the source in", "filter by source country"],
    },
    "network.src_geo_ip.latitude": {
        "synonyms": ["source latitude", "src lat", "source GPS latitude"],
        "context_phrases": ["latitude of source IP", "geographic latitude of source"],
    },
    "network.src_geo_ip.location": {
        "synonyms": ["source geo point", "source coordinates", "src location", "source GPS"],
        "context_phrases": ["geolocation of source IP", "where is the source IP located"],
    },
    "network.src_geo_ip.longitude": {
        "synonyms": ["source longitude", "src lon", "source GPS longitude"],
        "context_phrases": ["longitude of source IP", "geographic longitude of source"],
    },
    "network.src_geo_ip.region_name": {
        "synonyms": ["source region", "src region", "originating state or province"],
        "context_phrases": ["what region is the source in", "region of source IP"],
    },
    "network.src_host": {
        "synonyms": ["source hostname", "src host", "originating host", "sender hostname", "source domain"],
        "context_phrases": ["what is the source hostname", "find traffic from a specific host"],
    },
    "network.src_host.keyword": {
        "synonyms": ["exact source hostname", "src host raw"],
        "context_phrases": ["exact match on source hostname"],
    },
    "network.src_ip": {
        "synonyms": ["source IP", "src IP", "originating IP address", "sender IP", "source address", "client IP"],
        "context_phrases": ["what is the source IP address", "filter by source IP", "traffic coming from this IP"],
    },
    "network.src_ip_remark": {
        "synonyms": ["source IP notes", "src IP annotation", "remarks about src IP"],
        "context_phrases": ["remarks about the source IP", "notes on source IP address"],
    },
    "network.tunnel_src_ip": {
        "synonyms": ["tunnel source IP", "VPN source IP", "encapsulated source IP", "inner source IP"],
        "context_phrases": ["source IP inside the tunnel", "VPN tunnel source address"],
    },
    "network.tunnel_dst_ip": {
        "synonyms": ["tunnel destination IP", "VPN destination IP", "encapsulated destination IP", "inner destination IP"],
        "context_phrases": ["destination IP inside the tunnel", "VPN tunnel destination address"],
    },
    "payload.dns_domain_names": {
        "synonyms": ["DNS domains", "queried domains", "DNS names", "domain names in DNS", "resolved domains", "DNS lookup domains"],
        "context_phrases": ["what domains were queried in DNS", "filter by DNS domain"],
    },
    "payload.dns_headers.*": {
        "synonyms": ["DNS headers", "DNS protocol headers", "DNS response fields", "DNS packet headers"],
        "context_phrases": ["DNS header fields", "all DNS header data"],
    },
    "payload.dns_headers.txt_data": {
        "synonyms": ["DNS TXT record", "DNS text record", "TXT record data", "DNS SPF DKIM data"],
        "context_phrases": ["what TXT records were in DNS", "SPF or DKIM data from DNS"],
    },
    "payload.dns_headers.cname": {
        "synonyms": ["DNS CNAME", "canonical name record", "DNS alias", "CNAME record", "DNS redirect"],
        "context_phrases": ["DNS CNAME record value", "alias resolved in DNS"],
    },
    "payload.dns_headers.dns_record_type": {
        "synonyms": ["DNS record type", "DNS query type", "A AAAA MX TXT record type"],
        "context_phrases": ["what type of DNS record", "filter by DNS record type"],
    },
    "payload.dns_ip_address": {
        "synonyms": ["DNS resolved IP", "IP from DNS", "DNS answer IP", "resolved IP address", "DNS A record IP"],
        "context_phrases": ["what IP address was returned by DNS", "IP from DNS lookup"],
    },
    "payload.dtmf": {
        "synonyms": ["DTMF tones", "touch tones", "telephone keypad tones", "dual tone multi frequency", "IVR tones"],
        "context_phrases": ["DTMF tones detected in call", "IVR keypad input"],
    },
    "payload.email_from": {
        "synonyms": ["email sender", "from address", "sender email", "email originator", "who sent the email"],
        "context_phrases": ["who sent this email", "email sender address", "filter by email from field"],
    },
    "payload.email_subjects": {
        "synonyms": ["email subject", "email title", "message subject", "email topic", "email header subject"],
        "context_phrases": ["what is the email subject", "filter by email subject line"],
    },
    "payload.email_to": {
        "synonyms": ["email recipient", "to address", "receiver email", "email destination", "who received the email"],
        "context_phrases": ["who received this email", "email recipient address"],
    },
    "payload.fax_csi": {
        "synonyms": ["fax CSI", "called subscriber identification", "fax sender ID"],
        "context_phrases": ["fax CSI identifier", "called subscriber ID in fax"],
    },
    "payload.fax_tsi": {
        "synonyms": ["fax TSI", "transmitting subscriber identification", "fax transmitter ID", "fax sender station ID"],
        "context_phrases": ["fax TSI identifier", "transmitting station ID"],
    },
    "payload.file_names": {
        "synonyms": ["file names in payload", "transferred files", "file name list", "filenames detected", "document names"],
        "context_phrases": ["what files were transferred", "file names found in payload"],
    },
    "payload.file_types": {
        "synonyms": ["file types", "file extensions", "mime types", "file format types", "document types"],
        "context_phrases": ["what types of files were detected", "filter by file type"],
    },
    "payload.ftp_data_type": {
        "synonyms": ["FTP transfer type", "FTP data mode", "FTP ASCII binary", "FTP file transfer type"],
        "context_phrases": ["FTP data type for transfer", "was FTP transfer ASCII or binary"],
    },
    "payload.gsm_*": {
        "synonyms": ["GSM protocol fields", "GSM mobile fields", "GSM headers", "2G protocol data"],
        "context_phrases": ["GSM protocol data", "2G cellular protocol headers"],
    },
    "payload.h323_headers.call_identifier": {
        "synonyms": ["H.323 call ID", "VoIP call identifier", "call ID", "H323 session ID"],
        "context_phrases": ["H.323 call identifier", "find session by call ID"],
    },
    "payload.h323_headers.called_display": {
        "synonyms": ["H.323 called party display", "called name", "callee display name", "H323 destination name"],
        "context_phrases": ["display name of the called party", "who was called in H323"],
    },
    "payload.h323_headers.calling_display": {
        "synonyms": ["H.323 calling party display", "caller name", "caller display name", "H323 source name"],
        "context_phrases": ["display name of the calling party", "who initiated the H323 call"],
    },
    "payload.h323_headers.calling_number": {
        "synonyms": ["H.323 caller number", "calling party number", "H323 source number", "caller phone number"],
        "context_phrases": ["H.323 calling number", "phone number of caller in H323"],
    },
    "payload.h323_headers.conference_id": {
        "synonyms": ["H.323 conference ID", "conference identifier", "H323 meeting ID"],
        "context_phrases": ["H.323 conference identifier"],
    },
    "payload.h323_headers.protocol_identifier": {
        "synonyms": ["H.323 protocol ID", "H323 version identifier"],
        "context_phrases": ["H.323 protocol identifier", "H323 version used"],
    },
    "payload.hget_*": {
        "synonyms": ["HGET fields", "HGET protocol data"],
        "context_phrases": ["HGET protocol fields"],
    },
    "payload.http_cookie": {
        "synonyms": ["HTTP cookie", "web cookie", "session cookie", "browser cookie", "cookie header"],
        "context_phrases": ["HTTP cookie value", "web session cookie"],
    },
    "payload.http_get": {
        "synonyms": ["HTTP GET request", "HTTP request URL", "GET request path", "HTTP URI", "web request"],
        "context_phrases": ["HTTP GET request made", "URL requested via GET"],
    },
    "payload.http_host": {
        "synonyms": ["HTTP host header", "web server hostname", "HTTP host", "requested hostname", "virtual host"],
        "context_phrases": ["HTTP host header value", "which hostname was requested"],
    },
    "payload.http_server": {
        "synonyms": ["HTTP server header", "web server software", "server banner", "HTTP server type"],
        "context_phrases": ["what web server was used", "web server software banner"],
    },
    "payload.http_x_api_version": {
        "synonyms": ["API version header", "X-API-Version", "HTTP API version"],
        "context_phrases": ["API version used in HTTP request"],
    },
    "payload.http_x_forwarded_for": {
        "synonyms": ["X-Forwarded-For", "proxy IP", "real client IP behind proxy", "forwarded IP", "original client IP", "XFF header"],
        "context_phrases": ["client IP behind a proxy", "X-Forwarded-For header", "original IP before NAT or proxy"],
    },
    "payload.incorrect_login_attempt": {
        "synonyms": ["failed login", "bad credentials", "authentication failure details", "wrong password attempt"],
        "context_phrases": ["failed login attempt details", "incorrect credentials used"],
    },
    "payload.incorrect_login_attempts_count": {
        "synonyms": ["failed login count", "auth failure count", "wrong password count", "brute force attempts", "number of failed logins"],
        "context_phrases": ["how many failed login attempts", "brute force attempt count"],
    },
    "payload.irc_message": {
        "synonyms": ["IRC chat message", "IRC communication", "internet relay chat message", "IRC text"],
        "context_phrases": ["IRC message content", "chat message over IRC"],
    },
    "payload.is_ephemeral_cipher": {
        "synonyms": ["ephemeral cipher flag", "forward secrecy cipher", "DHE ECDHE cipher", "perfect forward secrecy"],
        "context_phrases": ["was an ephemeral cipher used", "is forward secrecy enabled"],
    },
    "payload.is_fax": {
        "synonyms": ["fax indicator", "is fax transmission", "fax flag", "fax session flag"],
        "context_phrases": ["is this a fax transmission", "fax detection flag"],
    },
    "payload.machine.browser": {
        "synonyms": ["web browser", "browser type", "browser name", "user browser", "HTTP client browser"],
        "context_phrases": ["what browser was used", "browser detected from user agent"],
    },
    "payload.machine.device_name": {
        "synonyms": ["device name", "machine name", "endpoint device name", "client device name", "hardware name"],
        "context_phrases": ["what device was used", "name of the client device"],
    },
    "payload.machine.device_type": {
        "synonyms": ["device type", "device category", "endpoint type", "mobile desktop tablet", "hardware type"],
        "context_phrases": ["type of device used", "is this a mobile or desktop device"],
    },
    "payload.machine.platform": {
        "synonyms": ["operating system", "platform type", "OS name", "Windows Linux Android iOS"],
        "context_phrases": ["what platform or OS was used", "operating system of the device"],
    },
    "payload.machine_address": {
        "synonyms": ["machine IP address", "device address", "client machine address", "endpoint address"],
        "context_phrases": ["machine address of the endpoint", "device network address"],
    },
    "payload.megaco_headers.*": {
        "synonyms": ["Megaco headers", "H.248 headers", "media gateway control headers"],
        "context_phrases": ["Megaco or H.248 protocol headers", "media gateway control data"],
    },
    "payload.mtp3_headers.dpc": {
        "synonyms": ["MTP3 destination point code", "DPC", "SS7 destination point code", "signaling destination"],
        "context_phrases": ["MTP3 destination point code", "SS7 DPC value"],
    },
    "payload.mtp3_headers.opc": {
        "synonyms": ["MTP3 origination point code", "OPC", "SS7 origination point code", "signaling source"],
        "context_phrases": ["MTP3 origination point code", "SS7 OPC value"],
    },
    "payload.national_numbers": {
        "synonyms": ["national phone numbers", "local format numbers", "national format phone", "in-country numbers"],
        "context_phrases": ["national phone numbers found in payload"],
    },
    "payload.numbers": {
        "synonyms": ["phone numbers", "telephone numbers", "dialled numbers", "contact numbers", "MSISDN numbers"],
        "context_phrases": ["phone numbers found in session", "filter by phone number"],
    },
    "payload.numbers.keyword": {
        "synonyms": ["exact phone number", "phone number raw value"],
        "context_phrases": ["exact match on phone number"],
    },
    "payload.password": {
        "synonyms": ["password found", "credential", "cleartext password", "extracted password", "login password"],
        "context_phrases": ["was a password detected in traffic", "cleartext credential found"],
    },
    "payload.possible_ids": {
        "synonyms": ["possible identifiers", "potential IDs", "extracted identifiers", "possible account IDs"],
        "context_phrases": ["possible identifiers in the payload", "potential account IDs found"],
    },
    "payload.possible_ids.keyword": {
        "synonyms": ["exact possible identifier", "possible ID raw value"],
        "context_phrases": ["exact match on possible identifier"],
    },
    "payload.radius_headers.user_name": {
        "synonyms": ["RADIUS username", "RADIUS user", "AAA username", "authenticated username via RADIUS", "network access username"],
        "context_phrases": ["username in RADIUS authentication", "who authenticated via RADIUS"],
    },
    "payload.remarks": {
        "synonyms": ["payload notes", "payload annotations", "payload comments", "payload flags"],
        "context_phrases": ["remarks attached to payload", "notes on this payload"],
    },
    "payload.rtsp_headers.content_type": {
        "synonyms": ["RTSP content type", "streaming media type", "RTSP media format", "video stream content type"],
        "context_phrases": ["RTSP content type header", "streaming format type"],
    },
    "payload.s7comm_headers.*": {
        "synonyms": ["S7 communication headers", "Siemens S7 PLC headers", "industrial protocol S7", "ICS S7 data"],
        "context_phrases": ["Siemens S7 protocol headers", "SCADA S7 fields"],
    },
    "payload.sctp_headers.protocol": {
        "synonyms": ["SCTP protocol", "stream control transmission protocol", "SCTP PPID"],
        "context_phrases": ["SCTP protocol type", "payload protocol identifier in SCTP"],
    },
    "payload.sip_country_codes": {
        "synonyms": ["SIP country codes", "VoIP country codes", "SIP call country", "countries in SIP call"],
        "context_phrases": ["country codes in SIP session", "countries involved in VoIP call"],
    },
    "payload.sip_from_area_code": {
        "synonyms": ["SIP caller area code", "calling area code", "SIP originating area"],
        "context_phrases": ["area code of SIP caller"],
    },
    "payload.sip_from_cc": {
        "synonyms": ["SIP caller country code", "SIP from country", "calling country code"],
        "context_phrases": ["country code of SIP caller", "where the SIP call originated"],
    },
    "payload.sip_from_cn": {
        "synonyms": ["SIP caller common name", "SIP from name", "caller name in SIP", "SIP calling party name"],
        "context_phrases": ["name of the SIP caller"],
    },
    "payload.sip_from_display": {
        "synonyms": ["SIP caller display name", "SIP from display", "calling party display", "caller name shown"],
        "context_phrases": ["display name of SIP caller"],
    },
    "payload.sip_from_id": {
        "synonyms": ["SIP from identifier", "SIP caller ID", "SIP URI from", "calling party SIP ID"],
        "context_phrases": ["SIP from identifier value", "identity of SIP caller"],
    },
    "payload.sip_from_parsed_id": {
        "synonyms": ["parsed SIP from ID", "extracted SIP caller ID", "normalised SIP from identifier"],
        "context_phrases": ["parsed SIP from identifier"],
    },
    "payload.sip_ids": {
        "synonyms": ["SIP identifiers", "SIP call IDs", "SIP session IDs", "SIP URIs", "VoIP identifiers"],
        "context_phrases": ["SIP identifiers in session", "VoIP session identifiers"],
    },
    "payload.sip_national_number": {
        "synonyms": ["SIP national number", "SIP local number", "national format SIP number"],
        "context_phrases": ["national phone number in SIP"],
    },
    "payload.sip_subject": {
        "synonyms": ["SIP subject header", "SIP call subject", "VoIP call subject"],
        "context_phrases": ["subject of SIP call or message"],
    },
    "payload.sip_to_cc": {
        "synonyms": ["SIP destination country code", "SIP to country", "called party country code"],
        "context_phrases": ["country code of SIP destination"],
    },
    "payload.sip_to_cn": {
        "synonyms": ["SIP destination common name", "SIP to name", "callee name in SIP", "called party name"],
        "context_phrases": ["common name of SIP destination"],
    },
    "payload.sip_to_display": {
        "synonyms": ["SIP destination display name", "SIP to display", "callee display name"],
        "context_phrases": ["display name of SIP destination"],
    },
    "payload.sip_to_id": {
        "synonyms": ["SIP to identifier", "SIP destination ID", "SIP URI to", "called party SIP ID"],
        "context_phrases": ["SIP to identifier value", "identity of SIP destination"],
    },
    "payload.sip_to_parsed_id": {
        "synonyms": ["parsed SIP to ID", "extracted SIP destination ID"],
        "context_phrases": ["parsed SIP to identifier"],
    },
    "payload.sip_pai": {
        "synonyms": ["SIP P-Asserted-Identity", "asserted identity", "trusted caller identity", "SIP PAI header"],
        "context_phrases": ["SIP P-Asserted-Identity value", "trusted identity asserted in SIP"],
    },
    "payload.sip_pai_cc": {
        "synonyms": ["SIP PAI country code", "asserted identity country code"],
        "context_phrases": ["country code of SIP P-Asserted-Identity"],
    },
    "payload.sip_pai_cn": {
        "synonyms": ["SIP PAI common name", "asserted identity name"],
        "context_phrases": ["common name in SIP PAI header"],
    },
    "payload.sip_pai_display": {
        "synonyms": ["SIP PAI display name", "asserted identity display name"],
        "context_phrases": ["display name of SIP P-Asserted-Identity"],
    },
    "payload.sip_pai_id": {
        "synonyms": ["SIP PAI identifier", "asserted identity ID"],
        "context_phrases": ["SIP PAI identifier value"],
    },
    "payload.sip_pai_parsed_id": {
        "synonyms": ["parsed SIP PAI ID", "extracted asserted identity ID"],
        "context_phrases": ["parsed P-Asserted-Identity identifier"],
    },
    "payload.sip_pai_url": {
        "synonyms": ["SIP PAI URL", "asserted identity URL", "PAI SIP URI"],
        "context_phrases": ["URL in SIP P-Asserted-Identity header"],
    },
    "payload.sip_p_access_network_info": {
        "synonyms": ["SIP access network info", "P-Access-Network-Info", "SIP network access header"],
        "context_phrases": ["SIP P-Access-Network-Info header"],
    },
    "payload.sip_visited_network_id": {
        "synonyms": ["SIP visited network", "roaming network ID", "visited network identifier"],
        "context_phrases": ["SIP visited network identifier", "roaming network ID in SIP session"],
    },
    "payload.sms_data": {
        "synonyms": ["SMS message", "text message content", "SMS text", "short message content", "SMS body"],
        "context_phrases": ["SMS message content", "what was the text message"],
    },
    "payload.ssl_negotiated_cipher": {
        "synonyms": ["TLS cipher suite", "SSL cipher", "negotiated cipher", "encryption cipher", "TLS algorithm"],
        "context_phrases": ["what cipher was negotiated in TLS", "encryption algorithm in TLS handshake"],
    },
    "payload.ssl_server_name": {
        "synonyms": ["TLS SNI", "SSL server name", "SNI hostname", "TLS server name indication", "SSL hostname"],
        "context_phrases": ["TLS SNI server name", "which hostname in TLS handshake"],
    },
    "payload.ssl_version": {
        "synonyms": ["TLS version", "SSL version", "TLS protocol version", "SSL TLS version string"],
        "context_phrases": ["what TLS or SSL version was used", "TLS version negotiated"],
    },
    "payload.sslhash_alert": {
        "synonyms": ["SSL hash alert", "TLS alert hash", "SSL fingerprint alert", "JA3 alert"],
        "context_phrases": ["SSL hash alert triggered", "TLS fingerprint alert"],
    },
    "payload.telnet_headers": {
        "synonyms": ["Telnet headers", "Telnet protocol data", "Telnet session headers"],
        "context_phrases": ["Telnet protocol headers"],
    },
    "payload.tftp_headers.file_name": {
        "synonyms": ["TFTP filename", "TFTP transferred file", "trivial FTP file name"],
        "context_phrases": ["filename transferred over TFTP"],
    },
    "payload.time_zones": {
        "synonyms": ["time zones detected", "timezone values", "UTC offsets detected", "timezone identifiers"],
        "context_phrases": ["time zones found in payload", "UTC offset in session"],
    },
    "payload.tls_client_fingerprint": {
        "synonyms": ["TLS client fingerprint", "JA3 fingerprint", "client TLS fingerprint", "TLS client hash", "JA3"],
        "context_phrases": ["TLS client fingerprint value", "JA3 hash of client"],
    },
    "payload.tls_server_fingerprint": {
        "synonyms": ["TLS server fingerprint", "JA3S fingerprint", "server TLS fingerprint", "TLS server hash", "JA3S"],
        "context_phrases": ["TLS server fingerprint value", "JA3S hash of server"],
    },
    "payload.uma_gsm_headers.dst_phone_number": {
        "synonyms": ["UMA destination phone number", "GSM destination number", "called GSM number"],
        "context_phrases": ["destination phone number in UMA GSM", "called party number in UMA session"],
    },
    "payload.uma_gsm_headers.src_phone_number": {
        "synonyms": ["UMA source phone number", "GSM source number", "calling GSM number"],
        "context_phrases": ["source phone number in UMA GSM", "calling party number in UMA session"],
    },
    "payload.user_agent": {
        "synonyms": ["user agent string", "browser user agent", "HTTP user agent", "client user agent", "UA string"],
        "context_phrases": ["what user agent was used", "HTTP user agent string", "browser or client software identifier"],
    },
    "payload.user_id": {
        "synonyms": ["user ID", "user identifier", "account ID", "login ID", "authenticated user ID", "username"],
        "context_phrases": ["what is the user ID", "filter by user identifier", "authenticated user in session"],
    },
    "payload.voip_routing_countries": {
        "synonyms": ["VoIP routing countries", "call routing countries", "SIP routing countries"],
        "context_phrases": ["countries involved in VoIP routing"],
    },
    "payload.arp_headers.opcode": {
        "synonyms": ["ARP opcode", "ARP operation", "ARP request reply", "ARP operation code"],
        "context_phrases": ["ARP opcode value", "was this an ARP request or reply"],
    },
    "payload.arp_headers.sender_ip": {
        "synonyms": ["ARP sender IP", "ARP source IP", "ARP announcer IP", "gratuitous ARP IP"],
        "context_phrases": ["IP address of ARP sender", "who sent the ARP"],
    },
    "payload.arp_headers.target_ip": {
        "synonyms": ["ARP target IP", "ARP destination IP", "IP being resolved in ARP"],
        "context_phrases": ["target IP in ARP packet", "which IP is being resolved by ARP"],
    },
    "payload.attribute_type": {
        "synonyms": ["attribute type", "payload attribute category", "attribute class", "data attribute type"],
        "context_phrases": ["type of attribute in payload"],
    },
    "payload.attribute_value": {
        "synonyms": ["attribute value", "payload attribute data", "attribute content"],
        "context_phrases": ["value of the attribute", "payload attribute value"],
    },
    "payload.icmp_code": {
        "synonyms": ["ICMP code", "ICMP subtype code", "ICMP error code", "ping ICMP code"],
        "context_phrases": ["ICMP code value", "ICMP error subtype"],
    },
    "payload.icmp_type": {
        "synonyms": ["ICMP type", "ICMP message type", "ping type", "ICMP echo type"],
        "context_phrases": ["ICMP type value", "is this an ICMP echo request or reply"],
    },
    "payload.kerberos_headers.error_code": {
        "synonyms": ["Kerberos error", "KRB error code", "Kerberos authentication error", "KDC error code"],
        "context_phrases": ["Kerberos error code value", "authentication error in Kerberos"],
    },
    "payload.ldap_headers.bindresponse_code": {
        "synonyms": ["LDAP bind response", "LDAP auth response code", "LDAP bind result", "directory bind code"],
        "context_phrases": ["LDAP bind response code", "was LDAP bind successful"],
    },
    "payload.smb_headers.msrpc_bind_iface_uuid": {
        "synonyms": ["MSRPC interface UUID", "RPC bind UUID", "DCOM interface UUID", "RPC interface identifier"],
        "context_phrases": ["MSRPC bind interface UUID", "RPC interface being called"],
    },
    "payload.smb_headers.msrpc_bind_minor_version": {
        "synonyms": ["MSRPC minor version", "RPC bind minor version"],
        "context_phrases": ["MSRPC bind minor version number"],
    },
    "payload.smb_headers.msrpc_bind_version": {
        "synonyms": ["MSRPC bind version", "RPC bind major version", "RPC protocol version"],
        "context_phrases": ["MSRPC bind version number"],
    },
    "payload.smb_headers.msrpc_key_file": {
        "synonyms": ["MSRPC key file", "RPC key file", "MSRPC named pipe file"],
        "context_phrases": ["MSRPC key file in SMB"],
    },
    "payload.smb_headers.msrpc_key_name": {
        "synonyms": ["MSRPC key name", "RPC named pipe name", "MSRPC binding name"],
        "context_phrases": ["MSRPC key name", "RPC named pipe identifier"],
    },
    "payload.smb_headers.msrpc_opnum": {
        "synonyms": ["MSRPC operation number", "RPC opnum", "RPC operation ID", "DCOM method ID"],
        "context_phrases": ["MSRPC operation number", "which RPC operation was called"],
    },
    "payload.smb_headers.msrpc_pkt_type": {
        "synonyms": ["MSRPC packet type", "RPC PDU type", "RPC bind call response type"],
        "context_phrases": ["MSRPC packet type", "is this an RPC bind or call"],
    },
    "payload.smb_headers.msrpc_service_name": {
        "synonyms": ["MSRPC service name", "RPC service", "Windows service via RPC", "DCOM service name"],
        "context_phrases": ["MSRPC service name", "which Windows service is being called via RPC"],
    },
    "payload.smb_headers.smb_command": {
        "synonyms": ["SMB command", "SMB1 operation", "SMB request type", "CIFS command"],
        "context_phrases": ["SMB command used", "type of SMB1 operation"],
    },
    "payload.smb_headers.smb_command.keyword": {
        "synonyms": ["exact SMB command", "SMB1 command raw"],
        "context_phrases": ["exact match on SMB command"],
    },
    "payload.smb_headers.smb_filename": {
        "synonyms": ["SMB file name", "CIFS filename", "file accessed via SMB", "SMB1 file name"],
        "context_phrases": ["filename in SMB session", "file accessed over SMB1"],
    },
    "payload.smb_headers.smb_filename.keyword": {
        "synonyms": ["exact SMB filename", "SMB1 filename raw"],
        "context_phrases": ["exact match on SMB filename"],
    },
    "payload.smb_headers.smb_path": {
        "synonyms": ["SMB path", "CIFS path", "network share path", "SMB1 file path", "UNC path"],
        "context_phrases": ["SMB file path", "network share path accessed"],
    },
    "payload.smb_headers.smb2_command": {
        "synonyms": ["SMB2 command", "SMB2 operation", "SMB2 request type"],
        "context_phrases": ["SMB2 command used", "type of SMB2 operation"],
    },
    "payload.smb_headers.smb2_command.keyword": {
        "synonyms": ["exact SMB2 command", "SMB2 command raw"],
        "context_phrases": ["exact match on SMB2 command"],
    },
    "payload.smb_headers.smb2_filename": {
        "synonyms": ["SMB2 file name", "file accessed via SMB2"],
        "context_phrases": ["filename in SMB2 session"],
    },
    "payload.smb_headers.smb2_filename.keyword": {
        "synonyms": ["exact SMB2 filename", "SMB2 filename raw"],
        "context_phrases": ["exact match on SMB2 filename"],
    },
    "payload.smb_headers.smb2_name": {
        "synonyms": ["SMB2 name", "SMB2 resource name", "SMB2 object name"],
        "context_phrases": ["SMB2 name field", "name of resource in SMB2"],
    },
    "payload.smb_headers.smb2_path": {
        "synonyms": ["SMB2 path", "network share path SMB2", "SMB2 file path", "UNC path SMB2"],
        "context_phrases": ["SMB2 file path", "network share path in SMB2 session"],
    },
    "payload.smb_headers.smb2_path.keyword": {
        "synonyms": ["exact SMB2 path", "SMB2 path raw"],
        "context_phrases": ["exact match on SMB2 path"],
    },
    "recon.file_names": {
        "synonyms": ["recon file names", "reconnaissance filenames", "files discovered in recon"],
        "context_phrases": ["file names found in reconnaissance"],
    },
    "recon.file_types": {
        "synonyms": ["recon file types", "file types in reconnaissance", "file formats discovered"],
        "context_phrases": ["file types found in recon"],
    },
    "recon.has_content": {
        "synonyms": ["recon has data", "reconnaissance content flag", "has recon data"],
        "context_phrases": ["does recon have content", "is recon data present"],
    },
    "recon.path": {
        "synonyms": ["recon path", "reconnaissance file path", "recon directory path"],
        "context_phrases": ["path found in recon", "directory or file path from reconnaissance"],
    },
    "recon.possible_codecs": {
        "synonyms": ["recon codecs", "possible audio video codecs", "detected codecs in recon"],
        "context_phrases": ["possible codecs from recon", "audio or video codecs detected in reconnaissance"],
    },
    "remark": {
        "synonyms": ["general remark", "note", "comment", "annotation", "free text remark", "analyst note"],
        "context_phrases": ["general remarks on this record", "analyst notes", "free text comments"],
    },
    "remarks.comment": {
        "synonyms": ["remark comment", "remarks text", "comment field in remarks"],
        "context_phrases": ["comment in the remarks object"],
    },
    "rtp_type_list": {
        "synonyms": ["RTP types", "RTP payload types", "RTP codec list", "real time protocol type list"],
        "context_phrases": ["RTP payload type list", "types of RTP streams"],
    },
    "session.app_group": {
        "synonyms": ["application group", "app category", "application family", "app group label", "traffic category"],
        "context_phrases": ["what application group is this", "category of application"],
    },
    "session.application": {
        "synonyms": ["application name", "app name", "detected application", "protocol application", "service name"],
        "context_phrases": ["what application was used", "filter by application name"],
    },
    "session.call_status": {
        "synonyms": ["call status", "VoIP call result", "call outcome", "session call result", "call state"],
        "context_phrases": ["status of the call", "was the call answered"],
    },
    "session.client_tcp_initial_flags": {
        "synonyms": ["client TCP flags", "TCP handshake client flags", "initial TCP flags from client", "SYN flags"],
        "context_phrases": ["TCP flags from client at session start"],
    },
    "session.dpi_protocol": {
        "synonyms": ["DPI protocol", "deep packet inspection protocol", "application layer protocol", "identified protocol"],
        "context_phrases": ["protocol identified by DPI", "deep packet inspection result"],
    },
    "session.dst_os": {
        "synonyms": ["destination OS", "destination operating system", "target OS", "server OS"],
        "context_phrases": ["operating system of destination", "what OS is the destination running"],
    },
    "session.dst_tcp_initial_flags": {
        "synonyms": ["destination TCP flags", "TCP handshake destination flags", "initial TCP flags to destination"],
        "context_phrases": ["TCP flags to destination at session start"],
    },
    "session.duration": {
        "synonyms": ["session duration", "connection duration", "session length", "how long", "session time", "elapsed time"],
        "context_phrases": ["how long did the session last", "session duration in milliseconds"],
    },
    "session.id": {
        "synonyms": ["session ID", "session identifier", "connection ID", "flow ID", "session key"],
        "context_phrases": ["what is the session ID", "find session by ID"],
    },
    "session.index_name": {
        "synonyms": ["index name", "Elasticsearch index", "data index name", "storage index"],
        "context_phrases": ["which index does this session belong to"],
    },
    "session.input_file_name": {
        "synonyms": ["input file", "source file name", "capture file", "PCAP file name"],
        "context_phrases": ["which input file was this from", "source PCAP file name"],
    },
    "session.possible_data_type": {
        "synonyms": ["possible data type", "data type guess", "likely data type", "inferred data type"],
        "context_phrases": ["what data type is this session", "inferred data type"],
    },
    "session.possible_user_action": {
        "synonyms": ["user action", "possible action", "detected user activity", "inferred user behaviour"],
        "context_phrases": ["what user action was detected", "inferred user behaviour in session"],
    },
    "session.probe_id": {
        "synonyms": ["probe ID", "probe identifier", "sensor ID", "capture probe ID", "monitor probe"],
        "context_phrases": ["which probe captured this session", "probe identifier"],
    },
    "session.probe_ip": {
        "synonyms": ["probe IP", "sensor IP address", "capture probe IP", "monitoring sensor IP"],
        "context_phrases": ["IP address of the probe", "sensor IP address"],
    },
    "session.protocol": {
        "synonyms": ["session protocol", "transport protocol", "network protocol", "communication protocol"],
        "context_phrases": ["what protocol is this session", "filter by protocol"],
    },
    "session.received_bytes": {
        "synonyms": ["bytes received", "downloaded bytes", "inbound bytes", "received data volume", "download size"],
        "context_phrases": ["how many bytes were received", "inbound data volume"],
    },
    "session.received_packets": {
        "synonyms": ["packets received", "inbound packets", "received packet count"],
        "context_phrases": ["how many packets were received", "inbound packet count"],
    },
    "session.server_tcp_initial_flags": {
        "synonyms": ["server TCP flags", "TCP handshake server flags", "SYN ACK flags"],
        "context_phrases": ["TCP flags from server at session start"],
    },
    "session.src_os": {
        "synonyms": ["source OS", "source operating system", "client OS", "originating OS"],
        "context_phrases": ["operating system of source", "what OS is the source running"],
    },
    "session.src_tcp_initial_flags": {
        "synonyms": ["source TCP flags", "TCP handshake source flags"],
        "context_phrases": ["TCP flags from source at session start"],
    },
    "session.start_time": {
        "synonyms": ["session start", "connection start time", "session begin time", "when session started", "flow start"],
        "context_phrases": ["when did the session start", "filter by session start time"],
    },
    "session.term_clause": {
        "synonyms": ["termination clause", "session end reason", "why session ended", "termination reason"],
        "context_phrases": ["why did the session terminate", "session end reason code"],
    },
    "session.total_bytes": {
        "synonyms": ["total bytes", "total data transferred", "session bytes", "bandwidth used", "total data volume"],
        "context_phrases": ["total bytes transferred in session", "session data volume"],
    },
    "session.total_packets": {
        "synonyms": ["total packets", "packet count", "total packet count", "all packets in session"],
        "context_phrases": ["total number of packets in session"],
    },
    "session.total_payload_size": {
        "synonyms": ["payload size", "total payload", "application data size", "payload bytes", "content size"],
        "context_phrases": ["total payload size in session", "how much payload was transferred"],
    },
    "session.transmitted_bytes": {
        "synonyms": ["bytes sent", "uploaded bytes", "outbound bytes", "transmitted data", "sent data volume"],
        "context_phrases": ["how many bytes were sent", "outbound data volume"],
    },
    "session.transmitted_packets": {
        "synonyms": ["packets sent", "outbound packets", "transmitted packet count"],
        "context_phrases": ["how many packets were sent", "outbound packet count"],
    },
    "session.url_category": {
        "synonyms": ["URL category", "web category", "URL classification", "website category", "web filter category"],
        "context_phrases": ["what category is this URL", "web filtering category"],
    },
    "session.url_remark": {
        "synonyms": ["URL remark", "URL notes", "URL annotation", "comments on URL"],
        "context_phrases": ["remarks about the URL"],
    },
    "speaker_match": {
        "synonyms": ["speaker identification", "voice match", "speaker recognition", "voice fingerprint match", "biometric speaker match"],
        "context_phrases": ["speaker identification result", "voice matched to a speaker"],
    },
    "speaker_score": {
        "synonyms": ["speaker match score", "voice match confidence", "speaker recognition score", "biometric match score"],
        "context_phrases": ["how confident is the speaker match", "speaker recognition confidence score"],
    },
    "system_name": {
        "synonyms": ["system name", "system identifier", "platform name", "monitoring system", "system label"],
        "context_phrases": ["name of the system", "which system generated this"],
    },
    "text": {
        "synonyms": ["general text", "content text", "body text", "free text content", "text data"],
        "context_phrases": ["general text content of the record", "body text"],
    },
    "text_summary": {
        "synonyms": ["text summary", "content summary", "abstract", "brief summary", "text overview"],
        "context_phrases": ["summary of the text content", "brief overview of content"],
    },
    "transcripted_text": {
        "synonyms": ["transcription", "speech to text", "voice transcription", "call transcript", "audio transcription"],
        "context_phrases": ["transcribed text from audio", "call transcript", "speech recognition output"],
    },
    "translated_processed": {
        "synonyms": ["translation processed flag", "was translated", "translation done", "translation status"],
        "context_phrases": ["was this record translated", "translation processing status"],
    },
    "translated_text": {
        "synonyms": ["translated content", "translation output", "translated version", "language translation"],
        "context_phrases": ["translated version of the text", "what is the translation"],
    },
    "translated_text_summary": {
        "synonyms": ["translation summary", "translated summary", "translated abstract"],
        "context_phrases": ["summary of the translated text"],
    },
    "transport.dst_port": {
        "synonyms": ["destination port", "dst port", "target port", "receiver port", "service port"],
        "context_phrases": ["what is the destination port", "filter by destination port", "which port was connected to"],
    },
    "transport.protocol": {
        "synonyms": ["transport protocol", "layer 4 protocol", "TCP UDP", "transport layer protocol"],
        "context_phrases": ["what is the transport protocol", "TCP or UDP"],
    },
    "transport.src_port": {
        "synonyms": ["source port", "src port", "originating port", "client port", "ephemeral port"],
        "context_phrases": ["what is the source port", "filter by source port"],
    },
    "commu_identifiers": {
        "synonyms": ["communication identifiers", "comm IDs", "communication IDs", "session communication identifiers", "contact identifiers"],
        "context_phrases": ["communication identifiers in this session", "IDs used for communication"],
    },
    "endpoints_swapped_with_confidence": {
        "synonyms": ["endpoints swapped", "src dst swapped", "direction swapped", "swapped endpoints flag"],
        "context_phrases": ["were the endpoints swapped", "source destination direction swapped"],
    },
    "malware_remarks.signature": {
        "synonyms": ["malware signature", "virus signature", "threat signature", "malware detection rule", "IDS signature"],
        "context_phrases": ["malware signature detected", "which malware signature matched"],
    },
}