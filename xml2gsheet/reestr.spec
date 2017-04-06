# -*- mode: python -*-

block_cipher = None


a = Analysis(['gui_main.py'],
             pathex=['C:\\Users\\maks2020\\projects\\xml_in_gsheet\\xml2gsheet',
             r'C:\Users\maks2020\projects\xml_in_gsheet\env_xml2gsheet\Lib\site-packages',
             r'C:\Users\maks2020\projects\xml_in_gsheet\static'],
             binaries=[],
             datas=[],
             hiddenimports=['httplib2',
                            'bs4',
                            'apiclient',
                            'oauth2client',
                            'selenium',
                            'selenium.webdriver',
                            'gbot',
                            'gui_utils',
                            'parser_html',
                            'parse_xml',
                            'sheetapi',
                            'srch_utils',
                            'xml2gsheet',
                             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='gui_main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='gui_main')
