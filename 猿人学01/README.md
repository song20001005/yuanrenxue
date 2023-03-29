# pythonProject01
yuan01test
这是猿人学网站的第一题，这里的有个MD5加密,通过网页请求参数找到加密值m，明显是加密值|时间挫的格式  

这里有个无限debugger和防止格式化的反调试，通过调用栈堆或者xhr断点可以找到request栈里面有大量混淆的js代码，找到关键参数手动解混淆，在这部分使用以下hook代码找到生成加密的参数的位置。(注意这里的时间挫是经过处理的)将加密代码粘贴然后得到加密值可以正常访问网站

 Object.defineProperty(window, 'f', {
  set: function(val) {
      console.log('f的值:', val);
      debugger
      return val;
    }
  }
) 

