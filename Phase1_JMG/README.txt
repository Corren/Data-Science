README.TXT
 
Jonathan Gregory
CS 490
Project: Phase 1
 
Requirement:
Goal
Collect Tweets using Twitter’s Streaming APIs (e.g., 100K Tweets)
https://dev.twitter.com/docs/streaming-apis
Search online for documentation and code; feel free to use any online code
Write code to extract all the hashtags in the collected tweets
Run the Wordcount example in Apache Hadoop on the file containing hashtags. Collect the output and log files from Hadoop. Add a README file with your submission.
What to submit?
Your code and the output and log files
 
Notes:
This is the result of streaming twitter with the following keywords:
AAAP,AABA,AAL,AAME,AAOI,AAON,AAPL,AAWW,AAXJ,AAXN,ABAC,ABAX,ABCB,ABCD,ABDC,ABEO,ABEOW,ABIL,ABIO,ABLX,ABMD,ABTX,ABUS,ACAD,ACBI,ACER,ACERW,ACET,ACFC,ACGL,ACGLO,ACGLP,ACHC,ACHN,ACHV,ACIA,ACIU,ACIW,ACLS,ACMR,ACNB,ACOR,ACRS,ACRX,ACSF,ACST,ACT,ACTA,ACTG,ACWI,ACWX,ACXM,ADAP,ADBE,ADES,ADI,ADMA,ADMP,ADMS,ADOM,ADP,ADRA,ADRD,ADRE,ADRO,ADRU,ADSK,ADTN,ADUS,ADVM,ADXS,ADXSW,AEGN,AEHR,AEIS,AEMD,AERI,AETI,AEY,AEZS,AFAM,AFH,AFHBL,AFMD,AFSI,AGEN,AGFS,AGFSW,AGII,AGIIL,AGIO,AGLE,AGNC,AGNCB,AGNCN,AGND,AGRX,AGTC,AGYS,AGZD,AHGP,AHPA,AHPAU,AHPAW,AHPI,AIA,AIMC,AIMT,AINV,AIPT,AIRG,AIRR,AIRT,AKAM,AKAO,AKBA,AKCA,AKER,AKRX,AKTS,AKTX,ALBO,ALCO,ALDR,ALDX,ALGN,ALGT,ALIM,ALJJ,ALKS,ALLT,ALNA,ALNY,ALOG,ALOT,ALPN,ALQA,ALRM,ALRN,ALSK,ALT,ALTR,ALTY,ALXN,AMAG,AMAT,AMBA,AMBC,AMBCW,AMCA,AMCN,AMCX,AMD,AMDA,AMED,AMEH,AMGN,AMKR,AMMA,AMNB,AMOT,AMPH,AMR,AMRB,AMRH,AMRHW,AMRK,AMRN,AMRS,AMRWW,AMSC,AMSF,AMSWA,AMTD,AMTX,AMWD,AMZN,ANAB,ANAT,ANCB,ANCX,ANDA,ANDAR,ANDAW,ANDE,ANGI,ANGO,ANIK,ANIP,ANSS,ANTH,ANY,AOBC,AOSL,APDN,APDNW,APEI,APEN,APLP,APLS,APOG,APOP,APOPW,APPF,APPN,APPS,APRI,APTI,APTO,APVO,APWC,AQB,AQMS,AQXP,ARAY,ARCB,ARCC,ARCI,ARCT,ARCW,ARDM,ARDX,AREX,ARGS,ARGX,ARII,ARKR,ARLP,ARLZ,ARMO,ARNA,AROW,ARQL,ARRS,ARRY,ARTNA,ARTW,ARTX,ARWR,ASCMA,ASET,ASFI,ASMB,ASML,ASNA,ASND,ASNS,ASPS,ASPU,ASRV,ASRVP,ASTC,ASTE,ASUR,ASV,ASYS,ATAC,ATACR,ATACU,ATAI,ATAX,ATEC,ATHN,ATHX,ATLC,ATLO,ATNI,ATNX,ATOM,ATOS,ATRA,ATRC,ATRI,ATRO,ATRS,ATSG,ATTU,ATVI,ATXI,AUBN,AUDC,AUPH,AUTO,AVAV,AVDL,AVEO,AVGO,AVGR,AVHI,AVID,AVIR,AVNW,AVXL,AVXS,AWRE,AXAS,AXDX,AXGN,AXON,AXSM,AXTI,AY,AYTU,AZPN,AZRX,BABY,BAND,BANF,BANFP,BANR,BANX,BASI,BATRA,BATRK,BBBY,BBGI,BBH,BBOX,BBRG,BBSI,BCAC,BCACR,BCACU,BCACW,BCBP,BCLI,BCOM,BCOR,BCOV,BCPC,BCRX,BCTF,BDGE,BDSI,BEAT,BECN,BELFA,BELFB,BFIN,BFIT,BFRA,BGCP,BGFV,BGNE,BHAC,BHACR,BHACW,BHBK,BHF,BIB,BICK,BIDU,BIIB,BIOC,BIOL,BIOS,BIS,BIVV,BJRI,BKCC,BKEP,BKEPP,BKNG,BKSC,BKYI,BL,BLBD,BLCM,BLCN,BLDP,BLDR,BLFS,BLIN,BLKB,BLMN,BLMT,BLNK,BLNKW,BLPH,BLRX,BLUE,BMCH,BMLP,BMRA,BMRC,BMRN,BMTC,BNCL,BNDX,BNFT,BNSO,BNTC,BNTCW,BOCH,BOFI,BOFIL,BOJA,BOKF,BOKFL,BOLD
 
These are the first 400 stock symbols as I am currently limited by twitter to 400 of my list of over 10k terms
 
I installed Hadoop on a fresh install VM of Ubuntu. I followed this guide to finish the process.
http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/
 
Using Cloudera with Apache Flume, I was able to get my data to output into several files in JSON format. That file merged.json is the result of merging 10 sample sets of data from Flume. This file was too large to submit to Turnitin, so it can be found at the following link:
https://goo.gl/RgHpk9
 
The python program called "export.py", a modified version of code written by Norman Merritt, to extract the keywords.
 
The resulting keywords file then has wordcount ran on it to produce the file renamed as wordcount.txt
 
Other resources:
https://github.com/cloudera/cdh-twitter-example
http://flume.apache.org/
http://hadoop.apache.org/


