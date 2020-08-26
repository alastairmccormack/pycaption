# coding: utf-8
from pycaption import DFXPReader, WebVTTWriter, CaptionConverter


tt = u'''<?xml version="1.0" encoding="UTF-8"?>
<tt xmlns="http://www.w3.org/ns/ttml" xmlns:tts="http://www.w3.org/ns/ttml#styling" xmlns:ttm="http://www.w3.org/ns/ttml#metadata" xmlns:ttp="http://www.w3.org/ns/ttml#parameter" xmlns:smpte="http://www.smpte-ra.org/schemas/2052-1/2010/smpte-tt" xmlns:m608="http://www.smpte-ra.org/schemas/2052-1/2010/smpte-tt#cea608" xml:lang="en" ttp:timeBase="media" ttp:frameRate="1" ttp:frameRateMultiplier="30000 1001">
<head>
<ttm:desc>SMPTE Timed Text document created by Anvato</ttm:desc>
	<metadata>
		<smpte:information xmlns:m608="http://www.smpte-ra.org/schemas/2052-1/2010/smpte-tt#cea608" origin="http://www.smpte-ra.org/schemas/2052-1/2010/smpte-tt#cea608" mode="Enhanced" m608:channel="CC1" m608:programName="/tmp/ccaR2YgS" m608:captionService="F1C1CC"/>
	</metadata>
	<styling>
		<style xml:id="basic" tts:color="white" tts:backgroundColor="black" tts:fontFamily="monospace" tts:lineHeight="100%" tts:fontSize="80%" tts:fontWeight="normal" tts:fontStyle="normal"/>
	</styling>
	<layout>
		<region xml:id="pop1" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="pop2" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="pop3" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="pop4" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="rollup1" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="rollup2" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="rollup3" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
	</layout>
</head>
	<body>
		<div>
			<p begin="00:00:08:03" end="00:00:12.19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">Cathy Hamborsky appeared</p>
		</div>
	</body>
</tt>'''

tt = u'''
<?xml version="1.0" encoding="utf-8"?>
<tt xml:lang="en" xmlns="http://www.w3.org/ns/ttml" xmlns:tts="http://www.w3.org/ns/ttml#styling"
xmlns:ttp="http://www.w3.org/ns/ttml#parameter" ttp:timeBase="media" ttp:frameRate="30">
 <head>
  <layout>
   <region tts:origin="10% 10%" xml:id="b1"/>
   <region tts:origin="40% 40%" xml:id="b2"/>
   <region tts:origin="10% 70%" xml:id="b3"/>
  </layout>
 </head>
 <body>
  <div region="bottom" xml:lang="en-US">
   <p begin="00:00:09:20" end="00:00:12.19" region="b1">
    Some text here
   </p>
   <p begin="00:04:18:2" end="2:16:8.19" region="b2">
    Some text there
   </p>
   <p begin="12:00:8:29" end="14:00:12.19" region="b3">
    Caption texts are everywhere!
   </p>
  </div>
 </body>
</tt>'''

tt = u'''
<?xml version="1.0" encoding="UTF-8"?>
<tt xmlns="http://www.w3.org/ns/ttml" xmlns:tts="http://www.w3.org/ns/ttml#styling" xmlns:ttm="http://www.w3.org/ns/ttml#metadata" xmlns:ttp="http://www.w3.org/ns/ttml#parameter" xmlns:smpte="http://www.smpte-ra.org/schemas/2052-1/2010/smpte-tt" xmlns:m608="http://www.smpte-ra.org/schemas/2052-1/2010/smpte-tt#cea608" xml:lang="en" ttp:timeBase="media" ttp:frameRate="24" ttp:frameRateMultiplier="1000 1001">
<head>
<ttm:desc>SMPTE Timed Text document created by Anvato</ttm:desc>
	<metadata>
		<smpte:information xmlns:m608="http://www.smpte-ra.org/schemas/2052-1/2010/smpte-tt#cea608" origin="http://www.smpte-ra.org/schemas/2052-1/2010/smpte-tt#cea608" mode="Enhanced" m608:channel="CC1" m608:programName="/tmp/cc6kTAUt" m608:captionService="F1C1CC"/>
	</metadata>
	<styling>
		<style xml:id="basic" tts:color="white" tts:backgroundColor="black" tts:fontFamily="monospace" tts:lineHeight="100%" tts:fontSize="80%" tts:fontWeight="normal" tts:fontStyle="normal"/>
	</styling>
	<layout>
		<region xml:id="pop1" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="pop2" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="pop3" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="pop4" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="rollup1" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="rollup2" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
		<region xml:id="rollup3" tts:backgroundColor="transparent" tts:showBackground="whenActive"/>
	</layout>
</head>
	<body>
		<div>
			<p begin="00:00:04:06" end="00:00:06:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="78% 5.33%">	&gt;&gt; Let&apos;s get our Carnivale on!</p>
			<p begin="00:00:08:21" end="00:00:10:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	&gt;&gt; Hot Dog!</p>
			<p begin="00:00:08:21" end="00:00:10:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="26% 5.33%">			&gt;&gt; Woo!</p>
			<p begin="00:00:10:18" end="00:00:12:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">&gt;&gt; Come on Dr G!</p>
			<p begin="00:00:12:02" end="00:00:14:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">		Whoop, whoo!</p>
			<p begin="00:00:14:13" end="00:00:16:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Let&apos;s toast to, new</p>
			<p begin="00:00:14:13" end="00:00:16:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	beginnings.</p>
			<p begin="00:00:16:01" end="00:00:16:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; New Beginnings.</p>
			<p begin="00:00:16:21" end="00:00:18:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	Yes! Honey, I&apos;m back.</p>
			<p begin="00:00:18:09" end="00:00:19:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	Just do this.</p>
			<p begin="00:00:19:13" end="00:00:21:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		And I came to slay.</p>
			<p begin="00:00:21:01" end="00:00:22:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="81% 5.33%">&gt;&gt; You don&apos;t wanna be round them</p>
			<p begin="00:00:21:01" end="00:00:22:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	messy girls.</p>
			<p begin="00:00:22:18" end="00:00:24:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	Let them go home and take a</p>
			<p begin="00:00:22:18" end="00:00:24:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="26% 5.33%">			shower.</p>
			<p begin="00:00:24:08" end="00:00:25:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">(Laughs)</p>
			<p begin="00:00:25:13" end="00:00:26:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">â™ªHip-hop musicâ™ª</p>
			<p begin="00:00:26:18" end="00:00:27:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	&gt;&gt; Do you want a baby?</p>
			<p begin="00:00:27:21" end="00:00:28:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Yeah.</p>
			<p begin="00:00:28:19" end="00:00:32:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">&gt;&gt; These eggs are ready to be</p>
			<p begin="00:00:28:19" end="00:00:32:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">fer-til-ized.</p>
			<p begin="00:00:32:01" end="00:00:34:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="78% 5.33%">Sure you dont want me to tickle</p>
			<p begin="00:00:32:01" end="00:00:34:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	your pickle?</p>
			<p begin="00:00:35:10" end="00:00:39:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Eugene: Toya, we are in a</p>
			<p begin="00:00:35:10" end="00:00:39:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		financial crisis.</p>
			<p begin="00:00:39:15" end="00:00:41:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Quad: Bitch who owes</p>
			<p begin="00:00:39:15" end="00:00:41:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			170,000 dollars</p>
			<p begin="00:00:41:11" end="00:00:43:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">to the damn IRS?</p>
			<p begin="00:00:43:13" end="00:00:45:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		You going to go to</p>
			<p begin="00:00:43:13" end="00:00:45:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">the big house?</p>
			<p begin="00:00:45:06" end="00:00:46:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Dr. Heavenly: You think</p>
			<p begin="00:00:45:06" end="00:00:46:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		I m mean?</p>
			<p begin="00:00:46:18" end="00:00:48:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="26% 5.33%">			Alaura:</p>
			<p begin="00:00:46:18" end="00:00:48:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	To a point!</p>
			<p begin="00:00:48:02" end="00:00:48:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		Gregory: I thought</p>
			<p begin="00:00:48:02" end="00:00:48:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		we d have</p>
			<p begin="00:00:48:17" end="00:00:50:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">a family by now.</p>
			<p begin="00:00:50:02" end="00:00:51:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Dr. Jackie: That s what</p>
			<p begin="00:00:50:02" end="00:00:51:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">marriage is all about,</p>
			<p begin="00:00:51:15" end="00:00:53:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		compromise.</p>
			<p begin="00:00:53:02" end="00:00:55:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Curtis: Compromise,</p>
			<p begin="00:00:53:02" end="00:00:55:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	boy do I know that.</p>
			<p begin="00:00:55:10" end="00:00:59:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Being a doctor is a</p>
			<p begin="00:00:55:10" end="00:00:59:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	huge responsibility.</p>
			<p begin="00:00:59:09" end="00:01:00:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I m going to get the</p>
			<p begin="00:00:59:09" end="00:01:00:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	old one out.</p>
			<p begin="00:01:00:14" end="00:01:02:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		One, two,</p>
			<p begin="00:01:00:14" end="00:01:02:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	three! Bam!</p>
			<p begin="00:01:02:02" end="00:01:05:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">You re the next person</p>
			<p begin="00:01:02:02" end="00:01:05:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		in line after God.</p>
			<p begin="00:01:05:02" end="00:01:05:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	Dr. Simone:</p>
			<p begin="00:01:05:02" end="00:01:05:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		It hurts?</p>
			<p begin="00:01:05:17" end="00:01:07:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; That hurts.</p>
			<p begin="00:01:08:17" end="00:01:10:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			&gt;&gt; My dad s been missing.</p>
			<p begin="00:01:10:13" end="00:01:12:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">No one s heard from him.</p>
			<p begin="00:01:12:02" end="00:01:14:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I never thought that</p>
			<p begin="00:01:12:02" end="00:01:14:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		I would be looking</p>
			<p begin="00:01:14:09" end="00:01:15:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		for my dad.</p>
			<p begin="00:01:15:21" end="00:01:17:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; I got you baby.</p>
			<p begin="00:01:17:10" end="00:01:19:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; I m trying!</p>
			<p begin="00:01:20:07" end="00:01:23:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; I didn t leave my wife,</p>
			<p begin="00:01:20:07" end="00:01:23:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			my wife left me.</p>
			<p begin="00:01:24:07" end="00:01:25:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	Lisa Nicole:</p>
			<p begin="00:01:24:07" end="00:01:25:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		You said that you</p>
			<p begin="00:01:25:11" end="00:01:27:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">wanted a baby!</p>
			<p begin="00:01:25:11" end="00:01:27:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	What is it?</p>
			<p begin="00:01:28:23" end="00:01:30:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">&gt;&gt; I gave you</p>
			<p begin="00:01:28:23" end="00:01:30:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	everything.</p>
			<p begin="00:01:30:11" end="00:01:32:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; Quad was never built to</p>
			<p begin="00:01:30:11" end="00:01:32:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	be a damn queen bee!</p>
			<p begin="00:01:32:23" end="00:01:35:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Mariah: Quad the fraud,</p>
			<p begin="00:01:32:23" end="00:01:35:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			Quad the fraud!</p>
			<p begin="00:01:35:03" end="00:01:37:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	She don t even know</p>
			<p begin="00:01:35:03" end="00:01:37:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">how to wear the crown!</p>
			<p begin="00:01:37:08" end="00:01:38:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			&gt;&gt; You are light.</p>
			<p begin="00:01:38:03" end="00:01:39:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; You re light,</p>
			<p begin="00:01:38:03" end="00:01:39:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			you re light and</p>
			<p begin="00:01:39:08" end="00:01:40:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			your breath stank.</p>
			<p begin="00:01:40:06" end="00:01:41:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Toya: I mean this is</p>
			<p begin="00:01:40:06" end="00:01:41:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		just unacceptable</p>
			<p begin="00:01:41:07" end="00:01:43:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	behavior of</p>
			<p begin="00:01:41:07" end="00:01:43:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			a doctor s wife.</p>
			<p begin="00:01:43:11" end="00:01:46:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			&gt;&gt; You guys are</p>
			<p begin="00:01:43:11" end="00:01:46:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		disrespecting me!</p>
			<p begin="00:01:46:18" end="00:01:48:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; Why are you</p>
			<p begin="00:01:46:18" end="00:01:48:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	so insecure!</p>
			<p begin="00:01:48:08" end="00:01:50:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Genise: What do I</p>
			<p begin="00:01:48:08" end="00:01:50:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		have to be insecure about?</p>
			<p begin="00:01:50:03" end="00:01:51:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			Do you see this!?</p>
			<p begin="00:01:51:03" end="00:01:53:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; I have no interest in</p>
			<p begin="00:01:51:03" end="00:01:53:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">this bullsh--</p>
			<p begin="00:01:53:03" end="00:01:55:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Twirl on, just</p>
			<p begin="00:01:53:03" end="00:01:55:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		twirl on!</p>
			<p begin="00:01:56:11" end="00:01:58:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		&gt;&gt; Can you</p>
			<p begin="00:01:56:11" end="00:01:58:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	hear me, Heavenly!?</p>
			<p begin="00:01:58:20" end="00:02:00:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Understand baby,</p>
			<p begin="00:01:58:20" end="00:02:00:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">I m ready to take your</p>
			<p begin="00:02:00:07" end="00:02:02:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">whole f---ing face off!</p>
			<p begin="00:02:02:04" end="00:02:03:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	&gt;&gt; Are you kidding me?</p>
			<p begin="00:02:03:01" end="00:02:04:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="16% 5.33%">	Stop!</p>
			<p begin="00:02:04:23" end="00:02:14:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		[pop music]</p>
			<p begin="00:02:14:23" end="00:02:23:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		[pop music]</p>
			<p begin="00:02:25:16" end="00:02:27:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	Dr. Simone:</p>
			<p begin="00:02:25:16" end="00:02:27:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">Good morning!</p>
			<p begin="00:02:27:07" end="00:02:29:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">&gt;&gt; You re on time today, doc.</p>
			<p begin="00:02:27:07" end="00:02:29:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		Aren t you a little early?</p>
			<p begin="00:02:29:16" end="00:02:33:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Well, I slept in</p>
			<p begin="00:02:29:16" end="00:02:33:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	the bed, by myself,</p>
			<p begin="00:02:33:05" end="00:02:35:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		no body snatching</p>
			<p begin="00:02:33:05" end="00:02:35:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		my covers.</p>
			<p begin="00:02:35:00" end="00:02:36:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	And my house is clean.</p>
			<p begin="00:02:36:16" end="00:02:39:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		I love that life,</p>
			<p begin="00:02:36:16" end="00:02:39:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	home alone.</p>
			<p begin="00:02:44:16" end="00:02:46:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Toya: Daddy said</p>
			<p begin="00:02:44:16" end="00:02:46:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	no shooting bullets</p>
			<p begin="00:02:46:06" end="00:02:48:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">at each other,</p>
			<p begin="00:02:46:06" end="00:02:48:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			did you hear me?</p>
			<p begin="00:02:48:13" end="00:02:49:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">	&gt;&gt; Eh.</p>
			<p begin="00:02:49:10" end="00:02:50:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			&gt;&gt; Got it!</p>
			<p begin="00:02:52:13" end="00:02:53:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		Dr Jackie:</p>
			<p begin="00:02:52:13" end="00:02:53:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">Hey precious!</p>
			<p begin="00:02:53:20" end="00:02:56:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		Come here!</p>
			<p begin="00:02:53:20" end="00:02:56:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	How are you?</p>
			<p begin="00:02:56:08" end="00:02:59:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		We don t take you</p>
			<p begin="00:02:56:08" end="00:02:59:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	back, nope we don t</p>
			<p begin="00:02:59:01" end="00:03:01:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">do refunds or exchanges.</p>
			<p begin="00:03:08:02" end="00:03:09:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">[cries]</p>
			<p begin="00:03:09:14" end="00:03:12:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		Quad: What s wrong</p>
			<p begin="00:03:09:14" end="00:03:12:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">with the baby?</p>
			<p begin="00:03:12:01" end="00:03:14:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			What s happening?</p>
			<p begin="00:03:14:13" end="00:03:15:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">Does baby want</p>
			<p begin="00:03:14:13" end="00:03:15:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		something to eat,</p>
			<p begin="00:03:15:17" end="00:03:17:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		is that what it is?</p>
			<p begin="00:03:18:13" end="00:03:19:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	Well honey,</p>
			<p begin="00:03:18:13" end="00:03:19:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	I m- listen,</p>
			<p begin="00:03:19:10" end="00:03:20:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I m trying to get the</p>
			<p begin="00:03:19:10" end="00:03:20:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			shrimp and grits</p>
			<p begin="00:03:20:17" end="00:03:22:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">going for you,</p>
			<p begin="00:03:20:17" end="00:03:22:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			I m just saying.</p>
			<p begin="00:03:22:17" end="00:03:24:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	Dr. Gregory:</p>
			<p begin="00:03:22:17" end="00:03:24:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">Good morning!</p>
			<p begin="00:03:24:01" end="00:03:25:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; Hey, honey bun!</p>
			<p begin="00:03:25:14" end="00:03:27:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			&gt;&gt; Hey how s my</p>
			<p begin="00:03:25:14" end="00:03:27:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		wonderful family?</p>
			<p begin="00:03:27:22" end="00:03:29:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Oh the child what</p>
			<p begin="00:03:27:22" end="00:03:29:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		we doing.</p>
			<p begin="00:03:29:15" end="00:03:33:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">&gt;&gt; Hey buddy!</p>
			<p begin="00:03:29:15" end="00:03:33:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			What s going on?</p>
			<p begin="00:03:33:06" end="00:03:35:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Oh! Honey, Miss Quad&apos;s</p>
			<p begin="00:03:33:06" end="00:03:35:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">life has been</p>
			<p begin="00:03:35:21" end="00:03:37:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	very busy and deep,</p>
			<p begin="00:03:35:21" end="00:03:37:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		I almost cant keep</p>
			<p begin="00:03:37:21" end="00:03:39:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			up with it myself!</p>
			<p begin="00:03:39:05" end="00:03:41:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">&gt;&gt; Whoop-whoop.</p>
			<p begin="00:03:42:06" end="00:03:44:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; She has a baby,</p>
			<p begin="00:03:42:06" end="00:03:44:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	uh huh, she has one!</p>
			<p begin="00:03:44:18" end="00:03:46:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	Lives in her</p>
			<p begin="00:03:44:18" end="00:03:46:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">house, honey!</p>
			<p begin="00:03:46:06" end="00:03:47:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			Can you call my</p>
			<p begin="00:03:46:06" end="00:03:47:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		brother so he can</p>
			<p begin="00:03:47:09" end="00:03:49:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	come get his child,</p>
			<p begin="00:03:47:09" end="00:03:49:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	cause I need</p>
			<p begin="00:03:49:06" end="00:03:50:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			to cook breakfast.</p>
			<p begin="00:03:50:17" end="00:03:52:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		But it ain t mine</p>
			<p begin="00:03:50:17" end="00:03:52:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">child, honey.</p>
			<p begin="00:03:52:02" end="00:03:52:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		She is still slim</p>
			<p begin="00:03:52:02" end="00:03:52:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	in the waste</p>
			<p begin="00:03:52:23" end="00:03:55:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	and cute in</p>
			<p begin="00:03:52:23" end="00:03:55:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		the face.</p>
			<p begin="00:03:55:11" end="00:03:57:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	Where the baby daddy?</p>
			<p begin="00:03:57:11" end="00:03:58:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Quentin: Where s</p>
			<p begin="00:03:57:11" end="00:03:58:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">my little man?</p>
			<p begin="00:03:58:15" end="00:03:59:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; What s up brother?</p>
			<p begin="00:03:59:12" end="00:04:00:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Hey good morning,</p>
			<p begin="00:03:59:12" end="00:04:00:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			how s everyone?</p>
			<p begin="00:04:00:18" end="00:04:02:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; I m good, I just</p>
			<p begin="00:04:00:18" end="00:04:02:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">need you to take your,</p>
			<p begin="00:04:02:18" end="00:04:05:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		half your-</p>
			<p begin="00:04:02:18" end="00:04:05:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		&gt;&gt; My better half.</p>
			<p begin="00:04:05:22" end="00:04:08:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; Take your little better</p>
			<p begin="00:04:05:22" end="00:04:08:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			half right here,</p>
			<p begin="00:04:08:07" end="00:04:09:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">			I got to</p>
			<p begin="00:04:08:07" end="00:04:09:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		finish breakfast.</p>
			<p begin="00:04:09:18" end="00:04:11:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; Okay I m kind</p>
			<p begin="00:04:09:18" end="00:04:11:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		of hungry.</p>
			<p begin="00:04:11:11" end="00:04:13:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Oh, you re hungry?</p>
			<p begin="00:04:11:11" end="00:04:13:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			Okay, whatever.</p>
			<p begin="00:04:13:10" end="00:04:14:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Want to sit with</p>
			<p begin="00:04:13:10" end="00:04:14:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		daddy or you want</p>
			<p begin="00:04:14:23" end="00:04:16:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">to sit in your</p>
			<p begin="00:04:14:23" end="00:04:16:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			high chair man.</p>
			<p begin="00:04:16:19" end="00:04:18:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; Have a good</p>
			<p begin="00:04:16:19" end="00:04:18:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">day, Gregory!</p>
			<p begin="00:04:18:19" end="00:04:20:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; I m excited</p>
			<p begin="00:04:18:19" end="00:04:20:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	having Mason around</p>
			<p begin="00:04:20:15" end="00:04:21:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		but there s a lot</p>
			<p begin="00:04:20:15" end="00:04:21:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		of good DNA going</p>
			<p begin="00:04:21:19" end="00:04:23:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			to waste sitting</p>
			<p begin="00:04:21:19" end="00:04:23:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		over here.</p>
			<p begin="00:04:23:07" end="00:04:25:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Well its not really</p>
			<p begin="00:04:23:07" end="00:04:25:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			going to waste,</p>
			<p begin="00:04:25:15" end="00:04:28:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	its still there and</p>
			<p begin="00:04:25:15" end="00:04:28:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	it s been preserved.</p>
			<p begin="00:04:29:00" end="00:04:33:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; You re cooking,</p>
			<p begin="00:04:29:00" end="00:04:33:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	the house is clean,</p>
			<p begin="00:04:33:07" end="00:04:34:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">it s time for</p>
			<p begin="00:04:33:07" end="00:04:34:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		that baby.</p>
			<p begin="00:04:34:23" end="00:04:37:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">Want to go to</p>
			<p begin="00:04:34:23" end="00:04:37:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			that next level!</p>
			<p begin="00:04:37:12" end="00:04:38:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; We re going to</p>
			<p begin="00:04:37:12" end="00:04:38:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">get you there.</p>
			<p begin="00:04:38:19" end="00:04:39:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Okay.</p>
			<p begin="00:04:39:09" end="00:04:40:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">&gt;&gt; We ll get you there.</p>
			<p begin="00:04:40:23" end="00:04:42:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; Come on in!</p>
			<p begin="00:04:40:23" end="00:04:42:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">Good morning!</p>
			<p begin="00:04:42:18" end="00:04:43:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="26% 5.33%">			Monica:</p>
			<p begin="00:04:42:18" end="00:04:43:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">Good morning.</p>
			<p begin="00:04:43:11" end="00:04:44:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	Good morning.</p>
			<p begin="00:04:44:07" end="00:04:45:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; Good morning,</p>
			<p begin="00:04:44:07" end="00:04:45:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			Princess Diana!</p>
			<p begin="00:04:45:07" end="00:04:47:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; So you took</p>
			<p begin="00:04:45:07" end="00:04:47:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			my baby?</p>
			<p begin="00:04:47:06" end="00:04:49:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Well you know he s</p>
			<p begin="00:04:47:06" end="00:04:49:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			partially mine.</p>
			<p begin="00:04:49:11" end="00:04:50:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			You just had him.</p>
			<p begin="00:04:50:13" end="00:04:54:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Recently when I went</p>
			<p begin="00:04:50:13" end="00:04:54:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			home to Memphis,</p>
			<p begin="00:04:54:03" end="00:04:56:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Quentin was working</p>
			<p begin="00:04:54:03" end="00:04:56:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			a dead end job, Monica,</p>
			<p begin="00:04:56:12" end="00:04:57:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			she lost her job.</p>
			<p begin="00:04:58:00" end="00:04:59:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">I said honey,</p>
			<p begin="00:04:58:00" end="00:04:59:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	the city is just not</p>
			<p begin="00:04:59:01" end="00:05:00:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">for you anymore.</p>
			<p begin="00:05:00:11" end="00:05:01:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	So he s here</p>
			<p begin="00:05:00:11" end="00:05:01:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	in Atlanta.</p>
			<p begin="00:05:01:23" end="00:05:03:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">			[crashes]</p>
			<p begin="00:05:03:09" end="00:05:06:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			Oh my God Mason</p>
			<p begin="00:05:03:09" end="00:05:06:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	I just bought those!</p>
			<p begin="00:05:06:08" end="00:05:09:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	Mason, why would you-</p>
			<p begin="00:05:10:20" end="00:05:12:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			You going to pay</p>
			<p begin="00:05:10:20" end="00:05:12:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			me back?</p>
			<p begin="00:05:12:04" end="00:05:15:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			I love the fact that my</p>
			<p begin="00:05:12:04" end="00:05:15:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			family s on deck honey!</p>
			<p begin="00:05:15:05" end="00:05:17:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I m going to go ahead</p>
			<p begin="00:05:15:05" end="00:05:17:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		and go on finish cooking.</p>
			<p begin="00:05:17:05" end="00:05:19:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		&gt;&gt; Yeah I m hungry!</p>
			<p begin="00:05:19:20" end="00:05:22:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			&gt;&gt; The hell I do.</p>
			<p begin="00:05:22:13" end="00:05:25:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">Child pay your</p>
			<p begin="00:05:22:13" end="00:05:25:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	dust, honey.</p>
			<p begin="00:05:25:00" end="00:05:26:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			[laughing]</p>
			<p begin="00:05:32:01" end="00:05:35:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Dr. Jackie: I looked</p>
			<p begin="00:05:32:01" end="00:05:35:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			at some places for you.</p>
			<p begin="00:05:35:01" end="00:05:36:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Curtis: How big are</p>
			<p begin="00:05:35:01" end="00:05:36:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			those bedrooms?</p>
			<p begin="00:05:36:17" end="00:05:38:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Yeah, they re not</p>
			<p begin="00:05:36:17" end="00:05:38:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		that big.</p>
			<p begin="00:05:38:09" end="00:05:39:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; And I know the</p>
			<p begin="00:05:38:09" end="00:05:39:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		master s not going</p>
			<p begin="00:05:39:13" end="00:05:40:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">to be that big.</p>
			<p begin="00:05:40:17" end="00:05:41:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Man don t worry</p>
			<p begin="00:05:40:17" end="00:05:41:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">about the size</p>
			<p begin="00:05:41:17" end="00:05:42:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">of the master bedroom</p>
			<p begin="00:05:41:17" end="00:05:42:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			all we going to</p>
			<p begin="00:05:42:21" end="00:05:44:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	do in there is sleep!</p>
			<p begin="00:05:44:05" end="00:05:44:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	Life is good!</p>
			<p begin="00:05:45:00" end="00:05:47:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">You know, I am busier</p>
			<p begin="00:05:45:00" end="00:05:47:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		than ever.</p>
			<p begin="00:05:47:17" end="00:05:50:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">		I m excited!</p>
			<p begin="00:05:50:01" end="00:05:52:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		Quad: Did you sell</p>
			<p begin="00:05:50:01" end="00:05:52:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			your house girl!</p>
			<p begin="00:05:52:01" end="00:05:53:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	Did you sell</p>
			<p begin="00:05:52:01" end="00:05:53:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	your house?</p>
			<p begin="00:05:53:13" end="00:05:54:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">&gt;&gt; Yes!</p>
			<p begin="00:05:54:13" end="00:05:56:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Curtis and I sold</p>
			<p begin="00:05:54:13" end="00:05:56:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			our house, yay!</p>
			<p begin="00:05:56:17" end="00:05:59:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		We had some crazy</p>
			<p begin="00:05:56:17" end="00:05:59:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		memories in here.</p>
			<p begin="00:05:59:13" end="00:06:02:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			However, we had</p>
			<p begin="00:05:59:13" end="00:06:02:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		to move  quickly,</p>
			<p begin="00:06:02:05" end="00:06:03:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		we had to move to</p>
			<p begin="00:06:02:05" end="00:06:03:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">an apartment.</p>
			<p begin="00:06:03:21" end="00:06:04:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	&gt;&gt; Bye house!</p>
			<p begin="00:06:04:20" end="00:06:06:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">&gt;&gt; Bye!</p>
			<p begin="00:06:06:05" end="00:06:10:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Moving into a 1400 foot</p>
			<p begin="00:06:06:05" end="00:06:10:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		apartment,</p>
			<p begin="00:06:10:01" end="00:06:13:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		we see each other</p>
			<p begin="00:06:10:01" end="00:06:13:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">all the time.</p>
			<p begin="00:06:14:11" end="00:06:17:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	City living is for me.</p>
			<p begin="00:06:17:06" end="00:06:19:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Suburban living</p>
			<p begin="00:06:17:06" end="00:06:19:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		is for me.</p>
			<p begin="00:06:19:10" end="00:06:22:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; I like the city living</p>
			<p begin="00:06:19:10" end="00:06:22:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		high rise-</p>
			<p begin="00:06:22:10" end="00:06:24:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; You grew up in</p>
			<p begin="00:06:22:10" end="00:06:24:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%"> Mississippi.</p>
			<p begin="00:06:24:02" end="00:06:25:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; So I-</p>
			<p begin="00:06:25:13" end="00:06:28:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Now you want to</p>
			<p begin="00:06:25:13" end="00:06:28:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		be up in the city?</p>
			<p begin="00:06:28:02" end="00:06:29:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Yeah.</p>
			<p begin="00:06:29:02" end="00:06:31:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		We sold our house</p>
			<p begin="00:06:29:02" end="00:06:31:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	with the exact same</p>
			<p begin="00:06:31:22" end="00:06:33:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		opinion, of moving</p>
			<p begin="00:06:31:22" end="00:06:33:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		to another house.</p>
			<p begin="00:06:33:22" end="00:06:36:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	But you can walk to</p>
			<p begin="00:06:33:22" end="00:06:36:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">where you need</p>
			<p begin="00:06:36:06" end="00:06:38:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">to in the city!</p>
			<p begin="00:06:38:10" end="00:06:42:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">However, after living</p>
			<p begin="00:06:38:10" end="00:06:42:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		in the rental and</p>
			<p begin="00:06:42:03" end="00:06:44:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		walking right down</p>
			<p begin="00:06:42:03" end="00:06:44:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">stairs to eat,</p>
			<p begin="00:06:44:10" end="00:06:49:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			I feel that a high rise</p>
			<p begin="00:06:44:10" end="00:06:49:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="76% 5.33%">will suit my lifestyle better.</p>
			<p begin="00:06:49:10" end="00:06:50:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; There s a particular</p>
			<p begin="00:06:49:10" end="00:06:50:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		house that</p>
			<p begin="00:06:50:19" end="00:06:52:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			I want us to see.</p>
			<p begin="00:06:52:10" end="00:06:57:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Because I&apos;m about house</p>
			<p begin="00:06:52:10" end="00:06:57:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">... and space.</p>
			<p begin="00:06:57:03" end="00:06:58:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			&gt;&gt; I m having a hot flash.</p>
			<p begin="00:06:58:14" end="00:07:00:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; I m used to having</p>
			<p begin="00:06:58:14" end="00:07:00:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			a large master bedroom.</p>
			<p begin="00:07:00:19" end="00:07:01:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">The fact that we re on</p>
			<p begin="00:07:00:19" end="00:07:01:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">different pages about</p>
			<p begin="00:07:01:23" end="00:07:05:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">where we want to live,</p>
			<p begin="00:07:01:23" end="00:07:05:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			it s nothing new to us,</p>
			<p begin="00:07:05:10" end="00:07:07:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	we ve been on a few</p>
			<p begin="00:07:05:10" end="00:07:07:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	different pages over</p>
			<p begin="00:07:07:02" end="00:07:08:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">the last fourteen years.</p>
			<p begin="00:07:08:23" end="00:07:10:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		Here we go.</p>
			<p begin="00:07:11:06" end="00:07:15:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">Floors look as nice as</p>
			<p begin="00:07:11:06" end="00:07:15:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			they do in the outside.</p>
			<p begin="00:07:15:08" end="00:07:17:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">&gt;&gt; But its grey.</p>
			<p begin="00:07:17:11" end="00:07:19:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; And... what s wrong</p>
			<p begin="00:07:17:11" end="00:07:19:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		with grey?</p>
			<p begin="00:07:19:23" end="00:07:21:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Pretty neutral color</p>
			<p begin="00:07:19:23" end="00:07:21:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		isn t it?</p>
			<p begin="00:07:21:11" end="00:07:24:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Any place that we</p>
			<p begin="00:07:21:11" end="00:07:24:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		see that s not in</p>
			<p begin="00:07:24:11" end="00:07:26:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			the city or in high rise</p>
			<p begin="00:07:24:11" end="00:07:26:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		right now.</p>
			<p begin="00:07:27:00" end="00:07:30:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; It s dark though,</p>
			<p begin="00:07:27:00" end="00:07:30:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		like it needs more light.</p>
			<p begin="00:07:30:04" end="00:07:32:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; This is gonna be wrong,</p>
			<p begin="00:07:30:04" end="00:07:32:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">that s gonna be wrong.</p>
			<p begin="00:07:32:03" end="00:07:33:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; This big room right</p>
			<p begin="00:07:32:03" end="00:07:33:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		here we don t know</p>
			<p begin="00:07:33:07" end="00:07:34:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">what to do with.</p>
			<p begin="00:07:34:19" end="00:07:37:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; So I usually end up</p>
			<p begin="00:07:34:19" end="00:07:37:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">	giving in with most things.</p>
			<p begin="00:07:37:05" end="00:07:38:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		&gt;&gt; With bad energy.</p>
			<p begin="00:07:38:20" end="00:07:41:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; We can maybe have</p>
			<p begin="00:07:38:20" end="00:07:41:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">like two beds in here.</p>
			<p begin="00:07:41:16" end="00:07:43:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">		&gt;&gt; We might.</p>
			<p begin="00:07:44:00" end="00:07:46:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">[hip hop music]</p>
			<p begin="00:07:47:04" end="00:07:53:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	[upbeat music]</p>
			<p begin="00:07:53:05" end="00:07:54:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; This is awesome,</p>
			<p begin="00:07:53:05" end="00:07:54:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		we are in a great</p>
			<p begin="00:07:54:08" end="00:07:55:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	neighbor hood.</p>
			<p begin="00:07:55:05" end="00:07:56:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Oh no, the neighbor</p>
			<p begin="00:07:55:05" end="00:07:56:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			hood is awesome.</p>
			<p begin="00:07:56:07" end="00:07:57:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">		&gt;&gt; Dude, you re in midtown.</p>
			<p begin="00:07:58:03" end="00:08:01:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			[music continues]</p>
			<p begin="00:08:01:16" end="00:08:04:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Oh honey this is</p>
			<p begin="00:08:01:16" end="00:08:04:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	so awesome.</p>
			<p begin="00:08:04:08" end="00:08:06:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">&gt;&gt; Cool, do-do you like?</p>
			<p begin="00:08:06:03" end="00:08:07:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; I mean seriously,</p>
			<p begin="00:08:06:03" end="00:08:07:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="26% 5.33%">			I love!</p>
			<p begin="00:08:07:08" end="00:08:09:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	&gt;&gt; So we are, we are finally</p>
			<p begin="00:08:07:08" end="00:08:09:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		about to be open.</p>
			<p begin="00:08:09:04" end="00:08:10:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">	[sigh]</p>
			<p begin="00:08:10:01" end="00:08:11:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt;Please believe the</p>
			<p begin="00:08:10:01" end="00:08:11:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			Harris household</p>
			<p begin="00:08:12:00" end="00:08:15:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		is on ten right now.</p>
			<p begin="00:08:16:08" end="00:08:17:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	[upbeat music]</p>
			<p begin="00:08:17:06" end="00:08:18:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			&gt;&gt; I wanna use that ball.</p>
			<p begin="00:08:18:10" end="00:08:19:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Wait let me show</p>
			<p begin="00:08:18:10" end="00:08:19:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			you  something.</p>
			<p begin="00:08:19:09" end="00:08:21:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; The kids are, a little</p>
			<p begin="00:08:19:09" end="00:08:21:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			mischievous but</p>
			<p begin="00:08:21:01" end="00:08:22:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">that s to be expected</p>
			<p begin="00:08:21:01" end="00:08:22:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">they re mine.</p>
			<p begin="00:08:22:17" end="00:08:23:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">[laughs]</p>
			<p begin="00:08:23:18" end="00:08:26:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Photographer: Good!</p>
			<p begin="00:08:23:18" end="00:08:26:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		Perfect! Oh that s great!</p>
			<p begin="00:08:26:02" end="00:08:28:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; And on top of that I m</p>
			<p begin="00:08:26:02" end="00:08:28:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	turning forty, boo!</p>
			<p begin="00:08:28:05" end="00:08:30:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Yes! And I don t look it.</p>
			<p begin="00:08:28:05" end="00:08:30:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="13% 5.33%">Okay?</p>
			<p begin="00:08:30:14" end="00:08:33:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Forty is the new Thirty,</p>
			<p begin="00:08:30:14" end="00:08:33:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	or maybe even Twenty</p>
			<p begin="00:08:33:01" end="00:08:33:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		when you look at me.</p>
			<p begin="00:08:33:21" end="00:08:34:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		&gt;&gt; Welcome.</p>
			<p begin="00:08:34:14" end="00:08:35:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	&gt;&gt; Thank you.</p>
			<p begin="00:08:35:21" end="00:08:38:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			&gt;&gt; To replenish</p>
			<p begin="00:08:35:21" end="00:08:38:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	by Nomad MD.</p>
			<p begin="00:08:38:21" end="00:08:40:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			I just want to see what</p>
			<p begin="00:08:38:21" end="00:08:40:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	you thought.</p>
			<p begin="00:08:40:10" end="00:08:41:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; This is like the</p>
			<p begin="00:08:40:10" end="00:08:41:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">waiting areas.</p>
			<p begin="00:08:41:20" end="00:08:44:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	I think it s nice I</p>
			<p begin="00:08:41:20" end="00:08:44:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			really love this floor,</p>
			<p begin="00:08:44:05" end="00:08:45:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			I mean seriously</p>
			<p begin="00:08:44:05" end="00:08:45:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			I love the wood,</p>
			<p begin="00:08:45:17" end="00:08:46:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		it s light.</p>
			<p begin="00:08:46:18" end="00:08:49:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	&gt;&gt; We are a</p>
			<p begin="00:08:46:18" end="00:08:49:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		selective IV spa,</p>
			<p begin="00:08:49:12" end="00:08:51:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		we actually have a</p>
			<p begin="00:08:49:12" end="00:08:51:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			vitamin therapy,</p>
			<p begin="00:08:51:10" end="00:08:54:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		IV fluids,</p>
			<p begin="00:08:51:10" end="00:08:54:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			hangover relief.</p>
			<p begin="00:08:54:09" end="00:08:57:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Honey, the bottom line</p>
			<p begin="00:08:54:09" end="00:08:57:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		is this...</p>
			<p begin="00:08:57:04" end="00:08:59:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">ya ll need to get the </p>
			<p begin="00:08:57:04" end="00:08:59:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		brick and morther,</p>
			<p begin="00:08:59:06" end="00:09:00:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			seriously.</p>
			<p begin="00:09:00:10" end="00:09:02:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; This is one of the</p>
			<p begin="00:09:00:10" end="00:09:02:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			treatment rooms.</p>
			<p begin="00:09:02:06" end="00:09:05:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I wanna say thank you</p>
			<p begin="00:09:02:06" end="00:09:05:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			for putting in the idea</p>
			<p begin="00:09:05:02" end="00:09:06:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	that we should open</p>
			<p begin="00:09:05:02" end="00:09:06:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	up a physical space.</p>
			<p begin="00:09:06:18" end="00:09:08:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Like lined up,</p>
			<p begin="00:09:06:18" end="00:09:08:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		and then you like</p>
			<p begin="00:09:08:10" end="00:09:10:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">put them up with an IV.</p>
			<p begin="00:09:10:05" end="00:09:12:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Initially didn t think</p>
			<p begin="00:09:10:05" end="00:09:12:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	it was a good idea,</p>
			<p begin="00:09:12:03" end="00:09:13:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	you know we</p>
			<p begin="00:09:12:03" end="00:09:13:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		wanted to be free,</p>
			<p begin="00:09:13:10" end="00:09:15:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	that s why we called</p>
			<p begin="00:09:13:10" end="00:09:15:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	ourselves Nomads so-</p>
			<p begin="00:09:15:10" end="00:09:16:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Honey, you been free</p>
			<p begin="00:09:15:10" end="00:09:16:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		this whole time--</p>
			<p begin="00:09:16:14" end="00:09:17:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">[laughs]</p>
			<p begin="00:09:17:18" end="00:09:18:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">black people have been</p>
			<p begin="00:09:17:18" end="00:09:18:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">free for a long time.</p>
			<p begin="00:09:18:18" end="00:09:20:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	&gt;&gt; Oh Jesus, for real?</p>
			<p begin="00:09:20:01" end="00:09:21:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; Seriously, I absolutely</p>
			<p begin="00:09:20:01" end="00:09:21:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			love the space.</p>
			<p begin="00:09:21:14" end="00:09:26:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			I- I do. I just want to</p>
			<p begin="00:09:21:14" end="00:09:26:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	know that in the end</p>
			<p begin="00:09:26:02" end="00:09:28:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			this is going to</p>
			<p begin="00:09:26:02" end="00:09:28:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			take off and like who s</p>
			<p begin="00:09:28:18" end="00:09:30:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		going to do the marketing</p>
			<p begin="00:09:28:18" end="00:09:30:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">who s going to</p>
			<p begin="00:09:30:01" end="00:09:30:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			get it out there?</p>
			<p begin="00:09:30:22" end="00:09:31:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	&gt;&gt; You don t</p>
			<p begin="00:09:30:22" end="00:09:31:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		have to worry about that.</p>
			<p begin="00:09:31:19" end="00:09:32:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; No I do have to worry</p>
			<p begin="00:09:31:19" end="00:09:32:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	about that,</p>
			<p begin="00:09:32:23" end="00:09:35:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			because outside of this</p>
			<p begin="00:09:32:23" end="00:09:35:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">we have bills-</p>
			<p begin="00:09:35:11" end="00:09:36:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; I hear you.</p>
			<p begin="00:09:36:06" end="00:09:37:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; That need to be paid,</p>
			<p begin="00:09:36:06" end="00:09:37:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			we have-</p>
			<p begin="00:09:37:03" end="00:09:38:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	we re behind on taxes.</p>
			<p begin="00:09:38:22" end="00:09:43:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	&gt;&gt; In the last three years,</p>
			<p begin="00:09:38:22" end="00:09:43:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			we fell behind on taxes.</p>
			<p begin="00:09:43:06" end="00:09:44:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; For three years</p>
			<p begin="00:09:44:07" end="00:09:45:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	[overlapping stutters]</p>
			<p begin="00:09:45:02" end="00:09:47:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">&gt;&gt; We re behind!</p>
			<p begin="00:09:47:11" end="00:09:49:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Our accountants suck!</p>
			<p begin="00:09:47:11" end="00:09:49:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		You know what I m saying?</p>
			<p begin="00:09:49:15" end="00:09:51:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			And the fact that I had</p>
			<p begin="00:09:49:15" end="00:09:51:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">to call him, fire him.</p>
			<p begin="00:09:51:12" end="00:09:55:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			To my surprise,</p>
			<p begin="00:09:51:12" end="00:09:55:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			we owe about six</p>
			<p begin="00:09:55:03" end="00:09:57:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		figures of debt to</p>
			<p begin="00:09:55:03" end="00:09:57:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			the IRS.</p>
			<p begin="00:09:57:16" end="00:09:59:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		I got to take some</p>
			<p begin="00:09:57:16" end="00:09:59:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	blame for it because</p>
			<p begin="00:09:59:11" end="00:10:02:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	for years I was just</p>
			<p begin="00:09:59:11" end="00:10:02:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		sitting back and you know,</p>
			<p begin="00:10:02:16" end="00:10:04:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="78% 5.33%">I wasn t even paying attention!</p>
			<p begin="00:10:04:04" end="00:10:06:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I just want to get us</p>
			<p begin="00:10:04:04" end="00:10:06:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			to a place where</p>
			<p begin="00:10:06:06" end="00:10:08:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		we re putting that</p>
			<p begin="00:10:06:06" end="00:10:08:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	money back.</p>
			<p begin="00:10:08:12" end="00:10:09:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Okay.</p>
			<p begin="00:10:09:07" end="00:10:10:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Alright let s get</p>
			<p begin="00:10:09:07" end="00:10:10:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">up out of here</p>
			<p begin="00:10:10:03" end="00:10:10:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	I need to go</p>
			<p begin="00:10:10:03" end="00:10:10:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">have a drink.</p>
			<p begin="00:10:10:23" end="00:10:12:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		I need a glass of</p>
			<p begin="00:10:10:23" end="00:10:12:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		wine or something</p>
			<p begin="00:10:12:11" end="00:10:14:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; I hope this</p>
			<p begin="00:10:12:11" end="00:10:14:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	drinking time is in</p>
			<p begin="00:10:14:07" end="00:10:16:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">the damn budget!</p>
			<p begin="00:10:17:06" end="00:10:18:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		Narrator:</p>
			<p begin="00:10:17:06" end="00:10:18:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		Coming up!</p>
			<p begin="00:10:18:07" end="00:10:19:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">Dr. Heavenly:</p>
			<p begin="00:10:18:07" end="00:10:19:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">So now are you</p>
			<p begin="00:10:19:06" end="00:10:20:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	going to get Darren</p>
			<p begin="00:10:19:06" end="00:10:20:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	checked out because</p>
			<p begin="00:10:20:11" end="00:10:22:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		he hasn t had any</p>
			<p begin="00:10:20:11" end="00:10:22:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	kids in a long time.</p>
			<p begin="00:10:22:17" end="00:10:24:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">Has he?</p>
			<p begin="00:10:34:05" end="00:10:36:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; So girl, I don t drink</p>
			<p begin="00:10:34:05" end="00:10:36:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		no more you know.</p>
			<p begin="00:10:37:00" end="00:10:38:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Lisa Nicole: You stopped</p>
			<p begin="00:10:37:00" end="00:10:38:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		drinking?</p>
			<p begin="00:10:38:08" end="00:10:42:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; I m doing my best</p>
			<p begin="00:10:38:08" end="00:10:42:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	to limit my intake.</p>
			<p begin="00:10:42:01" end="00:10:44:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I know you guys don t</p>
			<p begin="00:10:42:01" end="00:10:44:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">recognize me,</p>
			<p begin="00:10:44:12" end="00:10:46:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	the new Dr. Heavenly</p>
			<p begin="00:10:44:12" end="00:10:46:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			is here.</p>
			<p begin="00:10:46:00" end="00:10:48:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">This is how I work out!</p>
			<p begin="00:10:48:16" end="00:10:51:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		I ve lost a little weight</p>
			<p begin="00:10:48:16" end="00:10:51:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			I m looking pretty good.</p>
			<p begin="00:10:51:15" end="00:10:53:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">College, do you think</p>
			<p begin="00:10:51:15" end="00:10:53:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		college people are</p>
			<p begin="00:10:53:08" end="00:10:55:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	going to accept you</p>
			<p begin="00:10:53:08" end="00:10:55:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		with your hair like that?</p>
			<p begin="00:10:55:04" end="00:10:56:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Zachary: I mean I m</p>
			<p begin="00:10:55:04" end="00:10:56:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		 eighteen!</p>
			<p begin="00:10:56:07" end="00:10:58:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; My kids are</p>
			<p begin="00:10:56:07" end="00:10:58:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	doing well, </p>
			<p begin="00:10:58:16" end="00:11:01:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			my oldest boy is getting</p>
			<p begin="00:10:58:16" end="00:11:01:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		ready to graduate.</p>
			<p begin="00:11:01:08" end="00:11:02:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		Hey daddy!</p>
			<p begin="00:11:01:08" end="00:11:02:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		What s up?</p>
			<p begin="00:11:02:20" end="00:11:05:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			I just opened a</p>
			<p begin="00:11:02:20" end="00:11:05:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			new practice this year,</p>
			<p begin="00:11:05:01" end="00:11:07:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		and my husband and</p>
			<p begin="00:11:05:01" end="00:11:07:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		I opened a surgery</p>
			<p begin="00:11:07:09" end="00:11:08:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	center and you best</p>
			<p begin="00:11:07:09" end="00:11:08:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			believe my name</p>
			<p begin="00:11:08:17" end="00:11:09:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">is on the deed.</p>
			<p begin="00:11:09:17" end="00:11:11:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">I mean ladies</p>
			<p begin="00:11:09:17" end="00:11:11:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">pay attention.</p>
			<p begin="00:11:11:12" end="00:11:13:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Imma just go with</p>
			<p begin="00:11:11:12" end="00:11:13:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		you to see Jackie</p>
			<p begin="00:11:13:09" end="00:11:15:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">to see if you burning</p>
			<p begin="00:11:13:09" end="00:11:15:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		or who s burning.</p>
			<p begin="00:11:15:10" end="00:11:17:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I might get my stuff</p>
			<p begin="00:11:15:10" end="00:11:17:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			checked out so.</p>
			<p begin="00:11:17:10" end="00:11:19:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Girl! You re just here</p>
			<p begin="00:11:17:10" end="00:11:19:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		for moral support.</p>
			<p begin="00:11:20:00" end="00:11:22:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">This is a very</p>
			<p begin="00:11:20:00" end="00:11:22:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">important appointment</p>
			<p begin="00:11:22:13" end="00:11:25:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		you know I m very</p>
			<p begin="00:11:22:13" end="00:11:25:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	serious about trying</p>
			<p begin="00:11:25:04" end="00:11:26:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">to get pregnant.</p>
			<p begin="00:11:26:01" end="00:11:29:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; You think that</p>
			<p begin="00:11:26:01" end="00:11:29:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	having a baby right</p>
			<p begin="00:11:29:06" end="00:11:31:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	now is a great idea</p>
			<p begin="00:11:29:06" end="00:11:31:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			for you?</p>
			<p begin="00:11:31:02" end="00:11:33:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">I mean with everything</p>
			<p begin="00:11:31:02" end="00:11:33:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		you got going on?</p>
			<p begin="00:11:33:09" end="00:11:36:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Lisa has been hinting at</p>
			<p begin="00:11:33:09" end="00:11:36:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		having a baby for</p>
			<p begin="00:11:36:21" end="00:11:39:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">awhile but honestly I</p>
			<p begin="00:11:36:21" end="00:11:39:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">thought it was a joke.</p>
			<p begin="00:11:39:13" end="00:11:41:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			I just remember</p>
			<p begin="00:11:39:13" end="00:11:41:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			at the  bonfire,</p>
			<p begin="00:11:41:13" end="00:11:45:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		you said,</p>
			<p begin="00:11:41:13" end="00:11:45:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">&quot;If you couldn t trust</p>
			<p begin="00:11:45:10" end="00:11:46:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			him you were out.&quot;</p>
			<p begin="00:11:46:18" end="00:11:49:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; I m just at a place</p>
			<p begin="00:11:46:18" end="00:11:49:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		where I feel like</p>
			<p begin="00:11:49:02" end="00:11:50:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	if you don t</p>
			<p begin="00:11:49:02" end="00:11:50:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	have trust,</p>
			<p begin="00:11:50:11" end="00:11:52:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">you don t have</p>
			<p begin="00:11:50:11" end="00:11:52:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	a marriage.</p>
			<p begin="00:11:52:18" end="00:11:57:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Last year was the</p>
			<p begin="00:11:52:18" end="00:11:57:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			year from hell.</p>
			<p begin="00:11:57:02" end="00:11:58:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">		It just was.</p>
			<p begin="00:11:58:01" end="00:11:59:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Are you having</p>
			<p begin="00:11:58:01" end="00:11:59:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">a great time?</p>
			<p begin="00:11:59:18" end="00:12:00:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; I am!</p>
			<p begin="00:12:00:14" end="00:12:02:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">&gt;&gt; How s Darren?</p>
			<p begin="00:12:02:14" end="00:12:04:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">	&gt;&gt; Oh!</p>
			<p begin="00:12:04:10" end="00:12:06:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Darren: Sometimes</p>
			<p begin="00:12:04:10" end="00:12:06:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		husbands every now</p>
			<p begin="00:12:06:02" end="00:12:07:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		and then,</p>
			<p begin="00:12:06:02" end="00:12:07:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		go to strip clubs</p>
			<p begin="00:12:07:18" end="00:12:08:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		with their friends.</p>
			<p begin="00:12:08:15" end="00:12:10:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; That s bullsh--,</p>
			<p begin="00:12:08:15" end="00:12:10:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			not my husband.</p>
			<p begin="00:12:10:02" end="00:12:12:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Her husband is</p>
			<p begin="00:12:10:02" end="00:12:12:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		sleeping with me!</p>
			<p begin="00:12:12:02" end="00:12:15:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; I don t feel like</p>
			<p begin="00:12:12:02" end="00:12:15:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">we re like at a point</p>
			<p begin="00:12:15:22" end="00:12:17:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		of no return at all.</p>
			<p begin="00:12:17:18" end="00:12:19:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		I think this is a</p>
			<p begin="00:12:17:18" end="00:12:19:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	way for us to grow.</p>
			<p begin="00:12:19:19" end="00:12:22:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Darren and I had to</p>
			<p begin="00:12:19:19" end="00:12:22:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	really work through</p>
			<p begin="00:12:22:18" end="00:12:26:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		our communication</p>
			<p begin="00:12:22:18" end="00:12:26:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="73% 5.33%">	issues and definitely trust,</p>
			<p begin="00:12:26:18" end="00:12:28:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		but that s marriage.</p>
			<p begin="00:12:28:15" end="00:12:31:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; So you re going</p>
			<p begin="00:12:28:15" end="00:12:31:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		to Miss Jackie to</p>
			<p begin="00:12:31:02" end="00:12:32:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	see if you re fertile?</p>
			<p begin="00:12:32:19" end="00:12:34:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I mean what we going</p>
			<p begin="00:12:32:19" end="00:12:34:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">here for to get tested</p>
			<p begin="00:12:34:14" end="00:12:35:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">before we start.</p>
			<p begin="00:12:35:12" end="00:12:38:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Well you know once</p>
			<p begin="00:12:35:12" end="00:12:38:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	you re over the age</p>
			<p begin="00:12:38:04" end="00:12:40:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">of thirty five its not-</p>
			<p begin="00:12:40:03" end="00:12:42:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			[laughing]</p>
			<p begin="00:12:42:15" end="00:12:47:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	&gt;&gt; Quad is over thirty five,</p>
			<p begin="00:12:42:15" end="00:12:47:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		I think you re over four-</p>
			<p begin="00:12:47:07" end="00:12:49:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; No, no I don t know</p>
			<p begin="00:12:47:07" end="00:12:49:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		I stopped counting</p>
			<p begin="00:12:49:08" end="00:12:50:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			after twenty five.</p>
			<p begin="00:12:50:19" end="00:12:51:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">&gt;&gt; I know okay.</p>
			<p begin="00:12:51:19" end="00:12:54:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">I think Lisa Nicole is</p>
			<p begin="00:12:51:19" end="00:12:54:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		about forty five,</p>
			<p begin="00:12:54:06" end="00:12:55:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		forty six,</p>
			<p begin="00:12:54:06" end="00:12:55:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	somewhere in there.</p>
			<p begin="00:12:55:23" end="00:12:57:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">She s too damn old to</p>
			<p begin="00:12:55:23" end="00:12:57:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	have a baby.</p>
			<p begin="00:12:57:19" end="00:12:59:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	We know that.</p>
			<p begin="00:12:59:03" end="00:13:00:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	So now are you going</p>
			<p begin="00:12:59:03" end="00:13:00:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">to get Darren</p>
			<p begin="00:13:00:08" end="00:13:01:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">checked out because he</p>
			<p begin="00:13:00:08" end="00:13:01:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">hasn t had any</p>
			<p begin="00:13:01:19" end="00:13:03:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		kids in a long time.</p>
			<p begin="00:13:03:07" end="00:13:04:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">Has he?</p>
			<p begin="00:13:04:14" end="00:13:09:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			[laughing]</p>
			<p begin="00:13:10:19" end="00:13:14:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; You know what,</p>
			<p begin="00:13:10:19" end="00:13:14:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">you know what!</p>
			<p begin="00:13:15:00" end="00:13:15:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			Keisha: Hi ladies!</p>
			<p begin="00:13:15:21" end="00:13:16:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	&gt;&gt; Hi Keisha!</p>
			<p begin="00:13:16:20" end="00:13:17:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">&gt;&gt; How are you?</p>
			<p begin="00:13:17:20" end="00:13:18:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">		&gt;&gt; I m good.</p>
			<p begin="00:13:18:19" end="00:13:21:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			You sit there for moral</p>
			<p begin="00:13:18:19" end="00:13:21:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		 support!</p>
			<p begin="00:13:21:23" end="00:13:23:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Let me move down</p>
			<p begin="00:13:21:23" end="00:13:23:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	because I don t want</p>
			<p begin="00:13:23:17" end="00:13:25:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	to see nothing honey!</p>
			<p begin="00:13:25:01" end="00:13:27:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Look mine is bare you</p>
			<p begin="00:13:25:01" end="00:13:27:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			the one with the jungle!</p>
			<p begin="00:13:28:00" end="00:13:29:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">		&gt;&gt; No it s a safari, honey.</p>
			<p begin="00:13:29:16" end="00:13:31:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			He likes to find</p>
			<p begin="00:13:29:16" end="00:13:31:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		the golden prize.</p>
			<p begin="00:13:31:21" end="00:13:36:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		Dr. Jackie: Hi Lisa!</p>
			<p begin="00:13:37:01" end="00:13:38:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; Hey Jackie!</p>
			<p begin="00:13:38:20" end="00:13:40:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Who brought this</p>
			<p begin="00:13:38:20" end="00:13:40:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	woman in my office?</p>
			<p begin="00:13:40:21" end="00:13:42:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		&gt;&gt; What s going on!?</p>
			<p begin="00:13:42:20" end="00:13:45:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Security, come</p>
			<p begin="00:13:42:20" end="00:13:45:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">get this lady!</p>
			<p begin="00:13:45:04" end="00:13:46:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; I came to see you</p>
			<p begin="00:13:45:04" end="00:13:46:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		and come for moral</p>
			<p begin="00:13:46:20" end="00:13:48:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	support with my girl!</p>
			<p begin="00:13:48:04" end="00:13:50:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; So, what brings you in</p>
			<p begin="00:13:48:04" end="00:13:50:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		today, Miss Lisa?</p>
			<p begin="00:13:50:13" end="00:13:52:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; I just wanted to see</p>
			<p begin="00:13:50:13" end="00:13:52:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	if you know,</p>
			<p begin="00:13:52:05" end="00:13:56:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">what I could be doing</p>
			<p begin="00:13:52:05" end="00:13:56:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			to get pregnant.</p>
			<p begin="00:13:56:14" end="00:13:58:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; You- you want to have</p>
			<p begin="00:13:56:14" end="00:13:58:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">another baby?</p>
			<p begin="00:13:58:20" end="00:14:00:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Yeah that s why</p>
			<p begin="00:13:58:20" end="00:14:00:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		I m here, Jackie.</p>
			<p begin="00:14:00:06" end="00:14:04:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		I m very, very focused on</p>
			<p begin="00:14:00:06" end="00:14:04:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		getting pregnant.</p>
			<p begin="00:14:04:09" end="00:14:06:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			&gt;&gt; As a doctor,</p>
			<p begin="00:14:04:09" end="00:14:06:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			this is the look I give.</p>
			<p begin="00:14:06:13" end="00:14:13:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			What I really wanted to</p>
			<p begin="00:14:06:13" end="00:14:13:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			say was,  What! </p>
			<p begin="00:14:13:09" end="00:14:15:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			One, are you practicing</p>
			<p begin="00:14:13:09" end="00:14:15:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		getting pregnant?</p>
			<p begin="00:14:15:12" end="00:14:16:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">&gt;&gt; Yes!</p>
			<p begin="00:14:16:21" end="00:14:18:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			&gt;&gt; But nothing s happened?</p>
			<p begin="00:14:18:09" end="00:14:19:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Nope.</p>
			<p begin="00:14:19:13" end="00:14:20:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; Nope, okay.</p>
			<p begin="00:14:20:13" end="00:14:23:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Well getting pregnant is</p>
			<p begin="00:14:20:13" end="00:14:23:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">sometimes age related.</p>
			<p begin="00:14:23:21" end="00:14:26:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			After thirty five, your</p>
			<p begin="00:14:23:21" end="00:14:26:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		chances of getting</p>
			<p begin="00:14:26:09" end="00:14:28:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	pregnant each month</p>
			<p begin="00:14:26:09" end="00:14:28:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			kind of plummet,</p>
			<p begin="00:14:28:18" end="00:14:32:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			however forty percent of</p>
			<p begin="00:14:28:18" end="00:14:32:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">	infertility can be the man.</p>
			<p begin="00:14:32:10" end="00:14:36:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		And so we do need to check</p>
			<p begin="00:14:32:10" end="00:14:36:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">Darren s sperm count.</p>
			<p begin="00:14:36:10" end="00:14:39:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	I m going to take a medical</p>
			<p begin="00:14:36:10" end="00:14:39:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		history from you.</p>
			<p begin="00:14:39:02" end="00:14:40:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Okay.</p>
			<p begin="00:14:40:09" end="00:14:41:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; Any surgeries</p>
			<p begin="00:14:40:09" end="00:14:41:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	in the past?</p>
			<p begin="00:14:41:22" end="00:14:46:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Yup, had a sea section</p>
			<p begin="00:14:41:22" end="00:14:46:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">with both of my kids,</p>
			<p begin="00:14:46:02" end="00:14:51:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	and I did have post</p>
			<p begin="00:14:46:02" end="00:14:51:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">surgery complications,</p>
			<p begin="00:14:51:05" end="00:14:52:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		I had a blood clot.</p>
			<p begin="00:14:52:14" end="00:14:55:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; What do you mean like</p>
			<p begin="00:14:52:14" end="00:14:55:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">a blood clot?</p>
			<p begin="00:14:55:02" end="00:14:56:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		Like a DVT?</p>
			<p begin="00:14:56:02" end="00:14:57:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">&gt;&gt; Yeah, a DVT.</p>
			<p begin="00:14:57:02" end="00:15:00:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			&gt;&gt; Deep Venus Thrombosis?</p>
			<p begin="00:15:00:07" end="00:15:02:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	That could be very dangerous</p>
			<p begin="00:15:00:07" end="00:15:02:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">because the clot could</p>
			<p begin="00:15:02:22" end="00:15:06:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		travel right on up</p>
			<p begin="00:15:02:22" end="00:15:06:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			to your  lungs.</p>
			<p begin="00:15:06:07" end="00:15:08:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			Ultimately, you</p>
			<p begin="00:15:06:07" end="00:15:08:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		could die!</p>
			<p begin="00:15:08:03" end="00:15:11:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		Your OB history is</p>
			<p begin="00:15:08:03" end="00:15:11:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		a little, shotty.</p>
			<p begin="00:15:11:21" end="00:15:14:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Let me cross the</p>
			<p begin="00:15:11:21" end="00:15:14:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			line right now,</p>
			<p begin="00:15:14:15" end="00:15:15:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">I do this all</p>
			<p begin="00:15:14:15" end="00:15:15:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		the time.</p>
			<p begin="00:15:15:18" end="00:15:18:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		I m no longer your doctor,</p>
			<p begin="00:15:15:18" end="00:15:18:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			I m a good girl friend.</p>
			<p begin="00:15:18:07" end="00:15:19:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Okay.</p>
			<p begin="00:15:19:07" end="00:15:23:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Are you that- needing</p>
			<p begin="00:15:19:07" end="00:15:23:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	another baby to the</p>
			<p begin="00:15:23:18" end="00:15:24:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			point you could</p>
			<p begin="00:15:23:18" end="00:15:24:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		potentially leave</p>
			<p begin="00:15:24:23" end="00:15:28:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	the two behind that</p>
			<p begin="00:15:24:23" end="00:15:28:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		you  have?</p>
			<p begin="00:15:28:04" end="00:15:29:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; We care about</p>
			<p begin="00:15:28:04" end="00:15:29:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		you Lisa,</p>
			<p begin="00:15:29:16" end="00:15:31:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			we care about you.</p>
			<p begin="00:15:31:19" end="00:15:33:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; I ve prayed long and</p>
			<p begin="00:15:31:19" end="00:15:33:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			hard about this,</p>
			<p begin="00:15:33:19" end="00:15:36:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">and I want to</p>
			<p begin="00:15:33:19" end="00:15:36:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	have a baby.</p>
			<p begin="00:15:36:20" end="00:15:38:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Okay.</p>
			<p begin="00:15:38:15" end="00:15:42:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; I understand the risk,</p>
			<p begin="00:15:38:15" end="00:15:42:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		I ve always had this risk.</p>
			<p begin="00:15:42:11" end="00:15:45:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	And despite this, I was able</p>
			<p begin="00:15:42:11" end="00:15:45:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">	to have two healthy babies,</p>
			<p begin="00:15:45:11" end="00:15:48:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			and I don t expect this</p>
			<p begin="00:15:45:11" end="00:15:48:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	pregnancy to</p>
			<p begin="00:15:48:15" end="00:15:49:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			be any different.</p>
			<p begin="00:15:49:23" end="00:15:51:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Lisa, we would</p>
			<p begin="00:15:49:23" end="00:15:51:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			like to get your</p>
			<p begin="00:15:51:23" end="00:15:52:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		blood drawn today...</p>
			<p begin="00:15:52:20" end="00:15:55:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">And I do have</p>
			<p begin="00:15:52:20" end="00:15:55:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			your latest pap.</p>
			<p begin="00:15:55:19" end="00:15:57:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			Everything s normal there.</p>
			<p begin="00:15:57:00" end="00:15:58:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; I went through that</p>
			<p begin="00:15:57:00" end="00:15:58:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			whole struggle.</p>
			<p begin="00:15:58:19" end="00:16:00:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">Wanting a baby</p>
			<p begin="00:15:58:19" end="00:16:00:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">later in life,</p>
			<p begin="00:16:00:16" end="00:16:01:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">but I couldn t.</p>
			<p begin="00:16:01:20" end="00:16:02:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">Okay, you ready?</p>
			<p begin="00:16:02:20" end="00:16:04:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">	&gt;&gt; No!</p>
			<p begin="00:16:04:04" end="00:16:08:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; I definitely empathize</p>
			<p begin="00:16:04:04" end="00:16:08:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		with Lisa, that you know,</p>
			<p begin="00:16:08:03" end="00:16:09:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">you want what you want.</p>
			<p begin="00:16:09:16" end="00:16:11:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			I m all about you having</p>
			<p begin="00:16:09:16" end="00:16:11:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">babies, girl.</p>
			<p begin="00:16:11:16" end="00:16:13:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			Have more babies!</p>
			<p begin="00:16:13:04" end="00:16:14:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Let me sit up,</p>
			<p begin="00:16:13:04" end="00:16:14:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">	I got to tell you something</p>
			<p begin="00:16:14:23" end="00:16:16:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		I ve been thinking</p>
			<p begin="00:16:14:23" end="00:16:16:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">about throwing</p>
			<p begin="00:16:16:19" end="00:16:21:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	an over the top, glamorous,</p>
			<p begin="00:16:16:19" end="00:16:21:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			fabulous, party!</p>
			<p begin="00:16:21:08" end="00:16:25:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			To celebrate, Lisa going</p>
			<p begin="00:16:21:08" end="00:16:25:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		to be with child!</p>
			<p begin="00:16:25:01" end="00:16:30:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Who has a party about</p>
			<p begin="00:16:25:01" end="00:16:30:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			trying to get pregnant?</p>
			<p begin="00:16:30:04" end="00:16:31:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">Lisa, my momma didn t</p>
			<p begin="00:16:30:04" end="00:16:31:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	know I was pregnant</p>
			<p begin="00:16:31:20" end="00:16:33:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">till I was seven months!</p>
			<p begin="00:16:33:16" end="00:16:34:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	Baby party,</p>
			<p begin="00:16:33:16" end="00:16:34:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		pre baby-</p>
			<p begin="00:16:34:20" end="00:16:36:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			&gt;&gt; No, it s not</p>
			<p begin="00:16:34:20" end="00:16:36:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">a baby party!</p>
			<p begin="00:16:36:03" end="00:16:38:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">It s just a celebration-</p>
			<p begin="00:16:38:01" end="00:16:39:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">&gt;&gt; Celebration of life?</p>
			<p begin="00:16:39:05" end="00:16:41:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Yeah, celebration</p>
			<p begin="00:16:39:05" end="00:16:41:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			of life!</p>
			<p begin="00:16:41:05" end="00:16:43:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	&gt;&gt; Certainly!</p>
			<p begin="00:16:43:02" end="00:16:44:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Now, normally in the</p>
			<p begin="00:16:43:02" end="00:16:44:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		black  community,</p>
			<p begin="00:16:44:10" end="00:16:46:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	isn t that a funeral.</p>
			<p begin="00:16:46:01" end="00:16:49:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		I mean I m excited for you</p>
			<p begin="00:16:46:01" end="00:16:49:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		it s a great undertaking.</p>
			<p begin="00:16:49:09" end="00:16:52:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		We ll all get together and</p>
			<p begin="00:16:49:09" end="00:16:52:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	you and Darren will</p>
			<p begin="00:16:52:06" end="00:16:54:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		here your results</p>
			<p begin="00:16:52:06" end="00:16:54:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		and create a plan-</p>
			<p begin="00:16:54:14" end="00:16:55:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		&gt;&gt; Can I-</p>
			<p begin="00:16:54:14" end="00:16:55:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	can I come ?</p>
			<p begin="00:16:55:13" end="00:16:56:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; Come where?</p>
			<p begin="00:16:56:21" end="00:16:58:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">&gt;&gt; To hear your results!</p>
			<p begin="00:16:58:17" end="00:17:00:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Which ones seman</p>
			<p begin="00:16:58:17" end="00:17:00:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		 analysis?</p>
			<p begin="00:17:00:05" end="00:17:04:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	&gt;&gt; Oh no, please understand</p>
			<p begin="00:17:00:05" end="00:17:04:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			I don t want to</p>
			<p begin="00:17:04:09" end="00:17:05:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			come to that one!</p>
			<p begin="00:17:05:12" end="00:17:09:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	[upbeat music]</p>
			<p begin="00:17:15:13" end="00:17:17:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	Cecil: Uh, yo, I think your</p>
			<p begin="00:17:15:13" end="00:17:17:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			mom pulling up.</p>
			<p begin="00:17:20:22" end="00:17:21:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">Miles: Hey mom!</p>
			<p begin="00:17:21:22" end="00:17:24:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Dr. Simone: Hey! How</p>
			<p begin="00:17:21:22" end="00:17:24:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			are you feeling?</p>
			<p begin="00:17:24:10" end="00:17:25:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Good. Good how</p>
			<p begin="00:17:24:10" end="00:17:25:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">are you doing?</p>
			<p begin="00:17:25:22" end="00:17:27:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			&gt;&gt; Good is your</p>
			<p begin="00:17:25:22" end="00:17:27:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">daddy inside?</p>
			<p begin="00:17:27:06" end="00:17:27:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Yeah.</p>
			<p begin="00:17:27:23" end="00:17:28:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Good.</p>
			<p begin="00:17:29:00" end="00:17:33:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">My, my, my, things are</p>
			<p begin="00:17:29:00" end="00:17:33:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		definitely different now,</p>
			<p begin="00:17:33:18" end="00:17:35:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">for Dr. Simone.</p>
			<p begin="00:17:35:22" end="00:17:38:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		&gt;&gt; What s going on?</p>
			<p begin="00:17:38:03" end="00:17:42:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; Cecil, the boys, and I,</p>
			<p begin="00:17:38:03" end="00:17:42:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			are not spending</p>
			<p begin="00:17:42:05" end="00:17:44:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">time together right now.</p>
			<p begin="00:17:44:03" end="00:17:46:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">Ya ll leave your doors</p>
			<p begin="00:17:44:03" end="00:17:46:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	open is that right?</p>
			<p begin="00:17:46:18" end="00:17:50:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Yeah, we do it the</p>
			<p begin="00:17:46:18" end="00:17:50:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			way we do it, now what?</p>
			<p begin="00:17:50:07" end="00:17:54:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; That s because we</p>
			<p begin="00:17:50:07" end="00:17:54:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	bought a second home</p>
			<p begin="00:17:54:03" end="00:17:57:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">right down the street</p>
			<p begin="00:17:54:03" end="00:17:57:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">from the boy s school.</p>
			<p begin="00:17:57:05" end="00:18:01:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">I m having to split my</p>
			<p begin="00:17:57:05" end="00:18:01:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			time between two houses.</p>
			<p begin="00:18:07:20" end="00:18:10:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Oh! That traffic</p>
			<p begin="00:18:07:20" end="00:18:10:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	was a beast!</p>
			<p begin="00:18:10:11" end="00:18:13:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Every time we allow the</p>
			<p begin="00:18:10:11" end="00:18:13:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		boys to forget something,</p>
			<p begin="00:18:13:10" end="00:18:15:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			then I have to stop over</p>
			<p begin="00:18:13:10" end="00:18:15:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	at the other house,</p>
			<p begin="00:18:15:10" end="00:18:20:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">and then that s adding</p>
			<p begin="00:18:15:10" end="00:18:20:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">to my commute.</p>
			<p begin="00:18:20:03" end="00:18:22:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Hey, did ya ll</p>
			<p begin="00:18:20:03" end="00:18:22:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		hear that?</p>
			<p begin="00:18:22:08" end="00:18:24:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			I had some real</p>
			<p begin="00:18:22:08" end="00:18:24:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">estate property in LA</p>
			<p begin="00:18:24:12" end="00:18:27:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			and sold the property so</p>
			<p begin="00:18:24:12" end="00:18:27:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			I had this money</p>
			<p begin="00:18:27:15" end="00:18:29:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	sitting in an account.</p>
			<p begin="00:18:29:03" end="00:18:30:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Yeah, this was</p>
			<p begin="00:18:29:03" end="00:18:30:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">daddy s idea.</p>
			<p begin="00:18:30:11" end="00:18:31:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="76% 5.33%">		&gt;&gt; Thank god for two houses!</p>
			<p begin="00:18:31:07" end="00:18:32:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; I m exhausted but-</p>
			<p begin="00:18:32:07" end="00:18:33:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; I m not exhausted</p>
			<p begin="00:18:32:07" end="00:18:33:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		I m happy.</p>
			<p begin="00:18:33:11" end="00:18:34:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">&gt;&gt; You re happy?</p>
			<p begin="00:18:34:16" end="00:18:35:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; I get to wake up</p>
			<p begin="00:18:34:16" end="00:18:35:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		a little bit late.</p>
			<p begin="00:18:35:19" end="00:18:38:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Our children were</p>
			<p begin="00:18:35:19" end="00:18:38:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		having to commute</p>
			<p begin="00:18:38:04" end="00:18:40:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			an hour each way</p>
			<p begin="00:18:38:04" end="00:18:40:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	to and from school.</p>
			<p begin="00:18:40:16" end="00:18:43:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="76% 5.33%">&gt;&gt; They were at a disadvantage</p>
			<p begin="00:18:40:16" end="00:18:43:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="73% 5.33%">	than some of the other kids.</p>
			<p begin="00:18:43:12" end="00:18:45:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			We re all pretty happy,</p>
			<p begin="00:18:43:12" end="00:18:45:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			this is-</p>
			<p begin="00:18:45:12" end="00:18:47:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; I m the only one</p>
			<p begin="00:18:45:12" end="00:18:47:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			who s not happy?</p>
			<p begin="00:18:47:03" end="00:18:48:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">&gt;&gt; Yup!</p>
			<p begin="00:18:48:05" end="00:18:50:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; Wait hold on,</p>
			<p begin="00:18:48:05" end="00:18:50:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">you re not happy that</p>
			<p begin="00:18:50:05" end="00:18:51:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			they re getting</p>
			<p begin="00:18:50:05" end="00:18:51:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	their homework done</p>
			<p begin="00:18:51:23" end="00:18:54:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			and eating and it s not</p>
			<p begin="00:18:51:23" end="00:18:54:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			eight o clock at night?</p>
			<p begin="00:18:54:23" end="00:18:56:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Sometimes during the</p>
			<p begin="00:18:54:23" end="00:18:56:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	week night,</p>
			<p begin="00:18:56:20" end="00:18:59:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			if I m on call,</p>
			<p begin="00:18:56:20" end="00:18:59:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		I actually have to</p>
			<p begin="00:18:59:04" end="00:19:01:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		stay at the north</p>
			<p begin="00:18:59:04" end="00:19:01:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			house because it s more</p>
			<p begin="00:19:01:11" end="00:19:03:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		convenient to the</p>
			<p begin="00:19:01:11" end="00:19:03:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		hospital.</p>
			<p begin="00:19:03:23" end="00:19:07:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Michael, when am</p>
			<p begin="00:19:03:23" end="00:19:07:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	I going to see some</p>
			<p begin="00:19:07:11" end="00:19:09:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">improvement on</p>
			<p begin="00:19:07:11" end="00:19:09:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	the grades?</p>
			<p begin="00:19:09:08" end="00:19:10:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	Michael: I don t know.</p>
			<p begin="00:19:10:07" end="00:19:11:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; What do you mean</p>
			<p begin="00:19:10:07" end="00:19:11:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			you don t know?</p>
			<p begin="00:19:11:17" end="00:19:13:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">		&gt;&gt; That s the wrong answer.</p>
			<p begin="00:19:13:00" end="00:19:15:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">You got to look at the</p>
			<p begin="00:19:13:00" end="00:19:15:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">sacrifices that mommy</p>
			<p begin="00:19:15:20" end="00:19:17:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	and daddy are making</p>
			<p begin="00:19:15:20" end="00:19:17:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">for you guys.</p>
			<p begin="00:19:17:20" end="00:19:21:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	I have to spend the night at</p>
			<p begin="00:19:17:20" end="00:19:21:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		the other house sometimes</p>
			<p begin="00:19:21:04" end="00:19:22:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		when I m on call,</p>
			<p begin="00:19:21:04" end="00:19:22:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	I m away from daddy,</p>
			<p begin="00:19:22:19" end="00:19:24:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">I m away from you guys.</p>
			<p begin="00:19:24:08" end="00:19:25:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	That s a lot!</p>
			<p begin="00:19:25:12" end="00:19:27:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; Woah, woah,</p>
			<p begin="00:19:25:12" end="00:19:27:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	woah, woah!</p>
			<p begin="00:19:27:21" end="00:19:31:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">It is a sacrifice but</p>
			<p begin="00:19:27:21" end="00:19:31:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">sometimes mommy sounds</p>
			<p begin="00:19:31:01" end="00:19:33:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		like she s having</p>
			<p begin="00:19:31:01" end="00:19:33:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		a ball over there</p>
			<p begin="00:19:33:01" end="00:19:34:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		at the other house.</p>
			<p begin="00:19:34:01" end="00:19:37:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">I m just going</p>
			<p begin="00:19:34:01" end="00:19:37:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			to keep it real!</p>
			<p begin="00:19:39:22" end="00:19:43:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	&gt;&gt; Candy, my favorite.</p>
			<p begin="00:19:43:09" end="00:19:44:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	It s clean, nobodies</p>
			<p begin="00:19:43:09" end="00:19:44:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	snatching the covers</p>
			<p begin="00:19:44:22" end="00:19:45:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			off of me!</p>
			<p begin="00:19:45:20" end="00:19:46:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			&gt;&gt; That s all I m saying!</p>
			<p begin="00:19:46:21" end="00:19:48:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			Let s keep it real, right?</p>
			<p begin="00:19:48:04" end="00:19:50:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">&gt;&gt; All right boys, ya ll went</p>
			<p begin="00:19:48:04" end="00:19:50:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">to help me straighten</p>
			<p begin="00:19:50:18" end="00:19:52:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">up the kitchen?</p>
			<p begin="00:19:52:01" end="00:19:55:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; I ll help you get</p>
			<p begin="00:19:52:01" end="00:19:55:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			some ice cream!</p>
			<p begin="00:19:55:01" end="00:19:56:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		Narrator:</p>
			<p begin="00:19:55:01" end="00:19:56:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		Coming up.</p>
			<p begin="00:19:56:12" end="00:19:59:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Toya: We having our</p>
			<p begin="00:19:56:12" end="00:19:59:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">own issues with taxes,</p>
			<p begin="00:19:59:06" end="00:20:03:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			at the end of the day we</p>
			<p begin="00:19:59:06" end="00:20:03:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		owe like 170,000.</p>
			<p begin="00:20:03:01" end="00:20:04:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; You be thankful we</p>
			<p begin="00:20:03:01" end="00:20:04:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">don t get started on-</p>
			<p begin="00:20:04:21" end="00:20:06:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">when you gonna</p>
			<p begin="00:20:04:21" end="00:20:06:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	have a baby!</p>
			<p begin="00:20:06:21" end="00:20:08:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">Quad: Understand baby,</p>
			<p begin="00:20:06:21" end="00:20:08:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">I m ready to take your</p>
			<p begin="00:20:08:18" end="00:20:13:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">whole f---ing face off!</p>
			<p begin="00:20:31:18" end="00:20:32:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">Toya: Hey lady!</p>
			<p begin="00:20:32:10" end="00:20:33:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="13% 5.33%">Quad:</p>
			<p begin="00:20:32:10" end="00:20:33:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">What s going on girl!</p>
			<p begin="00:20:33:10" end="00:20:34:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; Bailey s mad, everytime</p>
			<p begin="00:20:33:10" end="00:20:34:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		you come over here</p>
			<p begin="00:20:34:01" end="00:20:35:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			without children!</p>
			<p begin="00:20:35:04" end="00:20:37:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">&gt;&gt; Well I should have brought</p>
			<p begin="00:20:35:04" end="00:20:37:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			them but I had no idea!</p>
			<p begin="00:20:37:02" end="00:20:38:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Honey bailey s in</p>
			<p begin="00:20:37:02" end="00:20:38:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		here I thought it</p>
			<p begin="00:20:38:23" end="00:20:40:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			was a rottweiler</p>
			<p begin="00:20:38:23" end="00:20:40:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			in here, honey </p>
			<p begin="00:20:40:10" end="00:20:41:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; I was like Quad going</p>
			<p begin="00:20:40:10" end="00:20:41:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		to come over here</p>
			<p begin="00:20:41:22" end="00:20:43:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	and we going to cook!</p>
			<p begin="00:20:43:21" end="00:20:44:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	I even lit the grill.</p>
			<p begin="00:20:44:19" end="00:20:46:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Hold the line child,</p>
			<p begin="00:20:44:19" end="00:20:46:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">hold the line.</p>
			<p begin="00:20:46:23" end="00:20:49:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">Now I know damn well,</p>
			<p begin="00:20:46:23" end="00:20:49:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">you did not invite me</p>
			<p begin="00:20:49:07" end="00:20:50:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		to your house so I</p>
			<p begin="00:20:49:07" end="00:20:50:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		could cook at your</p>
			<p begin="00:20:50:10" end="00:20:51:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	house all day!</p>
			<p begin="00:20:51:11" end="00:20:52:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			[laughing]</p>
			<p begin="00:20:52:11" end="00:20:54:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		She would have me</p>
			<p begin="00:20:52:11" end="00:20:54:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			to do something</p>
			<p begin="00:20:54:11" end="00:20:55:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		like that with her</p>
			<p begin="00:20:54:11" end="00:20:55:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		tacky ass!</p>
			<p begin="00:20:55:22" end="00:20:57:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Toya it s understood that</p>
			<p begin="00:20:55:22" end="00:20:57:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	you brought me over</p>
			<p begin="00:20:57:15" end="00:20:58:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	to your house to cook!</p>
			<p begin="00:20:58:16" end="00:21:00:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	So what you re going</p>
			<p begin="00:20:58:16" end="00:21:00:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			to do is pour the wine!</p>
			<p begin="00:21:00:10" end="00:21:02:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">But I would rather eat</p>
			<p begin="00:21:00:10" end="00:21:02:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		my food than hers,</p>
			<p begin="00:21:02:08" end="00:21:04:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			so I m okay with it boo,</p>
			<p begin="00:21:02:08" end="00:21:04:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	where s the salmon?</p>
			<p begin="00:21:04:16" end="00:21:06:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Girl, so what s been</p>
			<p begin="00:21:04:16" end="00:21:06:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		going on with you?</p>
			<p begin="00:21:06:08" end="00:21:10:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Let me just tell you,</p>
			<p begin="00:21:06:08" end="00:21:10:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		it has literally so crazy.</p>
			<p begin="00:21:10:03" end="00:21:12:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			You know I have</p>
			<p begin="00:21:10:03" end="00:21:12:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		a younger brother?</p>
			<p begin="00:21:12:07" end="00:21:12:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">	&gt;&gt; No.</p>
			<p begin="00:21:12:23" end="00:21:13:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Yeah.</p>
			<p begin="00:21:13:22" end="00:21:15:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Who in the hell</p>
			<p begin="00:21:13:22" end="00:21:15:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	her brother?</p>
			<p begin="00:21:15:19" end="00:21:17:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; So he s twenty nine</p>
			<p begin="00:21:15:19" end="00:21:17:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		years old.</p>
			<p begin="00:21:17:22" end="00:21:18:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Quad ain t never</p>
			<p begin="00:21:17:22" end="00:21:18:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">mentioned her</p>
			<p begin="00:21:18:20" end="00:21:20:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	brother ever in life.</p>
			<p begin="00:21:20:03" end="00:21:20:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; And he has-</p>
			<p begin="00:21:20:23" end="00:21:21:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; Is he cute?</p>
			<p begin="00:21:21:18" end="00:21:23:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; Is he cute?</p>
			<p begin="00:21:21:18" end="00:21:23:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		Well girl,</p>
			<p begin="00:21:23:03" end="00:21:23:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">hold the line,</p>
			<p begin="00:21:23:03" end="00:21:23:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">hold the line.</p>
			<p begin="00:21:23:21" end="00:21:25:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	He came, he already</p>
			<p begin="00:21:23:21" end="00:21:25:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		came now,</p>
			<p begin="00:21:25:08" end="00:21:26:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	he came to the beach</p>
			<p begin="00:21:25:08" end="00:21:26:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		with the sand so-</p>
			<p begin="00:21:26:20" end="00:21:27:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; What!</p>
			<p begin="00:21:27:15" end="00:21:29:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		He came to Atlanta</p>
			<p begin="00:21:27:15" end="00:21:29:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">with a chick?</p>
			<p begin="00:21:29:09" end="00:21:32:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="26% 5.33%">			&gt;&gt; Yes!</p>
			<p begin="00:21:29:09" end="00:21:32:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			My nephew s mom!</p>
			<p begin="00:21:32:08" end="00:21:33:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Talking about what,</p>
			<p begin="00:21:32:08" end="00:21:33:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">you going to let them</p>
			<p begin="00:21:33:09" end="00:21:34:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	live with you?</p>
			<p begin="00:21:34:09" end="00:21:36:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Let them live with me?</p>
			<p begin="00:21:34:09" end="00:21:36:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		They live with me.</p>
			<p begin="00:21:36:08" end="00:21:39:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	&gt;&gt; That ain t even a secret</p>
			<p begin="00:21:36:08" end="00:21:39:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			you got to keep!</p>
			<p begin="00:21:39:20" end="00:21:42:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Like don t you want me to</p>
			<p begin="00:21:39:20" end="00:21:42:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		meet your family?</p>
			<p begin="00:21:42:09" end="00:21:44:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	You know I got a twenty-nine</p>
			<p begin="00:21:42:09" end="00:21:44:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">year old brother too.</p>
			<p begin="00:21:44:20" end="00:21:46:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			And he ask me if</p>
			<p begin="00:21:44:20" end="00:21:46:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	he can come</p>
			<p begin="00:21:46:19" end="00:21:47:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	stay with us</p>
			<p begin="00:21:46:19" end="00:21:47:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">recently too.</p>
			<p begin="00:21:47:14" end="00:21:49:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; And your answer was</p>
			<p begin="00:21:47:14" end="00:21:49:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">apparently no.</p>
			<p begin="00:21:49:08" end="00:21:50:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">&gt;&gt; For how long?</p>
			<p begin="00:21:50:10" end="00:21:51:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">And don t get me wrong</p>
			<p begin="00:21:50:10" end="00:21:51:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="73% 5.33%">	I know what Arabic families,</p>
			<p begin="00:21:52:00" end="00:21:53:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			they let them stay until</p>
			<p begin="00:21:52:00" end="00:21:53:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		they married off,</p>
			<p begin="00:21:53:16" end="00:21:54:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">but we re black!</p>
			<p begin="00:21:54:15" end="00:21:56:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		And I just</p>
			<p begin="00:21:54:15" end="00:21:56:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			don t feel like-</p>
			<p begin="00:21:56:00" end="00:21:57:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Black folks help</p>
			<p begin="00:21:56:00" end="00:21:57:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			each other girl!</p>
			<p begin="00:21:57:19" end="00:21:58:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; Yeah we do!</p>
			<p begin="00:21:58:17" end="00:22:00:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	But we can help each</p>
			<p begin="00:21:58:17" end="00:22:00:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">other from a distance!</p>
			<p begin="00:22:00:08" end="00:22:02:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Well my philosophy is</p>
			<p begin="00:22:00:08" end="00:22:02:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	a little different.</p>
			<p begin="00:22:02:09" end="00:22:04:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">That s been my thing,</p>
			<p begin="00:22:02:09" end="00:22:04:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">that s kind of what s</p>
			<p begin="00:22:04:08" end="00:22:05:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	going on in</p>
			<p begin="00:22:04:08" end="00:22:05:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		my house.</p>
			<p begin="00:22:05:10" end="00:22:07:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; We having our own</p>
			<p begin="00:22:05:10" end="00:22:07:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="73% 5.33%">	issues over here with taxes.</p>
			<p begin="00:22:07:16" end="00:22:09:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			&gt;&gt; Oh no ma am,</p>
			<p begin="00:22:07:16" end="00:22:09:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="16% 5.33%">honey!</p>
			<p begin="00:22:09:04" end="00:22:11:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">&gt;&gt; For years I was letting my</p>
			<p begin="00:22:09:04" end="00:22:11:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="73% 5.33%">	husband handle the finances.</p>
			<p begin="00:22:12:00" end="00:22:12:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; The bills yeah.</p>
			<p begin="00:22:12:21" end="00:22:15:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; He signed over</p>
			<p begin="00:22:12:21" end="00:22:15:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">power of attorney to-</p>
			<p begin="00:22:15:09" end="00:22:15:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			&gt;&gt; To who?</p>
			<p begin="00:22:15:22" end="00:22:16:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; To the accountant.</p>
			<p begin="00:22:16:17" end="00:22:18:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Right did you check</p>
			<p begin="00:22:16:17" end="00:22:18:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%"> credentials?</p>
			<p begin="00:22:18:01" end="00:22:19:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; I checked credentials</p>
			<p begin="00:22:18:01" end="00:22:19:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	through our friends</p>
			<p begin="00:22:19:20" end="00:22:21:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		but it wasn t like</p>
			<p begin="00:22:19:20" end="00:22:21:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">we checked through our</p>
			<p begin="00:22:21:02" end="00:22:23:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	family because we re</p>
			<p begin="00:22:21:02" end="00:22:23:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	the first generation</p>
			<p begin="00:22:23:01" end="00:22:24:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">in our family to make</p>
			<p begin="00:22:23:01" end="00:22:24:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		any money!</p>
			<p begin="00:22:24:13" end="00:22:31:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			It is crazy how we have</p>
			<p begin="00:22:24:13" end="00:22:31:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	to learn everything</p>
			<p begin="00:22:31:05" end="00:22:33:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			by failing first.</p>
			<p begin="00:22:33:01" end="00:22:34:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">I just started opening</p>
			<p begin="00:22:33:01" end="00:22:34:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	up the mail.</p>
			<p begin="00:22:34:14" end="00:22:35:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	I m confused.</p>
			<p begin="00:22:36:00" end="00:22:39:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I m seeing 70,000 owe</p>
			<p begin="00:22:36:00" end="00:22:39:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			in 2011.</p>
			<p begin="00:22:39:17" end="00:22:41:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; Toya ya ll haven t been</p>
			<p begin="00:22:39:17" end="00:22:41:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	paying ya ll taxes?</p>
			<p begin="00:22:41:21" end="00:22:44:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; At the end of the day</p>
			<p begin="00:22:41:21" end="00:22:44:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	we owe like 170,00!</p>
			<p begin="00:22:44:18" end="00:22:49:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Bitch, who owes 170,00</p>
			<p begin="00:22:44:18" end="00:22:49:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			to the damn IRS!</p>
			<p begin="00:22:49:22" end="00:22:50:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			&gt;&gt; It s the most scariest</p>
			<p begin="00:22:50:21" end="00:22:53:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		thing I have ever</p>
			<p begin="00:22:50:21" end="00:22:53:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			experienced in my life!</p>
			<p begin="00:22:53:03" end="00:22:54:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">&gt;&gt; How does this happen?</p>
			<p begin="00:22:54:14" end="00:22:56:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Girl let me close</p>
			<p begin="00:22:54:14" end="00:22:56:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">the curtains!</p>
			<p begin="00:22:56:09" end="00:22:58:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I m just going to get</p>
			<p begin="00:22:56:09" end="00:22:58:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			on out of here,</p>
			<p begin="00:22:58:06" end="00:23:00:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	see you when</p>
			<p begin="00:22:58:06" end="00:23:00:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		I see you!</p>
			<p begin="00:23:00:19" end="00:23:03:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			But not before you don t</p>
			<p begin="00:23:00:19" end="00:23:03:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			pay them taxes.</p>
			<p begin="00:23:03:13" end="00:23:05:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Eugene should have never</p>
			<p begin="00:23:03:13" end="00:23:05:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			signed them damn</p>
			<p begin="00:23:05:10" end="00:23:06:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		papers over to him.</p>
			<p begin="00:23:06:07" end="00:23:08:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">And we need to get him</p>
			<p begin="00:23:06:07" end="00:23:08:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		arrested!</p>
			<p begin="00:23:08:14" end="00:23:11:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">You don t mind getting</p>
			<p begin="00:23:08:14" end="00:23:11:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		a bitch arrested.</p>
			<p begin="00:23:11:07" end="00:23:14:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		&gt;&gt; All day!</p>
			<p begin="00:23:14:10" end="00:23:15:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			You need to stop</p>
			<p begin="00:23:14:10" end="00:23:15:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">talking about getting</p>
			<p begin="00:23:15:15" end="00:23:17:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			people arrested!</p>
			<p begin="00:23:15:15" end="00:23:17:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">You moved on?</p>
			<p begin="00:23:17:15" end="00:23:19:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		&gt;&gt; Have I moved on?</p>
			<p begin="00:23:19:02" end="00:23:20:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">			Moved on?</p>
			<p begin="00:23:20:01" end="00:23:21:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; From trying to get</p>
			<p begin="00:23:20:01" end="00:23:21:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	Miss Lisa arrested!</p>
			<p begin="00:23:21:01" end="00:23:24:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Oh honey I don t even</p>
			<p begin="00:23:21:01" end="00:23:24:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">think of that person.</p>
			<p begin="00:23:24:06" end="00:23:25:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">[overlapping arguments]</p>
			<p begin="00:23:25:17" end="00:23:27:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Lisa Nicole: What about</p>
			<p begin="00:23:25:17" end="00:23:27:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	your lesbian</p>
			<p begin="00:23:27:01" end="00:23:28:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		relationship, bitch!</p>
			<p begin="00:23:29:06" end="00:23:30:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Do what! Threw that</p>
			<p begin="00:23:29:06" end="00:23:30:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		water in my face!</p>
			<p begin="00:23:30:18" end="00:23:32:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Darren: Hold on.</p>
			<p begin="00:23:30:18" end="00:23:32:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			hold on.</p>
			<p begin="00:23:33:05" end="00:23:34:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Told you about this</p>
			<p begin="00:23:33:05" end="00:23:34:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		altercation at the</p>
			<p begin="00:23:34:20" end="00:23:37:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			restaurant with she who</p>
			<p begin="00:23:34:20" end="00:23:37:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	shall not be named.</p>
			<p begin="00:23:37:23" end="00:23:41:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; This is actionable,</p>
			<p begin="00:23:37:23" end="00:23:41:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">criminally, and civil.</p>
			<p begin="00:23:41:14" end="00:23:43:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; We just got an invite</p>
			<p begin="00:23:41:14" end="00:23:43:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		to a dinner party.</p>
			<p begin="00:23:43:19" end="00:23:45:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; Right! And she actually</p>
			<p begin="00:23:43:19" end="00:23:45:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	invited me.</p>
			<p begin="00:23:45:19" end="00:23:46:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			You know when it</p>
			<p begin="00:23:45:19" end="00:23:46:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			came through the</p>
			<p begin="00:23:46:22" end="00:23:48:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			wire I said,  Oh honey,</p>
			<p begin="00:23:46:22" end="00:23:48:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		who is this on the wire! </p>
			<p begin="00:23:48:15" end="00:23:51:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; All right, so she saved</p>
			<p begin="00:23:48:15" end="00:23:51:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			your number and</p>
			<p begin="00:23:51:16" end="00:23:52:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	you didn t block her</p>
			<p begin="00:23:51:16" end="00:23:52:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	that s good things.</p>
			<p begin="00:23:52:23" end="00:23:55:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Oh here she is,</p>
			<p begin="00:23:52:23" end="00:23:55:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		 I hope we can let</p>
			<p begin="00:23:55:06" end="00:23:56:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		bygones be bygones</p>
			<p begin="00:23:55:06" end="00:23:56:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			and move forward</p>
			<p begin="00:23:56:19" end="00:23:58:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">in a positive</p>
			<p begin="00:23:56:19" end="00:23:58:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		productive manner,</p>
			<p begin="00:23:58:07" end="00:24:00:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">please come over to my</p>
			<p begin="00:23:58:07" end="00:24:00:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		house for the celebration</p>
			<p begin="00:24:00:15" end="00:24:01:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">of life party! </p>
			<p begin="00:24:01:19" end="00:24:04:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	&gt;&gt; That s so nice of her are</p>
			<p begin="00:24:01:19" end="00:24:04:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="73% 5.33%">you actually going to attend?</p>
			<p begin="00:24:04:06" end="00:24:06:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Yeah, oh yeah,</p>
			<p begin="00:24:04:06" end="00:24:06:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		I m going!</p>
			<p begin="00:24:06:07" end="00:24:07:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; That s awesome!</p>
			<p begin="00:24:07:11" end="00:24:11:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	&gt;&gt; I have given everyone in</p>
			<p begin="00:24:07:11" end="00:24:11:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		this group a clean slate.</p>
			<p begin="00:24:11:15" end="00:24:12:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			We re going to go ahead</p>
			<p begin="00:24:11:15" end="00:24:12:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		and take this out.</p>
			<p begin="00:24:12:19" end="00:24:14:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	But you never know,</p>
			<p begin="00:24:12:19" end="00:24:14:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			you know</p>
			<p begin="00:24:14:22" end="00:24:16:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Miss Lisa Nicole</p>
			<p begin="00:24:14:22" end="00:24:16:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	cloud honey!</p>
			<p begin="00:24:16:00" end="00:24:18:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">You might have to keep</p>
			<p begin="00:24:16:00" end="00:24:18:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		one eye up on her,</p>
			<p begin="00:24:18:20" end="00:24:20:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			you know just one.</p>
			<p begin="00:24:20:12" end="00:24:21:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; You know I have</p>
			<p begin="00:24:20:12" end="00:24:21:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	the prettiest little</p>
			<p begin="00:24:21:17" end="00:24:25:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			cooks, seriously!</p>
			<p begin="00:24:25:04" end="00:24:28:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">[music]</p>
			<p begin="00:24:35:23" end="00:24:37:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">Darren: Oh hey!</p>
			<p begin="00:24:37:20" end="00:24:38:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	Lisa Nicole:</p>
			<p begin="00:24:37:20" end="00:24:38:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		Oh my god!</p>
			<p begin="00:24:38:12" end="00:24:39:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="16% 5.33%">		Hey!</p>
			<p begin="00:24:39:15" end="00:24:40:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">&gt;&gt; How you doing today?</p>
			<p begin="00:24:40:09" end="00:24:41:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	&gt;&gt; What are you doing?</p>
			<p begin="00:24:41:09" end="00:24:43:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Oh getting ready for</p>
			<p begin="00:24:41:09" end="00:24:43:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	work you know I got</p>
			<p begin="00:24:43:08" end="00:24:45:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">to do another</p>
			<p begin="00:24:43:08" end="00:24:45:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			overnight shift.</p>
			<p begin="00:24:45:08" end="00:24:47:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; How do you even</p>
			<p begin="00:24:45:08" end="00:24:47:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">	handle those shifts I mean-</p>
			<p begin="00:24:47:11" end="00:24:49:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; You know I was tired</p>
			<p begin="00:24:47:11" end="00:24:49:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">the other day.</p>
			<p begin="00:24:49:04" end="00:24:50:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	You know I got home</p>
			<p begin="00:24:49:04" end="00:24:50:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">at six in the morning</p>
			<p begin="00:24:50:23" end="00:24:52:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			and then as soon</p>
			<p begin="00:24:50:23" end="00:24:52:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	as I got home I had</p>
			<p begin="00:24:52:11" end="00:24:54:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			to do yard work,</p>
			<p begin="00:24:52:11" end="00:24:54:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	spring cleaning so.</p>
			<p begin="00:24:54:00" end="00:24:55:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Had to do your</p>
			<p begin="00:24:54:00" end="00:24:55:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">honey-do list?</p>
			<p begin="00:24:55:12" end="00:24:56:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; Yeah you made</p>
			<p begin="00:24:55:12" end="00:24:56:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="26% 5.33%">			me one.</p>
			<p begin="00:24:56:15" end="00:24:59:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			It s been busy you know</p>
			<p begin="00:24:56:15" end="00:24:59:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		I m working a lot</p>
			<p begin="00:24:59:13" end="00:25:01:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">more shifts than usual</p>
			<p begin="00:24:59:13" end="00:25:01:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">I m working a lot more</p>
			<p begin="00:25:01:17" end="00:25:03:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	overnight shifts so</p>
			<p begin="00:25:01:17" end="00:25:03:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">it s kind of hard for</p>
			<p begin="00:25:03:17" end="00:25:05:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			us to spend time</p>
			<p begin="00:25:03:17" end="00:25:05:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		at night.</p>
			<p begin="00:25:05:16" end="00:25:07:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; You know I had my</p>
			<p begin="00:25:05:16" end="00:25:07:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			appointment with Jackie!</p>
			<p begin="00:25:07:17" end="00:25:09:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		&gt;&gt; What appointment?</p>
			<p begin="00:25:09:10" end="00:25:14:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; You know, I am</p>
			<p begin="00:25:09:10" end="00:25:14:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	really serious about</p>
			<p begin="00:25:14:16" end="00:25:16:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	having a baby.</p>
			<p begin="00:25:16:17" end="00:25:18:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Now we talked-</p>
			<p begin="00:25:16:17" end="00:25:18:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	hey hold on,</p>
			<p begin="00:25:18:01" end="00:25:19:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	you know we</p>
			<p begin="00:25:18:01" end="00:25:19:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			talked about it,</p>
			<p begin="00:25:19:16" end="00:25:21:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		but I never really thought</p>
			<p begin="00:25:19:16" end="00:25:21:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">that you were</p>
			<p begin="00:25:21:17" end="00:25:22:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	that serious with it.</p>
			<p begin="00:25:22:21" end="00:25:24:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">You know the two three</p>
			<p begin="00:25:22:21" end="00:25:24:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			years from now,</p>
			<p begin="00:25:24:17" end="00:25:26:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			we re going to be close</p>
			<p begin="00:25:24:17" end="00:25:26:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		to our fifties so-</p>
			<p begin="00:25:26:17" end="00:25:27:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">		&gt;&gt; I am not!</p>
			<p begin="00:25:27:17" end="00:25:28:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">&gt;&gt; So you know-</p>
			<p begin="00:25:28:18" end="00:25:32:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; I am not well over</p>
			<p begin="00:25:28:18" end="00:25:32:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			into my forties,</p>
			<p begin="00:25:32:09" end="00:25:33:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	get it right!</p>
			<p begin="00:25:33:06" end="00:25:35:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Well, well the</p>
			<p begin="00:25:33:06" end="00:25:35:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		reality is we re-</p>
			<p begin="00:25:35:01" end="00:25:37:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">it is a ticking clock whether</p>
			<p begin="00:25:35:01" end="00:25:37:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	she likes it or not.</p>
			<p begin="00:25:38:00" end="00:25:41:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">I am going to give you</p>
			<p begin="00:25:38:00" end="00:25:41:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	my concerns.</p>
			<p begin="00:25:41:10" end="00:25:45:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	You have a clotting disorder</p>
			<p begin="00:25:41:10" end="00:25:45:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	where you re at risk</p>
			<p begin="00:25:45:17" end="00:25:50:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	of having a blood clot that</p>
			<p begin="00:25:45:17" end="00:25:50:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		will travel to your lung,</p>
			<p begin="00:25:50:06" end="00:25:52:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			which in pregnancy puts</p>
			<p begin="00:25:50:06" end="00:25:52:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	you at greater risk!</p>
			<p begin="00:25:52:13" end="00:25:55:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		The kids, you know</p>
			<p begin="00:25:52:13" end="00:25:55:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			they need their,</p>
			<p begin="00:25:55:06" end="00:25:57:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	they need their mama.</p>
			<p begin="00:25:57:18" end="00:26:03:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			I need my wife, we need</p>
			<p begin="00:25:57:18" end="00:26:03:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	this family, right?</p>
			<p begin="00:26:03:13" end="00:26:06:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	We re trying to grow</p>
			<p begin="00:26:03:13" end="00:26:06:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	to be in our</p>
			<p begin="00:26:06:22" end="00:26:09:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">seventies and eighties!</p>
			<p begin="00:26:09:18" end="00:26:13:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; I understand the risk</p>
			<p begin="00:26:09:18" end="00:26:13:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		and the desires of</p>
			<p begin="00:26:13:06" end="00:26:17:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">my heart are to birth</p>
			<p begin="00:26:13:06" end="00:26:17:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">another child.</p>
			<p begin="00:26:17:10" end="00:26:20:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		And to experience</p>
			<p begin="00:26:17:10" end="00:26:20:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			everything that bringing</p>
			<p begin="00:26:20:11" end="00:26:24:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="76% 5.33%">	a child in this world offers.</p>
			<p begin="00:26:24:03" end="00:26:29:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		I know it s risky, I just</p>
			<p begin="00:26:24:03" end="00:26:29:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	really want a baby.</p>
			<p begin="00:26:29:18" end="00:26:31:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; We have two</p>
			<p begin="00:26:29:18" end="00:26:31:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			beautiful ones.</p>
			<p begin="00:26:31:19" end="00:26:35:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; I want to just enjoy</p>
			<p begin="00:26:31:19" end="00:26:35:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			you know I think</p>
			<p begin="00:26:35:19" end="00:26:41:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	the first time I was</p>
			<p begin="00:26:35:19" end="00:26:41:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">so hungry for</p>
			<p begin="00:26:41:11" end="00:26:44:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">success and I was just</p>
			<p begin="00:26:41:11" end="00:26:44:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			grinding and then I look</p>
			<p begin="00:26:44:15" end="00:26:46:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			up and their not babies</p>
			<p begin="00:26:44:15" end="00:26:46:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	anymore and I just-</p>
			<p begin="00:26:46:16" end="00:26:49:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			I mean they grew</p>
			<p begin="00:26:46:16" end="00:26:49:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	up so fast.</p>
			<p begin="00:26:49:18" end="00:26:53:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; If you want to do it,</p>
			<p begin="00:26:49:18" end="00:26:53:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">I put my faith in God</p>
			<p begin="00:26:53:04" end="00:26:56:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			that you know he covers</p>
			<p begin="00:26:53:04" end="00:26:56:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			this pregnancy.</p>
			<p begin="00:26:56:03" end="00:26:57:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		Anything can happen.</p>
			<p begin="00:26:57:23" end="00:27:01:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		We just really put</p>
			<p begin="00:26:57:23" end="00:27:01:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		our faith in him.</p>
			<p begin="00:27:01:15" end="00:27:05:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	&gt;&gt; Jackie says all the same</p>
			<p begin="00:27:01:15" end="00:27:05:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		things you say, you know,</p>
			<p begin="00:27:05:05" end="00:27:08:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="76% 5.33%">I have this clotting disorder,</p>
			<p begin="00:27:05:05" end="00:27:08:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	it s very high risk.</p>
			<p begin="00:27:08:00" end="00:27:12:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	But she understands,</p>
			<p begin="00:27:08:00" end="00:27:12:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		she drew my blood,</p>
			<p begin="00:27:12:12" end="00:27:16:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		but we got to make</p>
			<p begin="00:27:12:12" end="00:27:16:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	sure you re working.</p>
			<p begin="00:27:16:12" end="00:27:20:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; I m working, what you</p>
			<p begin="00:27:16:12" end="00:27:20:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	mean, I am working.</p>
			<p begin="00:27:20:13" end="00:27:23:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Okay, it s working</p>
			<p begin="00:27:20:13" end="00:27:23:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		but we got to make</p>
			<p begin="00:27:23:13" end="00:27:25:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">sure your boys</p>
			<p begin="00:27:23:13" end="00:27:25:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">are swimming.</p>
			<p begin="00:27:25:20" end="00:27:27:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; They working they like</p>
			<p begin="00:27:25:20" end="00:27:27:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			Navy SEALs they</p>
			<p begin="00:27:27:16" end="00:27:28:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	going to hit</p>
			<p begin="00:27:27:16" end="00:27:28:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">their target.</p>
			<p begin="00:27:28:17" end="00:27:30:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; We just got to make</p>
			<p begin="00:27:28:17" end="00:27:30:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">sure you have enough!</p>
			<p begin="00:27:30:20" end="00:27:32:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">		You think they re swimming?</p>
			<p begin="00:27:32:19" end="00:27:36:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; I think they re okay</p>
			<p begin="00:27:32:19" end="00:27:36:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		I think they re great, no.</p>
			<p begin="00:27:36:19" end="00:27:43:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		No I m not</p>
			<p begin="00:27:36:19" end="00:27:43:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			going to no, no.</p>
			<p begin="00:27:46:13" end="00:27:48:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		Narrator:</p>
			<p begin="00:27:46:13" end="00:27:48:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		Coming up!</p>
			<p begin="00:27:48:05" end="00:27:49:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Darling, look what</p>
			<p begin="00:27:48:05" end="00:27:49:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		I just brought in.</p>
			<p begin="00:27:49:21" end="00:27:57:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">			&gt;&gt; Hello!</p>
			<p begin="00:28:03:21" end="00:28:05:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Alaura: What type of</p>
			<p begin="00:28:03:21" end="00:28:05:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	party is it?</p>
			<p begin="00:28:05:01" end="00:28:06:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Dr. Heavenly: Lisa Nicole</p>
			<p begin="00:28:05:01" end="00:28:06:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		always makes stuff fancy,</p>
			<p begin="00:28:06:17" end="00:28:08:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		so you got to kind</p>
			<p begin="00:28:06:17" end="00:28:08:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	of dress up.</p>
			<p begin="00:28:09:00" end="00:28:10:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		And you know black</p>
			<p begin="00:28:09:00" end="00:28:10:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			can pretty much</p>
			<p begin="00:28:10:12" end="00:28:11:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		go with everything.</p>
			<p begin="00:28:11:06" end="00:28:12:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Nope, we re not</p>
			<p begin="00:28:11:06" end="00:28:12:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">doing  black!</p>
			<p begin="00:28:12:10" end="00:28:13:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="21% 5.33%">&gt;&gt; Okay.</p>
			<p begin="00:28:17:13" end="00:28:19:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Toya: I m excited because</p>
			<p begin="00:28:17:13" end="00:28:19:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		Lisa s having the</p>
			<p begin="00:28:19:05" end="00:28:20:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	party tonight.</p>
			<p begin="00:28:20:02" end="00:28:21:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		I love free stuff</p>
			<p begin="00:28:20:02" end="00:28:21:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		right now,</p>
			<p begin="00:28:21:17" end="00:28:23:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		I ll take it! I ll</p>
			<p begin="00:28:21:17" end="00:28:23:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		take free dinners,</p>
			<p begin="00:28:23:22" end="00:28:25:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		I ll take free wine!</p>
			<p begin="00:28:25:12" end="00:28:27:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	We re trying to save</p>
			<p begin="00:28:25:12" end="00:28:27:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		money up in here,</p>
			<p begin="00:28:27:22" end="00:28:31:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			I m just keeping it real.</p>
			<p begin="00:28:32:13" end="00:28:33:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">Quad: C mon Miss Quad</p>
			<p begin="00:28:32:13" end="00:28:33:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="26% 5.33%">			 honey,</p>
			<p begin="00:28:33:18" end="00:28:35:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">get that face together!</p>
			<p begin="00:28:35:18" end="00:28:37:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Mother doesn t know</p>
			<p begin="00:28:35:18" end="00:28:37:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			what to expect,</p>
			<p begin="00:28:37:11" end="00:28:38:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			but I ll be there!</p>
			<p begin="00:28:38:23" end="00:28:41:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	Mmhmm, I ll be there, honey.</p>
			<p begin="00:28:38:23" end="00:28:41:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		With a poncho, a raincoat</p>
			<p begin="00:28:41:14" end="00:28:42:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		an umbrella, floats.</p>
			<p begin="00:28:42:18" end="00:28:45:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I might just come on</p>
			<p begin="00:28:42:18" end="00:28:45:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	in there in a yacht.</p>
			<p begin="00:28:45:03" end="00:28:48:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Face is beat, honey</p>
			<p begin="00:28:45:03" end="00:28:48:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">and not by Ike Turner!</p>
			<p begin="00:28:48:21" end="00:28:52:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			[classical music]</p>
			<p begin="00:29:02:23" end="00:29:08:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Lisa Nicole: Oh!</p>
			<p begin="00:29:02:23" end="00:29:08:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">Everything is exactly</p>
			<p begin="00:29:08:12" end="00:29:10:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		how I envisioned it!</p>
			<p begin="00:29:10:11" end="00:29:12:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">You all look beautiful!</p>
			<p begin="00:29:12:15" end="00:29:16:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Nothing like my signature</p>
			<p begin="00:29:12:15" end="00:29:16:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			models representing the</p>
			<p begin="00:29:16:06" end="00:29:18:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">Lisa Nicole collection.</p>
			<p begin="00:29:18:07" end="00:29:20:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	Flowers are beautiful!</p>
			<p begin="00:29:20:03" end="00:29:22:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			My linens are extravagant!</p>
			<p begin="00:29:22:11" end="00:29:25:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">		I am smiling on the inside.</p>
			<p begin="00:29:25:03" end="00:29:26:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			When they arrive</p>
			<p begin="00:29:25:03" end="00:29:26:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	just greet,</p>
			<p begin="00:29:26:23" end="00:29:29:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">welcome to the</p>
			<p begin="00:29:26:23" end="00:29:29:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">Noggles home.</p>
			<p begin="00:29:29:11" end="00:29:33:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">Anytime I do an event,</p>
			<p begin="00:29:29:11" end="00:29:33:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		I advertise my dress line.</p>
			<p begin="00:29:33:14" end="00:29:34:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">I m a walking billboard.</p>
			<p begin="00:29:34:20" end="00:29:36:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">And let s walk around</p>
			<p begin="00:29:34:20" end="00:29:36:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			ladies and make</p>
			<p begin="00:29:36:12" end="00:29:39:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	sure everything else</p>
			<p begin="00:29:36:12" end="00:29:39:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	is in order.</p>
			<p begin="00:29:45:11" end="00:29:45:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			Dwight: Hey baby!</p>
			<p begin="00:29:45:23" end="00:29:46:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">			&gt;&gt; Hello!</p>
			<p begin="00:29:46:19" end="00:29:48:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; You look fabulous!</p>
			<p begin="00:29:48:07" end="00:29:49:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	&gt;&gt; Thank you!</p>
			<p begin="00:29:49:10" end="00:29:53:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">		&gt;&gt; This dress is everthing!</p>
			<p begin="00:29:54:04" end="00:29:57:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="16% 5.33%">&gt;&gt; Hi!</p>
			<p begin="00:29:54:04" end="00:29:57:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			Hi, how are you?</p>
			<p begin="00:30:01:08" end="00:30:03:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		Curtis: Nice entry.</p>
			<p begin="00:30:03:07" end="00:30:05:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Welcome to the</p>
			<p begin="00:30:03:07" end="00:30:05:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		Noggles residence!</p>
			<p begin="00:30:05:13" end="00:30:08:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Dr. Jackie: Everything is</p>
			<p begin="00:30:05:13" end="00:30:08:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">over the top!</p>
			<p begin="00:30:08:08" end="00:30:11:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	There s red carpet,</p>
			<p begin="00:30:08:08" end="00:30:11:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	a classical pianist,</p>
			<p begin="00:30:11:00" end="00:30:12:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		and there s cheese</p>
			<p begin="00:30:11:00" end="00:30:12:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	everywhere!</p>
			<p begin="00:30:12:15" end="00:30:14:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; Hi, Jackie!</p>
			<p begin="00:30:14:04" end="00:30:15:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	&gt;&gt; Got your red going!</p>
			<p begin="00:30:15:08" end="00:30:18:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Which kind of works</p>
			<p begin="00:30:15:08" end="00:30:18:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">because Lisa s events</p>
			<p begin="00:30:18:16" end="00:30:22:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	can be kind</p>
			<p begin="00:30:18:16" end="00:30:22:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		of cheesy.</p>
			<p begin="00:30:28:08" end="00:30:29:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Eugene: So what you think</p>
			<p begin="00:30:28:08" end="00:30:29:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">	is going to happen tonight?</p>
			<p begin="00:30:29:16" end="00:30:30:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Toya: Why you think</p>
			<p begin="00:30:29:16" end="00:30:30:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		something s going</p>
			<p begin="00:30:30:19" end="00:30:31:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			to happen?</p>
			<p begin="00:30:31:17" end="00:30:32:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Cause something always</p>
			<p begin="00:30:31:17" end="00:30:32:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		 happens!</p>
			<p begin="00:30:33:00" end="00:30:34:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Welcome to the</p>
			<p begin="00:30:33:00" end="00:30:34:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	Noggle s residence!</p>
			<p begin="00:30:34:09" end="00:30:36:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	&gt;&gt; Thank you!</p>
			<p begin="00:30:36:17" end="00:30:38:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; What s up with the</p>
			<p begin="00:30:36:17" end="00:30:38:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	amazons at the door?</p>
			<p begin="00:30:38:13" end="00:30:39:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		&gt;&gt; And in Lisa wear!</p>
			<p begin="00:30:39:17" end="00:30:42:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			I think what in the hell!</p>
			<p begin="00:30:42:01" end="00:30:43:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; You look gorgeous!</p>
			<p begin="00:30:43:04" end="00:30:44:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; Hey Eugene,</p>
			<p begin="00:30:43:04" end="00:30:44:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	how are you?</p>
			<p begin="00:30:44:13" end="00:30:46:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">&gt;&gt; I was just</p>
			<p begin="00:30:44:13" end="00:30:46:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			telling Jackie,</p>
			<p begin="00:30:46:17" end="00:30:48:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">tonight, is a</p>
			<p begin="00:30:46:17" end="00:30:48:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	celebration of life!</p>
			<p begin="00:30:48:21" end="00:30:50:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">&gt;&gt; Why?</p>
			<p begin="00:30:50:04" end="00:30:51:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Because I m getting</p>
			<p begin="00:30:50:04" end="00:30:51:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			ready to try to</p>
			<p begin="00:30:51:18" end="00:30:54:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	get pregnant.</p>
			<p begin="00:30:54:09" end="00:30:55:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			&gt;&gt; Really?</p>
			<p begin="00:30:55:05" end="00:30:56:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">&gt;&gt; Yes.</p>
			<p begin="00:30:56:21" end="00:31:00:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; It s kind of awkward</p>
			<p begin="00:30:56:21" end="00:31:00:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	like the first thing</p>
			<p begin="00:31:00:13" end="00:31:03:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	is hey we re</p>
			<p begin="00:31:00:13" end="00:31:03:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">going to have a baby!</p>
			<p begin="00:31:03:18" end="00:31:05:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Ya ll want to get</p>
			<p begin="00:31:03:18" end="00:31:05:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			back in diapers?</p>
			<p begin="00:31:05:10" end="00:31:10:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; I do. I m getting this</p>
			<p begin="00:31:05:10" end="00:31:10:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	fever again.</p>
			<p begin="00:31:13:13" end="00:31:14:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			Dr. Heavenly: Hey pretty! </p>
			<p begin="00:31:14:11" end="00:31:15:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">		You so cute!</p>
			<p begin="00:31:15:21" end="00:31:17:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Dr. Simone: I would take</p>
			<p begin="00:31:15:21" end="00:31:17:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">that as a compliment-</p>
			<p begin="00:31:17:22" end="00:31:18:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	&gt;&gt; It is a compliment!</p>
			<p begin="00:31:19:00" end="00:31:23:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; If it were coming from</p>
			<p begin="00:31:19:00" end="00:31:23:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			anybody other than you!</p>
			<p begin="00:31:23:19" end="00:31:26:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Poor Simone was stuck</p>
			<p begin="00:31:23:19" end="00:31:26:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		at the North house</p>
			<p begin="00:31:26:03" end="00:31:27:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		by her self so we</p>
			<p begin="00:31:26:03" end="00:31:27:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			had to offer to</p>
			<p begin="00:31:27:21" end="00:31:29:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	pick her up,</p>
			<p begin="00:31:27:21" end="00:31:29:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">so baby we was</p>
			<p begin="00:31:29:10" end="00:31:31:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">nice to go get</p>
			<p begin="00:31:29:10" end="00:31:31:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		her right?</p>
			<p begin="00:31:31:02" end="00:31:32:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			Dr. Damon: Mmhmm.</p>
			<p begin="00:31:32:06" end="00:31:33:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Do you know what</p>
			<p begin="00:31:32:06" end="00:31:33:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">this evening is about?</p>
			<p begin="00:31:33:15" end="00:31:35:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		&gt;&gt; Not quite do you?</p>
			<p begin="00:31:35:02" end="00:31:37:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Well I didn t want</p>
			<p begin="00:31:35:02" end="00:31:37:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	to tell you,</p>
			<p begin="00:31:37:10" end="00:31:40:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">but I m going</p>
			<p begin="00:31:37:10" end="00:31:40:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		to be a god, mama!</p>
			<p begin="00:31:40:06" end="00:31:41:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; She s pregnant?</p>
			<p begin="00:31:41:14" end="00:31:44:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; Well not yet,</p>
			<p begin="00:31:41:14" end="00:31:44:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		don t say nothing!</p>
			<p begin="00:31:44:19" end="00:31:46:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			[laughing]</p>
			<p begin="00:31:46:03" end="00:31:47:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; Don t say nothing!</p>
			<p begin="00:31:47:18" end="00:31:52:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; A celebration of life</p>
			<p begin="00:31:47:18" end="00:31:52:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	party is not really</p>
			<p begin="00:31:52:10" end="00:31:56:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			announcing that you want</p>
			<p begin="00:31:52:10" end="00:31:56:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		to conceive party.</p>
			<p begin="00:31:56:07" end="00:32:01:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="76% 5.33%">We could call it, I m about to</p>
			<p begin="00:31:56:07" end="00:32:01:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="73% 5.33%">start prenatal vitamin party.</p>
			<p begin="00:32:01:15" end="00:32:02:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; Is Quad coming?</p>
			<p begin="00:32:02:11" end="00:32:03:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	&gt;&gt; I hope so!</p>
			<p begin="00:32:03:19" end="00:32:05:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		&gt;&gt; I like them both.</p>
			<p begin="00:32:05:04" end="00:32:07:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; I like them both even</p>
			<p begin="00:32:05:04" end="00:32:07:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			though you sided</p>
			<p begin="00:32:07:04" end="00:32:08:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	with Lisa completely.</p>
			<p begin="00:32:08:03" end="00:32:10:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; And you sided</p>
			<p begin="00:32:08:03" end="00:32:10:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		with Quad.</p>
			<p begin="00:32:13:19" end="00:32:15:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Welcome to the</p>
			<p begin="00:32:13:19" end="00:32:15:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	Noggle s residence.</p>
			<p begin="00:32:15:07" end="00:32:16:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			Cecil: Thank you!</p>
			<p begin="00:32:16:07" end="00:32:19:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Cutris: Now Darren s</p>
			<p begin="00:32:16:07" end="00:32:19:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">got some news,</p>
			<p begin="00:32:19:07" end="00:32:20:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I don t know if he s</p>
			<p begin="00:32:19:07" end="00:32:20:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			have you shared</p>
			<p begin="00:32:20:15" end="00:32:21:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			it with everyone?</p>
			<p begin="00:32:21:11" end="00:32:22:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			&gt;&gt; Yeah I-</p>
			<p begin="00:32:22:07" end="00:32:24:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">&gt;&gt; Don t be shy, c mon.</p>
			<p begin="00:32:24:12" end="00:32:25:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			&gt;&gt; You know Lisa s always-</p>
			<p begin="00:32:25:11" end="00:32:27:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		she wants another</p>
			<p begin="00:32:25:11" end="00:32:27:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			baby, so, yeah.</p>
			<p begin="00:32:27:10" end="00:32:33:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; So are we banking</p>
			<p begin="00:32:27:10" end="00:32:33:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">on a girl this</p>
			<p begin="00:32:33:07" end="00:32:34:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	time or twins?</p>
			<p begin="00:32:34:12" end="00:32:35:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">&gt;&gt; I don t care.</p>
			<p begin="00:32:35:10" end="00:32:37:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">I m happy with the two</p>
			<p begin="00:32:35:10" end="00:32:37:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	kids we got,</p>
			<p begin="00:32:37:08" end="00:32:38:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I m not trying to be</p>
			<p begin="00:32:37:08" end="00:32:38:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">in my sixties</p>
			<p begin="00:32:38:13" end="00:32:39:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		sending people off</p>
			<p begin="00:32:38:13" end="00:32:39:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	to college.</p>
			<p begin="00:32:39:23" end="00:32:41:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Yeah but that s what</p>
			<p begin="00:32:39:23" end="00:32:41:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			you about to do!</p>
			<p begin="00:32:41:05" end="00:32:44:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			[laughing]</p>
			<p begin="00:32:44:19" end="00:32:47:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I don t think Darren</p>
			<p begin="00:32:44:19" end="00:32:47:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	really wants a baby.</p>
			<p begin="00:32:47:16" end="00:32:49:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Why do you think</p>
			<p begin="00:32:47:16" end="00:32:49:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	that, honey?</p>
			<p begin="00:32:49:08" end="00:32:50:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Because he said</p>
			<p begin="00:32:49:08" end="00:32:50:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	he doesn t!</p>
			<p begin="00:32:50:15" end="00:32:51:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; You just say that!</p>
			<p begin="00:32:51:20" end="00:32:53:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; I did. He said-</p>
			<p begin="00:32:51:20" end="00:32:53:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">he said specifically,</p>
			<p begin="00:32:53:11" end="00:32:56:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	I have a boy, I have a girl,</p>
			<p begin="00:32:53:11" end="00:32:56:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		I m good.</p>
			<p begin="00:32:56:15" end="00:33:01:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			Well good luck,</p>
			<p begin="00:32:56:15" end="00:33:01:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			brother!</p>
			<p begin="00:33:05:04" end="00:33:07:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">		&gt;&gt; Oh hey!</p>
			<p begin="00:33:05:04" end="00:33:07:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			How ya ll doing, hello!?</p>
			<p begin="00:33:07:09" end="00:33:09:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">		Oh my lord!</p>
			<p begin="00:33:09:01" end="00:33:10:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">			&gt;&gt; Hello!</p>
			<p begin="00:33:10:04" end="00:33:11:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">&gt;&gt; Lady of the evening!</p>
			<p begin="00:33:11:20" end="00:33:14:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			Lisa look like Apollonia.</p>
			<p begin="00:33:14:12" end="00:33:16:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">She look like Lisa Lisa.</p>
			<p begin="00:33:16:08" end="00:33:18:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	She look like she s</p>
			<p begin="00:33:16:08" end="00:33:18:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">from the past!</p>
			<p begin="00:33:18:12" end="00:33:19:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">		&gt;&gt; Old soul?</p>
			<p begin="00:33:19:17" end="00:33:22:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Yeah old sould</p>
			<p begin="00:33:19:17" end="00:33:22:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	baby you helping me?</p>
			<p begin="00:33:22:04" end="00:33:25:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			[laughing]</p>
			<p begin="00:33:28:06" end="00:33:31:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="13% 5.33%">Quad:</p>
			<p begin="00:33:28:06" end="00:33:31:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	Hello, hello, hello.</p>
			<p begin="00:33:31:10" end="00:33:34:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="16% 5.33%">Oh hi,</p>
			<p begin="00:33:31:10" end="00:33:34:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">how you doing?</p>
			<p begin="00:33:34:05" end="00:33:37:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; I m extremely well</p>
			<p begin="00:33:34:05" end="00:33:37:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">now that you re here!</p>
			<p begin="00:33:37:01" end="00:33:38:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; Well let s have</p>
			<p begin="00:33:37:01" end="00:33:38:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			a party!</p>
			<p begin="00:33:38:10" end="00:33:40:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			&gt;&gt; She is sitting darling!</p>
			<p begin="00:33:40:02" end="00:33:41:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">			&gt;&gt; She is sitting pretty!</p>
			<p begin="00:33:41:21" end="00:33:43:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Hey what s going</p>
			<p begin="00:33:41:21" end="00:33:43:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		on Curtis?</p>
			<p begin="00:33:43:08" end="00:33:44:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		&gt;&gt; Good to see you!</p>
			<p begin="00:33:44:06" end="00:33:46:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Yeah you too man,</p>
			<p begin="00:33:44:06" end="00:33:46:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	long time long time.</p>
			<p begin="00:33:46:16" end="00:33:47:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; It was dead child.</p>
			<p begin="00:33:47:21" end="00:33:49:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; I mean you really kind</p>
			<p begin="00:33:47:21" end="00:33:49:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		of expect to come</p>
			<p begin="00:33:49:05" end="00:33:51:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		through the door,</p>
			<p begin="00:33:49:05" end="00:33:51:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">party s going,</p>
			<p begin="00:33:52:16" end="00:33:54:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			hey you see a few people</p>
			<p begin="00:33:52:16" end="00:33:54:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		you know,</p>
			<p begin="00:33:54:17" end="00:33:57:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Hey what s going on we re</p>
			<p begin="00:33:54:17" end="00:33:57:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">here to party!</p>
			<p begin="00:33:57:05" end="00:34:00:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">But it wasn t like that.</p>
			<p begin="00:34:00:03" end="00:34:02:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">&gt;&gt; No, hell no.</p>
			<p begin="00:34:04:22" end="00:34:06:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; I told him we got to</p>
			<p begin="00:34:04:22" end="00:34:06:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		make sure his boys</p>
			<p begin="00:34:06:14" end="00:34:08:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">aren t in wheel chairs-</p>
			<p begin="00:34:08:01" end="00:34:09:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Wheel chairs that s</p>
			<p begin="00:34:08:01" end="00:34:09:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	exactly what I said.</p>
			<p begin="00:34:09:04" end="00:34:10:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	&gt;&gt; And that they don t have</p>
			<p begin="00:34:09:04" end="00:34:10:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			two heads or two tails.</p>
			<p begin="00:34:10:18" end="00:34:12:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I told him everything</p>
			<p begin="00:34:10:18" end="00:34:12:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">that you said.</p>
			<p begin="00:34:12:18" end="00:34:14:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Look what I just</p>
			<p begin="00:34:12:18" end="00:34:14:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	brought in.</p>
			<p begin="00:34:14:02" end="00:34:14:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">			&gt;&gt; Hello!</p>
			<p begin="00:34:14:18" end="00:34:15:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="18% 5.33%">	&gt;&gt; Hi!</p>
			<p begin="00:34:15:18" end="00:34:19:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">	&gt;&gt; Uh oh, Quad, Lisa?</p>
			<p begin="00:34:19:18" end="00:34:21:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Welcome, I m so glad</p>
			<p begin="00:34:19:18" end="00:34:21:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">you all came.</p>
			<p begin="00:34:21:23" end="00:34:23:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">&gt;&gt; Thank you,</p>
			<p begin="00:34:21:23" end="00:34:23:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		thank you!</p>
			<p begin="00:34:23:03" end="00:34:26:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">			&gt;&gt; Whoo!</p>
			<p begin="00:34:23:03" end="00:34:26:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		Bad combo.</p>
			<p begin="00:34:28:18" end="00:34:29:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		Narrator:</p>
			<p begin="00:34:28:18" end="00:34:29:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		Coming up.</p>
			<p begin="00:34:29:22" end="00:34:31:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">Toya: The reality is,</p>
			<p begin="00:34:29:22" end="00:34:31:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			if somebody else</p>
			<p begin="00:34:31:17" end="00:34:32:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">	is raising your child-</p>
			<p begin="00:34:32:22" end="00:34:34:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Ain t nobody raising</p>
			<p begin="00:34:32:22" end="00:34:34:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			my kids,</p>
			<p begin="00:34:34:10" end="00:34:36:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	ain t nobody raising</p>
			<p begin="00:34:34:10" end="00:34:36:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			my kids.</p>
			<p begin="00:34:36:05" end="00:34:45:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		&gt;&gt; I m just saying.</p>
			<p begin="00:34:45:22" end="00:34:46:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			Dr. Jackie: You</p>
			<p begin="00:34:45:22" end="00:34:46:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">look fabulous!</p>
			<p begin="00:34:47:00" end="00:34:48:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			Quad: Thank you</p>
			<p begin="00:34:47:00" end="00:34:48:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">dear, you too!</p>
			<p begin="00:34:48:11" end="00:34:50:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Lisa Nicole: Welcome I m</p>
			<p begin="00:34:48:11" end="00:34:50:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">so glad you all came!</p>
			<p begin="00:34:50:16" end="00:34:51:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Dr. Gregory: Thank you,</p>
			<p begin="00:34:50:16" end="00:34:51:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		thank you!</p>
			<p begin="00:34:51:20" end="00:34:53:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Lisa Nicole is really</p>
			<p begin="00:34:51:20" end="00:34:53:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			representing the</p>
			<p begin="00:34:53:11" end="00:34:55:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">Lisa Nicole collection</p>
			<p begin="00:34:53:11" end="00:34:55:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="16% 5.33%">honey,</p>
			<p begin="00:34:55:07" end="00:34:58:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">very cheap and</p>
			<p begin="00:34:55:07" end="00:34:58:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		very late.</p>
			<p begin="00:34:59:23" end="00:35:01:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; I didn t notice what</p>
			<p begin="00:34:59:23" end="00:35:01:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	she had on.</p>
			<p begin="00:35:01:07" end="00:35:02:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Oh yeah, I don t see</p>
			<p begin="00:35:01:07" end="00:35:02:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">how you could.</p>
			<p begin="00:35:02:19" end="00:35:05:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			It was like a Christmas</p>
			<p begin="00:35:02:19" end="00:35:05:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		stocking.</p>
			<p begin="00:35:05:11" end="00:35:07:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; I know we ve had</p>
			<p begin="00:35:05:11" end="00:35:07:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		our challenges so</p>
			<p begin="00:35:07:04" end="00:35:08:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I m really glad that</p>
			<p begin="00:35:07:04" end="00:35:08:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		you came.</p>
			<p begin="00:35:08:11" end="00:35:11:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">I m excited to really</p>
			<p begin="00:35:08:11" end="00:35:11:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			move forward and</p>
			<p begin="00:35:11:19" end="00:35:14:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			let the past be</p>
			<p begin="00:35:11:19" end="00:35:14:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		the past.</p>
			<p begin="00:35:14:02" end="00:35:15:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; It s old it s done</p>
			<p begin="00:35:14:02" end="00:35:15:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">it doesn t need to be-</p>
			<p begin="00:35:15:19" end="00:35:16:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		&gt;&gt; Can I have a hug?</p>
			<p begin="00:35:16:18" end="00:35:17:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Talked about again,</p>
			<p begin="00:35:16:18" end="00:35:17:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	it just needs to be</p>
			<p begin="00:35:17:20" end="00:35:21:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			dead on arrival,</p>
			<p begin="00:35:17:20" end="00:35:21:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			and it is dead.</p>
			<p begin="00:35:21:22" end="00:35:23:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			Let me just keep</p>
			<p begin="00:35:21:22" end="00:35:23:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			it real.</p>
			<p begin="00:35:23:20" end="00:35:25:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	She who shall not be</p>
			<p begin="00:35:23:20" end="00:35:25:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			named and I will</p>
			<p begin="00:35:25:17" end="00:35:27:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		never be friends,</p>
			<p begin="00:35:25:17" end="00:35:27:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		but the medical community</p>
			<p begin="00:35:27:16" end="00:35:29:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">is very small,</p>
			<p begin="00:35:27:16" end="00:35:29:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		so that forces us</p>
			<p begin="00:35:29:19" end="00:35:31:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			to be around each other</p>
			<p begin="00:35:29:19" end="00:35:31:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		from time to time.</p>
			<p begin="00:35:31:04" end="00:35:34:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">Well let s go out here</p>
			<p begin="00:35:31:04" end="00:35:34:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		and see the other ladies!</p>
			<p begin="00:35:34:08" end="00:35:36:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">We re making a little</p>
			<p begin="00:35:34:08" end="00:35:36:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	progress so</p>
			<p begin="00:35:36:01" end="00:35:39:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		I guess I can call</p>
			<p begin="00:35:36:01" end="00:35:39:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		her cloud.</p>
			<p begin="00:35:44:21" end="00:35:46:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">Toya: What s up ladies!</p>
			<p begin="00:35:46:16" end="00:35:49:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">Dr. Heavenly: Give me</p>
			<p begin="00:35:46:16" end="00:35:49:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			some love girl!</p>
			<p begin="00:35:51:16" end="00:35:56:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">[overlapping greetings]</p>
			<p begin="00:35:56:12" end="00:35:58:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">Well Miss Quad is here</p>
			<p begin="00:35:56:12" end="00:35:58:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			honey and I m so</p>
			<p begin="00:35:58:17" end="00:36:00:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		glad to see her in</p>
			<p begin="00:35:58:17" end="00:36:00:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">good spirits.</p>
			<p begin="00:36:00:04" end="00:36:02:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			We were in a bad</p>
			<p begin="00:36:00:04" end="00:36:02:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			place last year.</p>
			<p begin="00:36:02:08" end="00:36:05:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; So why don t we all</p>
			<p begin="00:36:02:08" end="00:36:05:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">just drop it,</p>
			<p begin="00:36:05:01" end="00:36:06:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		drop the charges,</p>
			<p begin="00:36:05:01" end="00:36:06:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		drop the-</p>
			<p begin="00:36:06:03" end="00:36:08:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Well here s the thing</p>
			<p begin="00:36:06:03" end="00:36:08:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			we not going to do that.</p>
			<p begin="00:36:08:01" end="00:36:09:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">We re going to have us</p>
			<p begin="00:36:08:01" end="00:36:09:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	a good time,</p>
			<p begin="00:36:09:08" end="00:36:10:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">let s have us</p>
			<p begin="00:36:09:08" end="00:36:10:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			a glass of wine-</p>
			<p begin="00:36:10:14" end="00:36:12:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">			[overlapping conversation]</p>
			<p begin="00:36:12:20" end="00:36:13:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Baby you going to</p>
			<p begin="00:36:12:20" end="00:36:13:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		walk away from me?</p>
			<p begin="00:36:13:15" end="00:36:15:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			I m glad that we</p>
			<p begin="00:36:13:15" end="00:36:15:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			can start over,</p>
			<p begin="00:36:15:06" end="00:36:18:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">I love me some</p>
			<p begin="00:36:15:06" end="00:36:18:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		Miss Quad.</p>
			<p begin="00:36:18:05" end="00:36:19:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Why is everybody</p>
			<p begin="00:36:18:05" end="00:36:19:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	sitting down</p>
			<p begin="00:36:19:20" end="00:36:21:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">and there s no dancing.</p>
			<p begin="00:36:21:02" end="00:36:23:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Toya: Cause it ain t</p>
			<p begin="00:36:21:02" end="00:36:23:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		no party!</p>
			<p begin="00:36:23:13" end="00:36:25:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">			[laughing]</p>
			<p begin="00:36:26:00" end="00:36:27:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			&gt;&gt; What are you</p>
			<p begin="00:36:26:00" end="00:36:27:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			saying over there Toya?</p>
			<p begin="00:36:27:12" end="00:36:28:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; I m about to teach</p>
			<p begin="00:36:27:12" end="00:36:28:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			you how to throw</p>
			<p begin="00:36:28:13" end="00:36:29:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">a party honey</p>
			<p begin="00:36:28:13" end="00:36:29:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">because this-</p>
			<p begin="00:36:29:21" end="00:36:31:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			&gt;&gt; Oh you mean if we re</p>
			<p begin="00:36:29:21" end="00:36:31:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">not turning up</p>
			<p begin="00:36:31:05" end="00:36:32:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			and fighting it</p>
			<p begin="00:36:31:05" end="00:36:32:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">ain t a party?</p>
			<p begin="00:36:32:13" end="00:36:35:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			We can t have an elegant</p>
			<p begin="00:36:32:13" end="00:36:35:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		affair without the drama?</p>
			<p begin="00:36:35:06" end="00:36:37:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">&gt;&gt; Where is the alcohol?</p>
			<p begin="00:36:37:10" end="00:36:41:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		There s no music,</p>
			<p begin="00:36:37:10" end="00:36:41:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			there s no one dancing,</p>
			<p begin="00:36:41:13" end="00:36:43:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		there s wine in a</p>
			<p begin="00:36:41:13" end="00:36:43:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			bucket now that</p>
			<p begin="00:36:43:09" end="00:36:45:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		I ve found the wine.</p>
			<p begin="00:36:45:01" end="00:36:47:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">You supposed to appeal</p>
			<p begin="00:36:45:01" end="00:36:47:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			to your guests!</p>
			<p begin="00:36:47:14" end="00:36:49:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; What Toya, why you</p>
			<p begin="00:36:47:14" end="00:36:49:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	always got something</p>
			<p begin="00:36:49:11" end="00:36:51:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	to say about</p>
			<p begin="00:36:49:11" end="00:36:51:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		somebodies party?</p>
			<p begin="00:36:51:02" end="00:36:53:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Because I wanted</p>
			<p begin="00:36:51:02" end="00:36:53:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">it to be fun!</p>
			<p begin="00:36:53:05" end="00:36:54:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Why don t you turn</p>
			<p begin="00:36:53:05" end="00:36:54:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	up then if you want</p>
			<p begin="00:36:54:14" end="00:36:57:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">it to be fun,</p>
			<p begin="00:36:54:14" end="00:36:57:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		you make the fun!</p>
			<p begin="00:36:57:18" end="00:37:01:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Dr. Jackie: Please lord</p>
			<p begin="00:36:57:18" end="00:37:01:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			don t let Toya turn up.</p>
			<p begin="00:37:01:03" end="00:37:03:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">If it means no</p>
			<p begin="00:37:01:03" end="00:37:03:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			drama  tonight,</p>
			<p begin="00:37:03:10" end="00:37:06:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="61% 5.33%">let s stick with boring.</p>
			<p begin="00:37:06:01" end="00:37:07:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; Well let me</p>
			<p begin="00:37:06:01" end="00:37:07:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">just say this,</p>
			<p begin="00:37:07:09" end="00:37:10:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	I really am thankful</p>
			<p begin="00:37:07:09" end="00:37:10:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">that all of us</p>
			<p begin="00:37:10:22" end="00:37:13:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">are here tonight and I</p>
			<p begin="00:37:10:22" end="00:37:13:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	just thank you guys</p>
			<p begin="00:37:13:10" end="00:37:14:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">for coming out</p>
			<p begin="00:37:13:10" end="00:37:14:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			and having this</p>
			<p begin="00:37:14:21" end="00:37:18:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			celebration of life with</p>
			<p begin="00:37:14:21" end="00:37:18:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			us I mean it s not going</p>
			<p begin="00:37:18:02" end="00:37:20:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	to be an easy accom-</p>
			<p begin="00:37:18:02" end="00:37:20:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">feet to get pregnant.</p>
			<p begin="00:37:20:23" end="00:37:25:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	&gt;&gt; Am I hearing this</p>
			<p begin="00:37:20:23" end="00:37:25:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	 correctly?</p>
			<p begin="00:37:25:01" end="00:37:28:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; And I m excited that my</p>
			<p begin="00:37:25:01" end="00:37:28:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			husband is in agreement.</p>
			<p begin="00:37:28:22" end="00:37:30:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Oh honey that is a two</p>
			<p begin="00:37:28:22" end="00:37:30:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		par trick you see</p>
			<p begin="00:37:30:23" end="00:37:33:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">first you got to get a</p>
			<p begin="00:37:30:23" end="00:37:33:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			woman who s over</p>
			<p begin="00:37:33:03" end="00:37:35:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			forty pregnant,</p>
			<p begin="00:37:33:03" end="00:37:35:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">and secondly,</p>
			<p begin="00:37:35:19" end="00:37:39:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		you got to convince a man</p>
			<p begin="00:37:35:19" end="00:37:39:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			of the travelling pants.</p>
			<p begin="00:37:39:15" end="00:37:41:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">Oh good luck with that!</p>
			<p begin="00:37:41:11" end="00:37:43:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	&gt;&gt; Listen, I have a question</p>
			<p begin="00:37:41:11" end="00:37:43:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			since there are</p>
			<p begin="00:37:43:07" end="00:37:45:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">two OBGYN s here that</p>
			<p begin="00:37:43:07" end="00:37:45:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			know about this.</p>
			<p begin="00:37:45:23" end="00:37:46:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">			&gt;&gt; Right.</p>
			<p begin="00:37:46:19" end="00:37:49:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; How old is too old</p>
			<p begin="00:37:46:19" end="00:37:49:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			to have a child?</p>
			<p begin="00:37:49:19" end="00:37:53:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Look at this couch,</p>
			<p begin="00:37:49:19" end="00:37:53:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			that s too old.</p>
			<p begin="00:37:53:07" end="00:37:54:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">&gt;&gt; My timeline is fine.</p>
			<p begin="00:37:54:04" end="00:37:56:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; Well wait a minute</p>
			<p begin="00:37:54:04" end="00:37:56:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		let s hear it from</p>
			<p begin="00:37:56:16" end="00:37:58:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		the experts hold up!</p>
			<p begin="00:37:58:15" end="00:38:01:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; There s an increase in</p>
			<p begin="00:37:58:15" end="00:38:01:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			the risk of chromosomal</p>
			<p begin="00:38:01:10" end="00:38:03:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		abnormalities right around</p>
			<p begin="00:38:01:10" end="00:38:03:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			the age of thirty five.</p>
			<p begin="00:38:03:22" end="00:38:06:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Dr. Gregory: Are you</p>
			<p begin="00:38:03:22" end="00:38:06:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	 listening?</p>
			<p begin="00:38:06:11" end="00:38:09:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	&gt;&gt; Also, there s a decrease</p>
			<p begin="00:38:06:11" end="00:38:09:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			in the chance of getting</p>
			<p begin="00:38:09:16" end="00:38:12:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			pregnant each month and</p>
			<p begin="00:38:09:16" end="00:38:12:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		by the age of forty- five,</p>
			<p begin="00:38:12:11" end="00:38:15:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">less than five percent chance</p>
			<p begin="00:38:12:11" end="00:38:15:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		that you ll get pregnant.</p>
			<p begin="00:38:15:20" end="00:38:19:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		And Greg, she s not forty-</p>
			<p begin="00:38:15:20" end="00:38:19:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="73% 5.33%">	five yet so leave her alone!</p>
			<p begin="00:38:20:00" end="00:38:21:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="16% 5.33%">	Okay!</p>
			<p begin="00:38:21:04" end="00:38:23:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; I m just a small</p>
			<p begin="00:38:21:04" end="00:38:23:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			country doctor,</p>
			<p begin="00:38:23:00" end="00:38:25:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			trying to have a</p>
			<p begin="00:38:23:00" end="00:38:25:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			baby of my own.</p>
			<p begin="00:38:25:11" end="00:38:26:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		Dr. Simone: Agreed.</p>
			<p begin="00:38:26:13" end="00:38:29:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Quad is sitting over</p>
			<p begin="00:38:26:13" end="00:38:29:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		there giggling and</p>
			<p begin="00:38:29:04" end="00:38:30:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="58% 5.33%">drinking her champagne.</p>
			<p begin="00:38:30:17" end="00:38:33:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	I m her girlfriend,</p>
			<p begin="00:38:30:17" end="00:38:33:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	I m her obstetrician</p>
			<p begin="00:38:33:15" end="00:38:36:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">gynecologist ,</p>
			<p begin="00:38:33:15" end="00:38:36:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		she needs a baby.</p>
			<p begin="00:38:36:16" end="00:38:38:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		We re sitting here talking</p>
			<p begin="00:38:36:16" end="00:38:38:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">about Lisa and Darren,</p>
			<p begin="00:38:38:09" end="00:38:42:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	who gives a-</p>
			<p begin="00:38:38:09" end="00:38:42:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	about them?</p>
			<p begin="00:38:42:09" end="00:38:43:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Dr. Eugene: You all are</p>
			<p begin="00:38:42:09" end="00:38:43:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			focused more on</p>
			<p begin="00:38:43:15" end="00:38:46:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">all the complications</p>
			<p begin="00:38:43:15" end="00:38:46:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">of you know the utero-</p>
			<p begin="00:38:46:04" end="00:38:47:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">	&gt;&gt; The mother.</p>
			<p begin="00:38:47:07" end="00:38:50:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Once the baby s born,</p>
			<p begin="00:38:47:07" end="00:38:50:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		it s a whole other thing.</p>
			<p begin="00:38:50:11" end="00:38:53:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		I ve seen mothers,</p>
			<p begin="00:38:50:11" end="00:38:53:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		who are sixty with</p>
			<p begin="00:38:54:00" end="00:38:56:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		you know,</p>
			<p begin="00:38:54:00" end="00:38:56:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		a twelve year old.</p>
			<p begin="00:38:56:18" end="00:38:58:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		You know they look</p>
			<p begin="00:38:56:18" end="00:38:58:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">like the grandmother!</p>
			<p begin="00:38:59:00" end="00:39:01:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			And they re beaten down</p>
			<p begin="00:38:59:00" end="00:39:01:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">	and they re kind of broken,</p>
			<p begin="00:39:01:05" end="00:39:03:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">you know hopefully you</p>
			<p begin="00:39:01:05" end="00:39:03:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">all have thought this</p>
			<p begin="00:39:03:13" end="00:39:05:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		through that this</p>
			<p begin="00:39:03:13" end="00:39:05:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	isn t just a fever.</p>
			<p begin="00:39:05:21" end="00:39:08:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; Just a minute, you re</p>
			<p begin="00:39:05:21" end="00:39:08:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="66% 5.33%">			insulting me right now.</p>
			<p begin="00:39:08:01" end="00:39:09:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		&gt;&gt; That s insulting?</p>
			<p begin="00:39:09:04" end="00:39:12:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; It is. My husband is a</p>
			<p begin="00:39:09:04" end="00:39:12:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			physician just like you,</p>
			<p begin="00:39:12:18" end="00:39:15:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		so he s very aware</p>
			<p begin="00:39:12:18" end="00:39:15:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	of the risk.</p>
			<p begin="00:39:15:05" end="00:39:16:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	Darren: Let me make</p>
			<p begin="00:39:15:05" end="00:39:16:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		the point.</p>
			<p begin="00:39:16:01" end="00:39:17:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">			&gt;&gt; As am I, and I-</p>
			<p begin="00:39:17:14" end="00:39:19:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; Let me, let me</p>
			<p begin="00:39:17:14" end="00:39:19:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">make a point.</p>
			<p begin="00:39:19:09" end="00:39:21:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			You know Eugene,</p>
			<p begin="00:39:19:09" end="00:39:21:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">		if I was a forty year old,</p>
			<p begin="00:39:21:13" end="00:39:25:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">weight problems, COPD,</p>
			<p begin="00:39:21:13" end="00:39:25:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			congestive hear failure,</p>
			<p begin="00:39:25:17" end="00:39:28:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">not be able to do it,</p>
			<p begin="00:39:25:17" end="00:39:28:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="71% 5.33%">	then I would be conscience.</p>
			<p begin="00:39:28:09" end="00:39:30:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	&gt;&gt; You need to add something</p>
			<p begin="00:39:28:09" end="00:39:30:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	to that list though,</p>
			<p begin="00:39:30:01" end="00:39:31:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			if you were a forty year</p>
			<p begin="00:39:30:01" end="00:39:31:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	old who didn t have</p>
			<p begin="00:39:31:21" end="00:39:35:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			a live in nanny,</p>
			<p begin="00:39:31:21" end="00:39:35:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">but the reality is if</p>
			<p begin="00:39:35:02" end="00:39:36:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			somebody else is</p>
			<p begin="00:39:35:02" end="00:39:36:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		raising your child</p>
			<p begin="00:39:36:22" end="00:39:38:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	you can have as many</p>
			<p begin="00:39:36:22" end="00:39:38:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	babies as you want.</p>
			<p begin="00:39:38:18" end="00:39:40:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		&gt;&gt; Ain t nobody raisin my</p>
			<p begin="00:39:38:18" end="00:39:40:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			kids aint nobody</p>
			<p begin="00:39:40:02" end="00:39:41:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">raising my kids!</p>
			<p begin="00:39:41:02" end="00:39:44:06" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; You could have a baby</p>
			<p begin="00:39:41:02" end="00:39:44:06" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">and a nanny c mon now!</p>
			<p begin="00:39:44:06" end="00:39:46:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	Toya right,</p>
			<p begin="00:39:44:06" end="00:39:46:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">Toya ain t right about</p>
			<p begin="00:39:46:01" end="00:39:47:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	a lot of things but</p>
			<p begin="00:39:46:01" end="00:39:47:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		she right tonight.</p>
			<p begin="00:39:47:19" end="00:39:50:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">&gt;&gt; I m not going to apologize</p>
			<p begin="00:39:47:19" end="00:39:50:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			for having help!</p>
			<p begin="00:39:50:05" end="00:39:54:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">Toya, I have a nanny,</p>
			<p begin="00:39:50:05" end="00:39:54:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			so what!</p>
			<p begin="00:39:54:02" end="00:39:56:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Most career woman</p>
			<p begin="00:39:54:02" end="00:39:56:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			do have nannies!</p>
			<p begin="00:39:56:05" end="00:39:57:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		Oh, but I forgot,</p>
			<p begin="00:39:56:05" end="00:39:57:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">you don t have</p>
			<p begin="00:39:57:06" end="00:39:58:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">a career, sorry.</p>
			<p begin="00:39:58:14" end="00:39:59:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; We re keeping</p>
			<p begin="00:39:58:14" end="00:39:59:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	it real with you and</p>
			<p begin="00:39:59:23" end="00:40:01:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	that s the problem,</p>
			<p begin="00:39:59:23" end="00:40:01:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		you have a problem</p>
			<p begin="00:40:01:13" end="00:40:02:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			with the reality.</p>
			<p begin="00:40:02:14" end="00:40:03:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			&gt;&gt; You re hating.</p>
			<p begin="00:40:03:13" end="00:40:05:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; What the hell</p>
			<p begin="00:40:03:13" end="00:40:05:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			do I have to hate about,</p>
			<p begin="00:40:05:06" end="00:40:09:13" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			I haven t had any issues</p>
			<p begin="00:40:05:06" end="00:40:09:13" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			with my husband!</p>
			<p begin="00:40:11:21" end="00:40:14:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		Narrator:</p>
			<p begin="00:40:11:21" end="00:40:14:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	Coming up on</p>
			<p begin="00:40:14:02" end="00:40:15:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		Married to Medicine.</p>
			<p begin="00:40:15:11" end="00:40:17:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; How much is it</p>
			<p begin="00:40:15:11" end="00:40:17:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	going to take Quad!?</p>
			<p begin="00:40:17:23" end="00:40:19:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		&gt;&gt; What I am doing</p>
			<p begin="00:40:17:23" end="00:40:19:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			is preparing for</p>
			<p begin="00:40:19:07" end="00:40:25:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	life to come!</p>
			<p begin="00:40:26:23" end="00:40:28:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Toya: You have a problem</p>
			<p begin="00:40:26:23" end="00:40:28:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		with the reality.</p>
			<p begin="00:40:28:12" end="00:40:29:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			&gt;&gt; You re hating!</p>
			<p begin="00:40:29:11" end="00:40:31:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; What the hell</p>
			<p begin="00:40:29:11" end="00:40:31:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">			do I have to hate about?</p>
			<p begin="00:40:31:03" end="00:40:33:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			I haven t had any issues</p>
			<p begin="00:40:31:03" end="00:40:33:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			with my husband!</p>
			<p begin="00:40:33:06" end="00:40:39:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		We don t have any reasons</p>
			<p begin="00:40:33:06" end="00:40:39:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			to not even have</p>
			<p begin="00:40:39:03" end="00:40:40:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		sex and have a baby!</p>
			<p begin="00:40:40:19" end="00:40:42:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">There s nothing going</p>
			<p begin="00:40:40:19" end="00:40:42:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">			on here!</p>
			<p begin="00:40:42:19" end="00:40:45:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		If last year, someone was</p>
			<p begin="00:40:42:19" end="00:40:45:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	coming to me talking</p>
			<p begin="00:40:45:03" end="00:40:48:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	about my husband had</p>
			<p begin="00:40:45:03" end="00:40:48:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	screwed him or her,</p>
			<p begin="00:40:48:07" end="00:40:50:05" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	we would not</p>
			<p begin="00:40:48:07" end="00:40:50:05" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">		be having-</p>
			<p begin="00:40:50:06" end="00:40:51:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			Dr. Eugene: We would not</p>
			<p begin="00:40:50:06" end="00:40:51:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		be having a baby.</p>
			<p begin="00:40:51:22" end="00:40:52:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">&gt;&gt; Talks about</p>
			<p begin="00:40:51:22" end="00:40:52:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	a baby, no.</p>
			<p begin="00:40:52:17" end="00:40:54:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; We would be fixing</p>
			<p begin="00:40:52:17" end="00:40:54:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">our  marriage.</p>
			<p begin="00:40:54:23" end="00:40:55:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="36% 5.33%">	&gt;&gt; Thank you.</p>
			<p begin="00:40:55:21" end="00:40:58:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	You proclaimed to be</p>
			<p begin="00:40:55:21" end="00:40:58:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		Miss I work hard,</p>
			<p begin="00:40:58:12" end="00:40:59:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		I got this going on-</p>
			<p begin="00:40:59:15" end="00:41:00:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; And that means I cant</p>
			<p begin="00:40:59:15" end="00:41:00:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	have a baby because</p>
			<p begin="00:41:00:21" end="00:41:03:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	I have a career and</p>
			<p begin="00:41:00:21" end="00:41:03:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	lots of businesses?</p>
			<p begin="00:41:03:12" end="00:41:04:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">&gt;&gt; Not at all</p>
			<p begin="00:41:03:12" end="00:41:04:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="31% 5.33%">	not at all.</p>
			<p begin="00:41:04:08" end="00:41:05:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		Dr. Simone: Let me</p>
			<p begin="00:41:04:08" end="00:41:05:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		tell you something</p>
			<p begin="00:41:05:05" end="00:41:06:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		about Lisa honey,</p>
			<p begin="00:41:05:05" end="00:41:06:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		Lisa s going to do</p>
			<p begin="00:41:06:02" end="00:41:07:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		whatever the hell</p>
			<p begin="00:41:06:02" end="00:41:07:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		Lisa wants to do.</p>
			<p begin="00:41:07:15" end="00:41:09:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Quad: Well then why ya ll</p>
			<p begin="00:41:07:15" end="00:41:09:08" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">raising ya lls breath?</p>
			<p begin="00:41:09:08" end="00:41:11:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		&gt;&gt; This is what it s about</p>
			<p begin="00:41:09:08" end="00:41:11:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">and you-you be</p>
			<p begin="00:41:11:19" end="00:41:14:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">thankful that we don t</p>
			<p begin="00:41:11:19" end="00:41:14:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		get started on you</p>
			<p begin="00:41:14:12" end="00:41:16:03" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			about where you</p>
			<p begin="00:41:14:12" end="00:41:16:03" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		going to-</p>
			<p begin="00:41:16:04" end="00:41:18:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="46% 5.33%">			get started and</p>
			<p begin="00:41:16:04" end="00:41:18:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	have a baby!</p>
			<p begin="00:41:18:04" end="00:41:19:11" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">		Cecil: Everybody says zero</p>
			<p begin="00:41:18:04" end="00:41:19:11" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			to one hundred,</p>
			<p begin="00:41:19:12" end="00:41:21:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">		she goes from zero</p>
			<p begin="00:41:19:12" end="00:41:21:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			to one thousand,</p>
			<p begin="00:41:21:23" end="00:41:24:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	I mean this is what</p>
			<p begin="00:41:21:23" end="00:41:24:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="28% 5.33%">		she does.</p>
			<p begin="00:41:24:01" end="00:41:25:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			&gt;&gt; And you don t take it</p>
			<p begin="00:41:24:01" end="00:41:25:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			for granted that</p>
			<p begin="00:41:25:23" end="00:41:28:20" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			those eggs are going to</p>
			<p begin="00:41:25:23" end="00:41:28:20" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">be ready for Dr. Greg!</p>
			<p begin="00:41:28:20" end="00:41:30:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">&gt;&gt; Get ready,</p>
			<p begin="00:41:28:20" end="00:41:30:04" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">come through.</p>
			<p begin="00:41:30:05" end="00:41:33:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">&gt;&gt; Wake up Quad, Greg,</p>
			<p begin="00:41:30:05" end="00:41:33:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">[bleep] forty-</p>
			<p begin="00:41:33:16" end="00:41:35:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			eight years old,</p>
			<p begin="00:41:33:16" end="00:41:35:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		it s time to give</p>
			<p begin="00:41:35:23" end="00:41:37:08" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="41% 5.33%">that man a baby.</p>
			<p begin="00:41:37:08" end="00:41:39:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">&gt;&gt; I m not waiting on</p>
			<p begin="00:41:37:08" end="00:41:39:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		my husband to take</p>
			<p begin="00:41:39:08" end="00:41:40:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	care of us,</p>
			<p begin="00:41:39:08" end="00:41:40:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			mother is going</p>
			<p begin="00:41:40:17" end="00:41:42:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	to come through with</p>
			<p begin="00:41:40:17" end="00:41:42:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">contributions as well.</p>
			<p begin="00:41:42:13" end="00:41:44:12" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">&gt;&gt; Mother has</p>
			<p begin="00:41:42:13" end="00:41:44:12" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">contributions!</p>
			<p begin="00:41:44:13" end="00:41:46:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	You don t have to be</p>
			<p begin="00:41:44:13" end="00:41:46:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">a millionaire!</p>
			<p begin="00:41:46:17" end="00:41:49:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		You don t have to</p>
			<p begin="00:41:46:17" end="00:41:49:00" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		be a millionaire!</p>
			<p begin="00:41:49:01" end="00:41:49:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		&gt;&gt; But I need more!</p>
			<p begin="00:41:49:22" end="00:41:51:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; How much is it</p>
			<p begin="00:41:49:22" end="00:41:51:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">	going to take Quad!</p>
			<p begin="00:41:51:02" end="00:41:53:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="31% 5.33%">	&gt;&gt; Hold on,</p>
			<p begin="00:41:51:02" end="00:41:53:07" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			no let me talk.</p>
			<p begin="00:41:53:08" end="00:41:57:15" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; She s driving</p>
			<p begin="00:41:53:08" end="00:41:57:15" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">a Porch for god sake!</p>
			<p begin="00:41:57:16" end="00:41:58:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; Okay, and that s</p>
			<p begin="00:41:57:16" end="00:41:58:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		still not enough.</p>
			<p begin="00:41:58:22" end="00:42:00:23" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">			&gt;&gt; You re taking</p>
			<p begin="00:41:58:22" end="00:42:00:23" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		life for granted!</p>
			<p begin="00:42:01:00" end="00:42:03:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		&gt;&gt; I am not love,</p>
			<p begin="00:42:01:00" end="00:42:03:01" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		what I am doing is</p>
			<p begin="00:42:03:01" end="00:42:04:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">preparing for</p>
			<p begin="00:42:03:01" end="00:42:04:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">life to come.</p>
			<p begin="00:42:04:18" end="00:42:06:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">		Understand baby I m ready</p>
			<p begin="00:42:04:18" end="00:42:06:21" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="51% 5.33%">		to take your whole</p>
			<p begin="00:42:06:21" end="00:42:08:00" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			[bleep] face off!</p>
			<p begin="00:42:08:01" end="00:42:11:01" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		Get your life girl!</p>
			<p begin="00:42:11:01" end="00:42:12:07" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="38% 5.33%">Girl excuse me.</p>
			<p begin="00:42:12:08" end="00:42:13:04" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">		 You don t jump up,</p>
			<p begin="00:42:13:05" end="00:42:14:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">yelling and screaming</p>
			<p begin="00:42:13:05" end="00:42:14:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">			popping fingers,</p>
			<p begin="00:42:14:09" end="00:42:16:19" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="71% 5.33%">	talking about what I should</p>
			<p begin="00:42:14:09" end="00:42:16:19" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="56% 5.33%">be doing with my life!</p>
			<p begin="00:42:16:20" end="00:42:18:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="48% 5.33%">		I m just going to</p>
			<p begin="00:42:16:20" end="00:42:18:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">head on out the door.</p>
			<p begin="00:42:18:18" end="00:42:22:09" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	&gt;&gt; What the hell is</p>
			<p begin="00:42:18:18" end="00:42:22:09" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			she waiting on?</p>
			<p begin="00:42:26:02" end="00:42:26:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		Narrator:</p>
			<p begin="00:42:26:02" end="00:42:26:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">	Next time on</p>
			<p begin="00:42:26:22" end="00:42:28:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		Married to Medicine.</p>
			<p begin="00:42:28:02" end="00:42:29:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="76% 5.33%">Quad: What was all the yelling</p>
			<p begin="00:42:28:02" end="00:42:29:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">	and screaming about?</p>
			<p begin="00:42:29:18" end="00:42:35:02" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="78% 5.33%">Lisa Nicole: Toya, at the party</p>
			<p begin="00:42:29:18" end="00:42:35:02" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="53% 5.33%">she made the comment,</p>
			<p begin="00:42:35:02" end="00:42:36:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">	 You re not raising</p>
			<p begin="00:42:35:02" end="00:42:36:10" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			your own kids, </p>
			<p begin="00:42:36:10" end="00:42:39:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="68% 5.33%">			she s a little oblivious</p>
			<p begin="00:42:36:10" end="00:42:39:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="48% 5.33%">		to what she says.</p>
			<p begin="00:42:39:18" end="00:42:41:14" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="66% 5.33%">			Quad: I think I ve been</p>
			<p begin="00:42:39:18" end="00:42:41:14" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="33% 5.33%">compromising.</p>
			<p begin="00:42:41:14" end="00:42:42:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">	Dr. Gregory: You say</p>
			<p begin="00:42:41:14" end="00:42:42:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">you compromise</p>
			<p begin="00:42:42:18" end="00:42:46:22" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="53% 5.33%">but I don t feel that</p>
			<p begin="00:42:42:18" end="00:42:46:22" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">you always do.</p>
			<p begin="00:42:46:22" end="00:42:49:17" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="73% 5.33%">	Mariah: I really just wanted</p>
			<p begin="00:42:46:22" end="00:42:49:17" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="68% 5.33%">		to invite you to my home,</p>
			<p begin="00:42:49:18" end="00:42:53:16" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="33% 5.33%">	to know that</p>
			<p begin="00:42:49:18" end="00:42:53:16" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="46% 5.33%">			I love you all.</p>
			<p begin="00:42:55:03" end="00:42:55:18" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="28% 5.33%">		Narrator:</p>
			<p begin="00:42:55:03" end="00:42:55:18" region="pop2" style="basic" tts:origin="15% 83.66%" tts:extent="36% 5.33%">&gt;&gt; For more on</p>
			<p begin="00:42:55:18" end="00:42:56:10" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="56% 5.33%">		Married to Medicine,</p>
			<p begin="00:42:56:10" end="00:42:58:21" region="pop1" style="basic" tts:origin="15% 78.33%" tts:extent="51% 5.33%">			go to BravoTV.com</p>
		</div>
	</body>
</tt>
'''


converter = CaptionConverter()
converter.read(tt, DFXPReader())

print(converter.write(WebVTTWriter()))

