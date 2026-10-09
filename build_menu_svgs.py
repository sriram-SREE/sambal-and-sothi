import os, base64

logo_path = r'C:\Users\srira\.gemini\antigravity\scratch\sambal-sothi\assets\img\brand-logo.png'
b64_logo = ''
if os.path.exists(logo_path):
    with open(logo_path, 'rb') as f:
        b64_logo = base64.b64encode(f.read()).decode('utf-8')

data_uri = f'data:image/png;base64,{b64_logo}' if b64_logo else 'brand-logo.png'

pages_data = [
    # P1: Cover Page with Official Chef Logo
    f'''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <defs>
        <clipPath id='p1-chef-clip'>
          <circle cx='400' cy='320' r='90'/>
        </clipPath>
      </defs>
      <rect width='600' height='850' fill='#2E0707'/>
      <path d='M250,0 Q600,425 250,850 L600,850 L600,0 Z' fill='#3F0D0D'/>
      <path d='M250,0 Q600,425 250,850' fill='none' stroke='#D4A24C' stroke-width='3'/>
      <circle cx='400' cy='320' r='92' fill='#5C1414' stroke='#C1272D' stroke-width='4'/>
      <circle cx='400' cy='320' r='98' fill='none' stroke='#D4A24C' stroke-width='2' stroke-dasharray='4 4'/>
      <image href='{data_uri}' x='308' y='228' width='184' height='184' clip-path='url(#p1-chef-clip)'/>
      <path d='M320,450 L480,450' stroke='#D4A24C' stroke-width='2'/>
      <text x='400' y='520' text-anchor='middle' fill='#F7F0E4' font-family='Cormorant Garamond, serif' font-size='56' letter-spacing='4'>MENU</text>
      <path d='M320,550 L480,550' stroke='#D4A24C' stroke-width='2'/>
    </svg>''',

    # P2: Specials
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Sambal &amp; Sothi Special</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Tau Sambal</text><line x1='165' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='180'>Chicken Sambal</text><line x1='205' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.50</text>
        <text x='65' y='215'>Chicken Kichap</text><line x1='195' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='250'>Mutton Kichap</text><line x1='190' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='285'>Quail Egg Sambal</text><line x1='215' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='320'>Ikan Bilis Sambal</text><line x1='210' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='355'>Ikan Bilis &amp; Kadai Muttai Sambal</text><line x1='330' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.00</text>
        <text x='65' y='390'>Ikan Bilis Petai</text><line x1='190' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.50</text>
        <text x='65' y='425'>Egg Sambal</text><line x1='170' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='460'>Sotong Sambal</text><line x1='195' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.00</text>
        <text x='65' y='495'>Prawn Sambal</text><line x1='190' y1='491' x2='445' y2='491' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='495' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.00</text>
        <text x='65' y='530'>Hotdog Sambal</text><line x1='195' y1='526' x2='445' y2='526' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='530' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.00</text>
        <text x='65' y='565'>Fish Sambal</text><line x1='170' y1='561' x2='445' y2='561' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='565' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.00</text>
        <text x='65' y='600'>Fishball Sambal</text><line x1='190' y1='596' x2='445' y2='596' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='600' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.00</text>
        <text x='65' y='635'>Kichap Egg</text><line x1='165' y1='631' x2='445' y2='631' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='635' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.20</text>
        <text x='65' y='670'>Fish Kichap</text><line x1='165' y1='666' x2='445' y2='666' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='670' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.00</text>
        <text x='65' y='705'>Sardine Sambal</text><line x1='195' y1='701' x2='445' y2='701' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='705' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='740'>Chicken Rendang</text><line x1='210' y1='736' x2='445' y2='736' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='740' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='775'>Mutton Rendang</text><line x1='200' y1='771' x2='445' y2='771' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='775' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.50</text>
      </g>
    </svg>''',

    # P3: Indian Classic
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Indian Classic</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='160'>White Rice</text><line x1='160' y1='156' x2='445' y2='156' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='160' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.20</text>
        <text x='65' y='210'>Biriyani Rice</text><line x1='170' y1='206' x2='445' y2='206' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='210' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='260'>Idli (2 Pcs)</text><line x1='165' y1='256' x2='445' y2='256' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='260' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='310'>Vadai (1 Pc)</text><line x1='170' y1='306' x2='445' y2='306' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='310' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.20</text>
        <text x='65' y='360'>Poori (2 Pcs)</text><line x1='170' y1='356' x2='445' y2='356' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='360' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='410'>Chapati (1 Pc)</text><line x1='180' y1='406' x2='445' y2='406' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='410' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.50</text>
        <text x='65' y='460'>Appam (Plain)</text><line x1='180' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.00</text>
        <text x='65' y='510'>Egg Appam</text><line x1='165' y1='506' x2='445' y2='506' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='510' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='560'>Milk Appam</text><line x1='165' y1='556' x2='445' y2='556' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='560' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='610'>String Hopper (3 Pcs)</text><line x1='240' y1='606' x2='445' y2='606' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='610' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='660'>Puttu (Plain)</text><line x1='170' y1='656' x2='445' y2='656' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='660' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
      </g>
    </svg>''',

    # P4: Thosai
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Thosai Delights</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Plain Thosai</text><line x1='170' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.00</text>
        <text x='65' y='180'>Egg Thosai</text><line x1='160' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.80</text>
        <text x='65' y='215'>Onion Thosai</text><line x1='175' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='250'>Masala Thosai</text><line x1='180' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='285'>Ghee Thosai</text><line x1='170' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.20</text>
        <text x='65' y='320'>Paper Thosai</text><line x1='175' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.80</text>
        <text x='65' y='355'>Cheese Thosai</text><line x1='185' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.00</text>
        <text x='65' y='390'>Butter Thosai</text><line x1='175' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='425'>Rava Thosai</text><line x1='170' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.20</text>
        <text x='65' y='460'>Rava Masala Thosai</text><line x1='235' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.20</text>
        <text x='65' y='495'>Onion Rava Thosai</text><line x1='220' y1='491' x2='445' y2='491' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='495' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.00</text>
        <text x='65' y='530'>Ghee Masala Thosai</text><line x1='230' y1='526' x2='445' y2='526' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='530' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='565'>Podhi Thosai</text><line x1='175' y1='561' x2='445' y2='561' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='565' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.20</text>
        <text x='65' y='600'>Egg Onion Thosai</text><line x1='215' y1='596' x2='445' y2='596' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='600' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.80</text>
        <text x='65' y='635'>Egg Masala Thosai</text><line x1='225' y1='631' x2='445' y2='631' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='635' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.20</text>
        <text x='65' y='670'>Uthappam (Plain)</text><line x1='205' y1='666' x2='445' y2='666' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='670' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='705'>Onion Uthappam</text><line x1='200' y1='701' x2='445' y2='701' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='705' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='740'>Tomato Uthappam</text><line x1='210' y1='736' x2='445' y2='736' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='740' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.80</text>
      </g>
    </svg>''',

    # P5: Fried VEG & Non-VEG
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Fried Veg &amp; Non-Veg</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Fried Tofu</text><line x1='155' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='180'>Fried Cauliflower (Gobi 65)</text><line x1='290' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='215'>Fried Brinjal</text><line x1='165' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='250'>Fried Mushroom</text><line x1='195' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='285'>Fried Bittergourd</text><line x1='195' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='320'>Fried Ladies Finger</text><line x1='215' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='355'>Chicken 65 (Boneless)</text><line x1='245' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='390'>Fried Chicken (1 Pc)</text><line x1='220' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.00</text>
        <text x='65' y='425'>Fried Fish (1 Pc)</text><line x1='195' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.50</text>
        <text x='65' y='460'>Fried Prawns</text><line x1='175' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.50</text>
        <text x='65' y='495'>Fried Squid (Sotong 65)</text><line x1='255' y1='491' x2='445' y2='491' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='495' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.50</text>
        <text x='65' y='530'>Fried Fishball (5 Pcs)</text><line x1='235' y1='526' x2='445' y2='526' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='530' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='565'>Fried Hotdog (3 Pcs)</text><line x1='225' y1='561' x2='445' y2='561' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='565' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='600'>Fried Egg (Sunnyside)</text><line x1='235' y1='596' x2='445' y2='596' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='600' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.20</text>
        <text x='65' y='635'>Omelette (Plain)</text><line x1='195' y1='631' x2='445' y2='631' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='635' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.00</text>
        <text x='65' y='670'>Onion Omelette</text><line x1='195' y1='666' x2='445' y2='666' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='670' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='705'>Prawn Omelette</text><line x1='205' y1='701' x2='445' y2='701' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='705' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
      </g>
    </svg>''',

    # P6: Prata
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Prata Selection</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Plain Prata (2 Pcs Min)</text><line x1='245' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.40</text>
        <text x='65' y='180'>Egg Prata</text><line x1='155' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.20</text>
        <text x='65' y='215'>Onion Prata</text><line x1='165' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.20</text>
        <text x='65' y='250'>Egg Onion Prata</text><line x1='205' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='285'>Cheese Prata</text><line x1='175' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.20</text>
        <text x='65' y='320'>Cheese Egg Prata</text><line x1='215' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.00</text>
        <text x='65' y='355'>Cheese Onion Prata</text><line x1='225' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.00</text>
        <text x='65' y='390'>Garlic Prata</text><line x1='165' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='425'>Garlic Egg Prata</text><line x1='205' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.20</text>
        <text x='65' y='460'>Butter Prata</text><line x1='165' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='495'>Plaster Prata (Egg on Top)</text><line x1='265' y1='491' x2='445' y2='491' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='495' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='530'>Mushroom Prata</text><line x1='205' y1='526' x2='445' y2='526' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='530' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.20</text>
        <text x='65' y='565'>Mushroom Cheese Prata</text><line x1='265' y1='561' x2='445' y2='561' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='565' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.20</text>
        <text x='65' y='600'>Banana Prata</text><line x1='175' y1='596' x2='445' y2='596' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='600' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='635'>Chocolate Prata</text><line x1='195' y1='631' x2='445' y2='631' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='635' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='670'>Coin Prata (Set of 6)</text><line x1='225' y1='666' x2='445' y2='666' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='670' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.50</text>
        <text x='65' y='705'>Mutton Murtabak</text><line x1='210' y1='701' x2='445' y2='701' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='705' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$9.50</text>
        <text x='65' y='740'>Chicken Murtabak</text><line x1='215' y1='736' x2='445' y2='736' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='740' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$8.50</text>
      </g>
    </svg>''',

    # P7: Kothu Prata & Egg Dishes
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Kothu &amp; Egg Specialties</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Veg Kothu Prata</text><line x1='200' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.50</text>
        <text x='65' y='180'>Egg Kothu Prata</text><line x1='200' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='215'>Chicken Kothu Prata</text><line x1='235' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$8.00</text>
        <text x='65' y='250'>Mutton Kothu Prata</text><line x1='225' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$9.00</text>
        <text x='65' y='285'>Seafood Kothu Prata</text><line x1='235' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$9.50</text>
        <text x='65' y='320'>Boiled Egg (2 Pcs)</text><line x1='205' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.80</text>
        <text x='65' y='355'>Half Boiled Egg (2 Pcs)</text><line x1='245' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.00</text>
        <text x='65' y='390'>Egg Podimass (Scrambled)</text><line x1='275' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='425'>Kalaki (Soft Omelette)</text><line x1='235' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.20</text>
        <text x='65' y='460'>Chicken Gravy Kalaki</text><line x1='245' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.80</text>
        <text x='65' y='495'>Mutton Gravy Kalaki</text><line x1='240' y1='491' x2='445' y2='491' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='495' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='530'>Fish Gravy Kalaki</text><line x1='215' y1='526' x2='445' y2='526' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='530' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.80</text>
      </g>
    </svg>''',

    # P8: Gravy & Curry
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Gravies &amp; Curries</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Chicken Curry Gravy</text><line x1='235' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='180'>Fish Curry Gravy</text><line x1='205' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='215'>Mutton Curry Gravy</text><line x1='225' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.00</text>
        <text x='65' y='250'>Vegetable Kurma</text><line x1='210' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.00</text>
        <text x='65' y='285'>Sambar Gravy</text><line x1='185' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='320'>Signature White Sothi</text><line x1='245' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='355'>Mutton Bone Marrow Curry</text><line x1='290' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$12.50</text>
        <text x='65' y='390'>Crab Curry (Seasonal)</text><line x1='245' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$14.00</text>
        <text x='65' y='425'>Prawn Curry</text><line x1='175' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$8.50</text>
      </g>
    </svg>''',

    # P9: Goreng
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Goreng Specialties</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Mee Goreng (Veg)</text><line x1='215' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='180'>Mee Goreng (Egg)</text><line x1='215' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.00</text>
        <text x='65' y='215'>Mee Goreng (Chicken)</text><line x1='245' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='250'>Mee Goreng (Mutton)</text><line x1='235' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.50</text>
        <text x='65' y='285'>Mee Goreng (Seafood)</text><line x1='245' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$8.00</text>
        <text x='65' y='320'>Nasi Goreng (Veg)</text><line x1='215' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='355'>Nasi Goreng (Chicken)</text><line x1='255' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='390'>Nasi Goreng (Mutton)</text><line x1='245' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.50</text>
        <text x='65' y='425'>Maggi Goreng (Plain)</text><line x1='225' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='460'>Maggi Goreng (Chicken)</text><line x1='265' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='495'>Kway Teow Goreng</text><line x1='220' y1='491' x2='445' y2='491' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='495' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.50</text>
        <text x='65' y='530'>Bee Hoon Goreng</text><line x1='210' y1='526' x2='445' y2='526' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='530' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.50</text>
      </g>
    </svg>''',

    # P10: Briyani & Set Meals
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Biriyani &amp; Set Meals</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='160'>Chicken Dum Biriyani</text><line x1='245' y1='156' x2='445' y2='156' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='160' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$10.80</text>
        <text x='65' y='210'>Mutton Dum Biriyani</text><line x1='235' y1='206' x2='445' y2='206' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='210' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$12.80</text>
        <text x='65' y='260'>Fish Dum Biriyani</text><line x1='215' y1='256' x2='445' y2='256' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='260' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$11.80</text>
        <text x='65' y='310'>Egg Biriyani Set</text><line x1='195' y1='306' x2='445' y2='306' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='310' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.50</text>
        <text x='65' y='360'>Vegetable Biriyani</text><line x1='210' y1='356' x2='445' y2='356' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='360' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.00</text>
        <text x='65' y='410'>South Indian Veg Thali Meal</text><line x1='290' y1='406' x2='445' y2='406' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='410' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.50</text>
        <text x='65' y='460'>Non-Veg Thali Meal (Chicken)</text><line x1='300' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$9.50</text>
        <text x='65' y='510'>Non-Veg Thali Meal (Mutton)</text><line x1='290' y1='506' x2='445' y2='506' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='510' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$10.50</text>
      </g>
    </svg>''',

    # P11: Hot Drinks
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Hot Beverages</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Teh Tarik (Pull Tea)</text><line x1='225' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.60</text>
        <text x='65' y='180'>Teh C (Tea with Milk)</text><line x1='235' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.60</text>
        <text x='65' y='215'>Teh O (Black Tea)</text><line x1='205' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.30</text>
        <text x='65' y='250'>Kopi (Coffee with Milk)</text><line x1='245' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.60</text>
        <text x='65' y='285'>Bru Coffee (Hot Milk)</text><line x1='235' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.20</text>
        <text x='65' y='320'>Masala Chai (Spiced Tea)</text><line x1='255' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='355'>Ginger Tea (Halia)</text><line x1='215' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.80</text>
        <text x='65' y='390'>Teh Halia (Ginger Tea)</text><line x1='235' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$1.80</text>
        <text x='65' y='425'>Hot Milo</text><line x1='145' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.00</text>
        <text x='65' y='460'>Hot Horlicks</text><line x1='165' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.20</text>
        <text x='65' y='495'>Hot Nescafe</text><line x1='165' y1='491' x2='445' y2='491' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='495' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.00</text>
        <text x='65' y='530'>Fresh Cow Milk (Hot)</text><line x1='235' y1='526' x2='445' y2='526' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='530' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='565'>Sukku Coffee (Herbal)</text><line x1='235' y1='561' x2='445' y2='561' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='565' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.20</text>
      </g>
    </svg>''',

    # P12: Cold Drinks
    '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <rect width='600' height='850' fill='#2E0707'/>
      <rect x='35' y='35' width='530' height='780' fill='none' stroke='#D4A24C' stroke-width='1.5'/>
      <text x='300' y='90' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-size='34' font-weight='600'>Cold Beverages &amp; Shakes</text>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='16'>
        <text x='65' y='145'>Iced Teh Tarik</text><line x1='175' y1='141' x2='445' y2='141' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='145' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.20</text>
        <text x='65' y='180'>Iced Kopi</text><line x1='145' y1='176' x2='445' y2='176' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='180' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.20</text>
        <text x='65' y='215'>Iced Milo</text><line x1='145' y1='211' x2='445' y2='211' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='215' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='250'>Milo Dinosaur (Extra Powder)</text><line x1='290' y1='246' x2='445' y2='246' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='250' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.80</text>
        <text x='65' y='285'>Milo Godzilla (Powder &amp; Ice Cream)</text><line x1='335' y1='281' x2='445' y2='281' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='285' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.00</text>
        <text x='65' y='320'>Fresh Lime Juice</text><line x1='195' y1='316' x2='445' y2='316' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='320' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.80</text>
        <text x='65' y='355'>Lime Juice with Juice Syrup</text><line x1='275' y1='351' x2='445' y2='351' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='355' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.20</text>
        <text x='65' y='390'>Sirap Bandung (Rose Milk)</text><line x1='265' y1='386' x2='445' y2='386' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='390' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='425'>Sweet Lassi (Yogurt)</text><line x1='215' y1='421' x2='445' y2='421' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='425' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='460'>Mango Lassi (Fresh Mango)</text><line x1='270' y1='456' x2='445' y2='456' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='460' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='495'>Salted Lassi</text><line x1='165' y1='491' x2='445' y2='491' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='495' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$3.50</text>
        <text x='65' y='530'>Spiced Buttermilk (Neer Moru)</text><line x1='280' y1='526' x2='445' y2='526' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='530' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.50</text>
        <text x='65' y='565'>Canned Soft Drinks</text><line x1='215' y1='561' x2='445' y2='561' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='565' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$2.00</text>
        <text x='65' y='600'>Fresh Coconut Water</text><line x1='225' y1='596' x2='445' y2='596' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='600' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$4.50</text>
        <text x='65' y='635'>Avocado Milkshake</text><line x1='215' y1='631' x2='445' y2='631' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='635' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$5.50</text>
        <text x='65' y='670'>Vanilla Milkshake</text><line x1='205' y1='666' x2='445' y2='666' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='670' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$6.00</text>
        <text x='65' y='705'>Chocolate Milkshake</text><line x1='220' y1='701' x2='445' y2='701' stroke='rgba(212,162,76,0.4)' stroke-dasharray='2 4'/><text x='535' y='705' text-anchor='end' fill='#FFD98A' font-weight='bold' font-size='18'>$7.00</text>
      </g>
    </svg>''',

    # P13: Back Cover Page with Official Chef Logo
    f'''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 850' width='100%' height='100%'>
      <defs>
        <clipPath id='p13-chef-clip'>
          <circle cx='300' cy='280' r='90'/>
        </clipPath>
      </defs>
      <rect width='600' height='850' fill='#2E0707'/>
      <circle cx='300' cy='280' r='92' fill='#5C1414' stroke='#C1272D' stroke-width='4'/>
      <circle cx='300' cy='280' r='98' fill='none' stroke='#D4A24C' stroke-width='2' stroke-dasharray='4 4'/>
      <image href='{data_uri}' x='208' y='188' width='184' height='184' clip-path='url(#p13-chef-clip)'/>
      <g fill='#F7F0E4' font-family='DM Sans, sans-serif' font-size='18' text-anchor='middle'>
        <text x='300' y='440' fill='#F0C46A'>+65 8782 9193 / +65 8398 3865</text>
        <text x='300' y='485'>Sambalandsothi@gmail.com</text>
        <text x='300' y='530'>41 Chander Road, Singapore 219543</text>
        <text x='300' y='575'>@sambalandsothi</text>
        <text x='300' y='620' fill='#C9B79E'>Business Hours 10.30 am – 10.30 pm</text>
      </g>
      <text x='300' y='720' text-anchor='middle' fill='#F0C46A' font-family='Cormorant Garamond, serif' font-style='italic' font-size='24'>Local Style Indian Food With a Kick of Spice</text>
    </svg>'''
]

out_dir = r'C:\Users\srira\.gemini\antigravity\scratch\sambal-sothi\assets\img'
for i, page_svg in enumerate(pages_data, start=1):
    fp = os.path.join(out_dir, f'menu-p{i}.svg')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(page_svg)

print('Updated build_menu_svgs.py with embedded Base64 official chef logo.')
