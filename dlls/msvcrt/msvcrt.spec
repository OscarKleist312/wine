# msvcrt.dll - MS VC++ Run Time Library

@ cdecl -norelay $I10_OUTPUT(double long long ptr) I10_OUTPUT
@ cdecl -arch=arm ??0__non_rtti_object@std@@QAA@ABV01@@Z(ptr ptr) __non_rtti_object_copy_ctor
@ thiscall -arch=i386 ??0__non_rtti_object@@QAE@ABV0@@Z(ptr ptr) __non_rtti_object_copy_ctor
@ cdecl -arch=win64 ??0__non_rtti_object@@QEAA@AEBV0@@Z(ptr ptr) __non_rtti_object_copy_ctor
@ cdecl -arch=arm ??0__non_rtti_object@std@@QAA@PBD@Z(ptr ptr) __non_rtti_object_ctor
@ thiscall -arch=i386 ??0__non_rtti_object@@QAE@PBD@Z(ptr ptr) __non_rtti_object_ctor
@ cdecl -arch=win64 ??0__non_rtti_object@@QEAA@PEBD@Z(ptr ptr) __non_rtti_object_ctor
@ cdecl -arch=arm ??0bad_cast@std@@AAA@PBQBD@Z(ptr ptr) bad_cast_ctor
@ thiscall -arch=i386 ??0bad_cast@@AAE@PBQBD@Z(ptr ptr) bad_cast_ctor
@ cdecl -arch=win64 ??0bad_cast@@AEAA@PEBQEBD@Z(ptr ptr) bad_cast_ctor
@ thiscall -arch=win32 ??0bad_cast@@QAE@ABQBD@Z(ptr ptr) bad_cast_ctor
@ cdecl -arch=win64 ??0bad_cast@@QEAA@AEBQEBD@Z(ptr ptr) bad_cast_ctor
@ cdecl -arch=arm ??0bad_cast@std@@QAA@ABV01@@Z(ptr ptr) bad_cast_ctor
@ thiscall -arch=i386 ??0bad_cast@@QAE@ABV0@@Z(ptr ptr) bad_cast_copy_ctor
@ cdecl -arch=win64 ??0bad_cast@@QEAA@AEBV0@@Z(ptr ptr) bad_cast_copy_ctor
@ cdecl -arch=arm ??0bad_cast@std@@QAA@PBD@Z(ptr str) bad_cast_ctor_charptr
@ thiscall -arch=i386 ??0bad_cast@@QAE@PBD@Z(ptr str) bad_cast_ctor_charptr
@ cdecl -arch=win64 ??0bad_cast@@QEAA@PEBD@Z(ptr str) bad_cast_ctor_charptr
@ cdecl -arch=arm ??0bad_typeid@std@@QAA@ABV01@@Z(ptr ptr) bad_typeid_copy_ctor
@ thiscall -arch=i386 ??0bad_typeid@@QAE@ABV0@@Z(ptr ptr) bad_typeid_copy_ctor
@ cdecl -arch=win64 ??0bad_typeid@@QEAA@AEBV0@@Z(ptr ptr) bad_typeid_copy_ctor
@ cdecl -arch=arm ??0bad_typeid@std@@QAA@PBD@Z(ptr str) bad_typeid_ctor
@ thiscall -arch=i386 ??0bad_typeid@@QAE@PBD@Z(ptr str) bad_typeid_ctor
@ cdecl -arch=win64 ??0bad_typeid@@QEAA@PEBD@Z(ptr str) bad_typeid_ctor
@ cdecl -arch=arm ??0exception@std@@QAA@ABQBD@Z(ptr ptr) exception_ctor
@ thiscall -arch=i386 ??0exception@@QAE@ABQBD@Z(ptr ptr) exception_ctor
@ cdecl -arch=win64 ??0exception@@QEAA@AEBQEBD@Z(ptr ptr) exception_ctor
@ cdecl -arch=arm ??0exception@std@@QAA@ABQBDH@Z(ptr ptr long) exception_ctor_noalloc
@ thiscall -arch=i386 ??0exception@@QAE@ABQBDH@Z(ptr ptr long) exception_ctor_noalloc
@ cdecl -arch=win64 ??0exception@@QEAA@AEBQEBDH@Z(ptr ptr long) exception_ctor_noalloc
@ cdecl -arch=arm ??0exception@std@@QAA@ABV01@@Z(ptr ptr) exception_copy_ctor
@ thiscall -arch=i386 ??0exception@@QAE@ABV0@@Z(ptr ptr) exception_copy_ctor
@ cdecl -arch=win64 ??0exception@@QEAA@AEBV0@@Z(ptr ptr) exception_copy_ctor
@ cdecl -arch=arm ??0exception@std@@QAA@XZ(ptr) exception_default_ctor
@ thiscall -arch=i386 ??0exception@@QAE@XZ(ptr) exception_default_ctor
@ cdecl -arch=win64 ??0exception@@QEAA@XZ(ptr) exception_default_ctor
@ cdecl -arch=arm ??1__non_rtti_object@std@@UAA@XZ(ptr) __non_rtti_object_dtor
@ thiscall -arch=i386 ??1__non_rtti_object@@UAE@XZ(ptr) __non_rtti_object_dtor
@ cdecl -arch=win64 ??1__non_rtti_object@@UEAA@XZ(ptr) __non_rtti_object_dtor
@ cdecl -arch=arm ??1bad_cast@std@@UAA@XZ(ptr) bad_cast_dtor
@ thiscall -arch=i386 ??1bad_cast@@UAE@XZ(ptr) bad_cast_dtor
@ cdecl -arch=win64 ??1bad_cast@@UEAA@XZ(ptr) bad_cast_dtor
@ cdecl -arch=arm ??1bad_typeid@std@@UAA@XZ(ptr) bad_typeid_dtor
@ thiscall -arch=i386 ??1bad_typeid@@UAE@XZ(ptr) bad_typeid_dtor
@ cdecl -arch=win64 ??1bad_typeid@@UEAA@XZ(ptr) bad_typeid_dtor
@ cdecl -arch=arm ??1exception@std@@UAA@XZ(ptr) exception_dtor
@ thiscall -arch=i386 ??1exception@@UAE@XZ(ptr) exception_dtor
@ cdecl -arch=win64 ??1exception@@UEAA@XZ(ptr) exception_dtor
@ cdecl -arch=arm ??1type_info@@UAA@XZ(ptr) type_info_dtor
@ thiscall -arch=i386 ??1type_info@@UAE@XZ(ptr) type_info_dtor
@ cdecl -arch=win64 ??1type_info@@UEAA@XZ(ptr) type_info_dtor
@ cdecl -arch=win32 ??2@YAPAXI@Z(long) operator_new
@ cdecl -arch=win64 ??2@YAPEAX_K@Z(long) operator_new
@ cdecl -arch=win32 ??2@YAPAXIHPBDH@Z(long long str long) operator_new_dbg
@ cdecl -arch=win64 ??2@YAPEAX_KHPEBDH@Z(long long str long) operator_new_dbg
@ cdecl -arch=win32 ??3@YAXPAX@Z(ptr) operator_delete
@ cdecl -arch=win64 ??3@YAXPEAX@Z(ptr) operator_delete
@ cdecl -arch=arm ??4__non_rtti_object@std@@QAAAAV01@ABV01@@Z(ptr ptr) __non_rtti_object_opequals
@ thiscall -arch=i386 ??4__non_rtti_object@@QAEAAV0@ABV0@@Z(ptr ptr) __non_rtti_object_opequals
@ cdecl -arch=win64 ??4__non_rtti_object@@QEAAAEAV0@AEBV0@@Z(ptr ptr) __non_rtti_object_opequals
@ cdecl -arch=arm ??4bad_cast@std@@QAAAAV01@ABV01@@Z(ptr ptr) bad_cast_opequals
@ thiscall -arch=i386 ??4bad_cast@@QAEAAV0@ABV0@@Z(ptr ptr) bad_cast_opequals
@ cdecl -arch=win64 ??4bad_cast@@QEAAAEAV0@AEBV0@@Z(ptr ptr) bad_cast_opequals
@ cdecl -arch=arm ??4bad_typeid@std@@QAAAAV01@ABV01@@Z(ptr ptr) bad_typeid_opequals
@ thiscall -arch=i386 ??4bad_typeid@@QAEAAV0@ABV0@@Z(ptr ptr) bad_typeid_opequals
@ cdecl -arch=win64 ??4bad_typeid@@QEAAAEAV0@AEBV0@@Z(ptr ptr) bad_typeid_opequals
@ cdecl -arch=arm ??4exception@std@@QAAAAV01@ABV01@@Z(ptr ptr) exception_opequals
@ thiscall -arch=i386 ??4exception@@QAEAAV0@ABV0@@Z(ptr ptr) exception_opequals
@ cdecl -arch=win64 ??4exception@@QEAAAEAV0@AEBV0@@Z(ptr ptr) exception_opequals
@ cdecl -arch=arm ??8type_info@@QBA_NABV0@@Z(ptr ptr) type_info_opequals_equals
@ thiscall -arch=i386 ??8type_info@@QBEHABV0@@Z(ptr ptr) type_info_opequals_equals
@ cdecl -arch=win64 ??8type_info@@QEBAHAEBV0@@Z(ptr ptr) type_info_opequals_equals
@ cdecl -arch=arm ??9type_info@@QBA_NABV0@@Z(ptr ptr) type_info_opnot_equals
@ thiscall -arch=i386 ??9type_info@@QBEHABV0@@Z(ptr ptr) type_info_opnot_equals
@ cdecl -arch=win64 ??9type_info@@QEBAHAEBV0@@Z(ptr ptr) type_info_opnot_equals
@ extern ??_7__non_rtti_object@@6B@ __non_rtti_object_vtable
@ extern ??_7bad_cast@@6B@ bad_cast_vtable
@ extern ??_7bad_typeid@@6B@ bad_typeid_vtable
@ extern ??_7exception@@6B@ exception_vtable
@ thiscall -arch=win32 ??_E__non_rtti_object@@UAEPAXI@Z(ptr long) __non_rtti_object_vector_dtor
@ thiscall -arch=win32 ??_Ebad_cast@@UAEPAXI@Z(ptr long) bad_cast_vector_dtor
@ thiscall -arch=win32 ??_Ebad_typeid@@UAEPAXI@Z(ptr long) bad_typeid_vector_dtor
@ thiscall -arch=win32 ??_Eexception@@UAEPAXI@Z(ptr long) exception_vector_dtor
@ cdecl -arch=arm ??_Fbad_cast@std@@QAAXXZ(ptr) bad_cast_default_ctor
@ thiscall -arch=i386 ??_Fbad_cast@@QAEXXZ(ptr) bad_cast_default_ctor
@ cdecl -arch=win64 ??_Fbad_cast@@QEAAXXZ(ptr) bad_cast_default_ctor
@ cdecl -arch=arm ??_Fbad_typeid@std@@QAAXXZ(ptr) bad_typeid_default_ctor
@ thiscall -arch=i386 ??_Fbad_typeid@@QAEXXZ(ptr) bad_typeid_default_ctor
@ cdecl -arch=win64 ??_Fbad_typeid@@QEAAXXZ(ptr) bad_typeid_default_ctor
@ thiscall -arch=win32 ??_G__non_rtti_object@@UAEPAXI@Z(ptr long) __non_rtti_object_scalar_dtor
@ thiscall -arch=win32 ??_Gbad_cast@@UAEPAXI@Z(ptr long) bad_cast_scalar_dtor
@ thiscall -arch=win32 ??_Gbad_typeid@@UAEPAXI@Z(ptr long) bad_typeid_scalar_dtor
@ thiscall -arch=win32 ??_Gexception@@UAEPAXI@Z(ptr long) exception_scalar_dtor
@ cdecl -arch=win32 ??_U@YAPAXI@Z(long) operator_new
@ cdecl -arch=win64 ??_U@YAPEAX_K@Z(long) operator_new
@ cdecl -arch=win32 ??_U@YAPAXIHPBDH@Z(long long str long) operator_new_dbg
@ cdecl -arch=win64 ??_U@YAPEAX_KHPEBDH@Z(long long str long) operator_new_dbg
@ cdecl -arch=win32 ??_V@YAXPAX@Z(ptr) operator_delete
@ cdecl -arch=win64 ??_V@YAXPEAX@Z(ptr) operator_delete
@ cdecl -arch=win32 ?_query_new_handler@@YAP6AHI@ZXZ() _query_new_handler
@ cdecl -arch=win64 ?_query_new_handler@@YAP6AH_K@ZXZ() _query_new_handler
@ cdecl ?_query_new_mode@@YAHXZ() _query_new_mode
@ cdecl -arch=win32 ?_set_new_handler@@YAP6AHI@ZP6AHI@Z@Z(ptr) _set_new_handler
@ cdecl -arch=win64 ?_set_new_handler@@YAP6AH_K@ZP6AH0@Z@Z(ptr) _set_new_handler
@ cdecl ?_set_new_mode@@YAHH@Z(long) _set_new_mode
@ cdecl -arch=win32 ?_set_se_translator@@YAP6AXIPAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z(ptr) _set_se_translator
@ cdecl -arch=win64 ?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z(ptr) _set_se_translator
@ cdecl -arch=arm ?before@type_info@@QBA_NABV1@@Z(ptr ptr) type_info_before
@ thiscall -arch=i386 ?before@type_info@@QBEHABV1@@Z(ptr ptr) type_info_before
@ cdecl -arch=win64 ?before@type_info@@QEBAHAEBV1@@Z(ptr ptr) type_info_before
@ thiscall -arch=win32 ?name@type_info@@QBEPBDXZ(ptr) type_info_name
@ cdecl -arch=win64 ?name@type_info@@QEBAPEBDXZ(ptr) type_info_name
@ cdecl -arch=arm ?raw_name@type_info@@QBAPBDXZ(ptr) type_info_raw_name
@ thiscall -arch=i386 ?raw_name@type_info@@QBEPBDXZ(ptr) type_info_raw_name
@ cdecl -arch=win64 ?raw_name@type_info@@QEBAPEBDXZ(ptr) type_info_raw_name
@ cdecl ?set_new_handler@@YAP6AXXZP6AXXZ@Z(ptr) set_new_handler
@ cdecl ?set_terminate@@YAP6AXXZP6AXXZ@Z(ptr) set_terminate
@ cdecl ?set_unexpected@@YAP6AXXZP6AXXZ@Z(ptr) set_unexpected
@ cdecl ?terminate@@YAXXZ() terminate
@ cdecl ?unexpected@@YAXXZ() unexpected
@ cdecl -arch=arm ?what@exception@std@@UBAPBDXZ(ptr) what_exception
@ thiscall -arch=i386 ?what@exception@@UBEPBDXZ(ptr) what_exception
@ cdecl -arch=win64 ?what@exception@@UEBAPEBDXZ(ptr) what_exception
@ cdecl -arch=i386 _CIacos()
@ cdecl -arch=i386 _CIasin()
@ cdecl -arch=i386 _CIatan()
@ cdecl -arch=i386 _CIatan2()
@ cdecl -arch=i386 _CIcos()
@ cdecl -arch=i386 _CIcosh()
@ cdecl -arch=i386 _CIexp()
@ cdecl -arch=i386 _CIfmod()
@ cdecl -arch=i386 _CIlog()
@ cdecl -arch=i386 _CIlog10()
@ cdecl -arch=i386 _CIpow()
@ cdecl -arch=i386 _CIsin()
@ cdecl -arch=i386 _CIsinh()
@ cdecl -arch=i386 _CIsqrt()
@ cdecl -arch=i386 _CItan()
@ cdecl -arch=i386 _CItanh()
# stub _CrtCheckMemory
# stub _CrtDbgBreak
# stub _CrtDbgReport
# stub _CrtDbgReportV
# stub _CrtDbgReportW
# stub _CrtDbgReportWV
# stub _CrtDoForAllClientObjects
# stub _CrtDumpMemoryLeaks
# stub _CrtIsMemoryBlock
# stub _CrtIsValidHeapPointer
# stub _CrtIsValidPointer
# stub _CrtMemCheckpoint
# stub _CrtMemDifference
# stub _CrtMemDumpAllObjectsSince
# stub _CrtMemDumpStatistics
# stub _CrtReportBlockType
# stub _CrtSetAllocHook
# stub _CrtSetBreakAlloc
# stub _CrtSetDbgBlockType
# stub _CrtSetDbgFlag
# stub _CrtSetDumpClient
# stub _CrtSetReportFile
# stub _CrtSetReportHook
# stub _CrtSetReportHook2
# stub _CrtSetReportMode
@ stdcall _CxxThrowException(ptr ptr)
@ cdecl -arch=i386 -norelay _EH_prolog()
@ cdecl _Getdays()
@ cdecl _Getmonths()
@ cdecl _Gettnames()
@ extern _HUGE MSVCRT__HUGE
@ cdecl _Strftime(ptr long str ptr ptr)
@ cdecl _XcptFilter(long ptr)
@ stdcall -arch=x86_64,arm64 __C_specific_handler(ptr long ptr ptr) ntdll.__C_specific_handler
@ cdecl -arch=i386,x86_64,arm,arm64 __CppXcptFilter(long ptr)
# stub __CxxCallUnwindDelDtor
# stub __CxxCallUnwindDtor
# stub __CxxCallUnwindVecDtor
@ cdecl -arch=i386,x86_64,arm,arm64 __CxxDetectRethrow(ptr)
@ cdecl -arch=i386,x86_64,arm,arm64 __CxxExceptionFilter(ptr ptr long ptr)
@ cdecl -arch=i386,x86_64,arm,arm64 -norelay __CxxFrameHandler(ptr ptr ptr ptr)
@ cdecl -arch=i386,x86_64,arm,arm64 -norelay __CxxFrameHandler2(ptr ptr ptr ptr) __CxxFrameHandler
@ cdecl -arch=i386,x86_64,arm,arm64 -norelay __CxxFrameHandler3(ptr ptr ptr ptr) __CxxFrameHandler
@ stdcall -arch=i386 __CxxLongjmpUnwind(ptr)
@ cdecl -arch=i386,x86_64,arm,arm64 __CxxQueryExceptionSize()
@ cdecl __CxxRegisterExceptionObject(ptr ptr)
@ cdecl __CxxUnregisterExceptionObject(ptr long)
@ cdecl __DestructExceptionObject(ptr)
@ cdecl __RTCastToVoid(ptr)
@ cdecl __RTDynamicCast(ptr long ptr ptr long)
@ cdecl __RTtypeid(ptr)
@ cdecl __STRINGTOLD(ptr ptr str long)
@ cdecl ___lc_codepage_func()
@ cdecl ___lc_collate_cp_func()
@ cdecl ___lc_handle_func()
@ cdecl ___mb_cur_max_func()
@ cdecl ___setlc_active_func()
@ cdecl ___unguarded_readlc_active_add_func()
@ extern __argc MSVCRT___argc
@ extern __argv MSVCRT___argv
@ extern __badioinfo MSVCRT___badioinfo
@ cdecl __crtCompareStringA(long long str long str long)
@ cdecl __crtCompareStringW(long long wstr long wstr long)
@ cdecl __crtGetLocaleInfoW(long long ptr long)
@ cdecl __crtGetStringTypeW(long long wstr long ptr)
@ cdecl __crtLCMapStringA(long long str long ptr long long long)
@ cdecl __crtLCMapStringW(long long wstr long ptr long long long)
@ cdecl __daylight() __p__daylight
@ cdecl __dllonexit(ptr ptr ptr)
@ cdecl __doserrno()
@ cdecl __dstbias() __p__dstbias
@ cdecl __fpecode()
@ stub __get_app_type
@ cdecl __getmainargs(ptr ptr ptr long ptr)
@ extern __initenv MSVCRT___initenv
@ cdecl __iob_func()
@ cdecl __isascii(long)
@ cdecl __iscsym(long)
@ cdecl __iscsymf(long)
@ extern __lc_codepage MSVCRT___lc_codepage
@ stub __lc_collate
@ extern __lc_collate_cp MSVCRT___lc_collate_cp
@ extern __lc_handle MSVCRT___lc_handle
@ cdecl __lconv_init()
@ cdecl -arch=i386 -norelay __libm_sse2_acos()
@ cdecl -arch=i386 -norelay __libm_sse2_acosf()
@ cdecl -arch=i386 -norelay __libm_sse2_asin()
@ cdecl -arch=i386 -norelay __libm_sse2_asinf()
@ cdecl -arch=i386 -norelay __libm_sse2_atan()
@ cdecl -arch=i386 -norelay __libm_sse2_atan2()
@ cdecl -arch=i386 -norelay __libm_sse2_atanf()
@ cdecl -arch=i386 -norelay __libm_sse2_cos()
@ cdecl -arch=i386 -norelay __libm_sse2_cosf()
@ cdecl -arch=i386 -norelay __libm_sse2_exp()
@ cdecl -arch=i386 -norelay __libm_sse2_expf()
@ cdecl -arch=i386 -norelay __libm_sse2_log()
@ cdecl -arch=i386 -norelay __libm_sse2_log10()
@ cdecl -arch=i386 -norelay __libm_sse2_log10f()
@ cdecl -arch=i386 -norelay __libm_sse2_logf()
@ cdecl -arch=i386 -norelay __libm_sse2_pow()
@ cdecl -arch=i386 -norelay __libm_sse2_powf()
@ cdecl -arch=i386 -norelay __libm_sse2_sin()
@ cdecl -arch=i386 -norelay __libm_sse2_sinf()
@ cdecl -arch=i386 -norelay __libm_sse2_tan()
@ cdecl -arch=i386 -norelay __libm_sse2_tanf()
@ extern __mb_cur_max MSVCRT___mb_cur_max
@ cdecl -arch=i386 __p___argc()
@ cdecl -arch=i386 __p___argv()
@ cdecl -arch=i386 __p___initenv()
@ cdecl -arch=i386 __p___mb_cur_max()
@ cdecl -arch=i386 __p___wargv()
@ cdecl -arch=i386 __p___winitenv()
@ cdecl -arch=i386 __p__acmdln()
@ cdecl -arch=i386 __p__amblksiz()
@ cdecl -arch=i386 __p__commode()
@ cdecl -arch=i386 __p__daylight()
@ cdecl -arch=i386 __p__dstbias()
@ cdecl -arch=i386 __p__environ()
@ stub -arch=i386 __p__fileinfo()
@ cdecl -arch=i386 __p__fmode()
@ cdecl -arch=i386 __p__iob() __iob_func
@ stub -arch=i386 __p__mbcasemap()
@ cdecl -arch=i386 __p__mbctype()
@ cdecl -arch=i386 __p__osver()
@ cdecl -arch=i386 __p__pctype()
@ cdecl -arch=i386 __p__pgmptr()
@ stub -arch=i386 __p__pwctype()
@ cdecl -arch=i386 __p__timezone()
@ cdecl -arch=i386 __p__tzname()
@ cdecl -arch=i386 __p__wcmdln()
@ cdecl -arch=i386 __p__wenviron()
@ cdecl -arch=i386 __p__winmajor()
@ cdecl -arch=i386 __p__winminor()
@ cdecl -arch=i386 __p__winver()
@ cdecl -arch=i386 __p__wpgmptr()
@ cdecl __pctype_func()
@ extern __pioinfo MSVCRT___pioinfo
# stub __pwctype_func()
@ cdecl __pxcptinfoptrs()
@ cdecl __set_app_type(long)
@ extern __setlc_active MSVCRT___setlc_active
@ cdecl __setusermatherr(ptr)
@ cdecl __strncnt(str long)
@ cdecl __threadhandle() kernel32.GetCurrentThread
@ cdecl __threadid() kernel32.GetCurrentThreadId
@ cdecl __toascii(long)
@ cdecl __uncaught_exception()
@ cdecl __unDName(ptr str long ptr ptr long)
@ cdecl __unDNameEx(ptr str long ptr ptr ptr long)
@ extern __unguarded_readlc_active MSVCRT___unguarded_readlc_active
@ extern __wargv MSVCRT___wargv
@ cdecl __wcserror(wstr)
@ cdecl __wcserror_s(ptr long wstr)
# stub __wcsncnt(wstr long)
@ cdecl __wgetmainargs(ptr ptr ptr long ptr)
@ extern __winitenv MSVCRT___winitenv
@ cdecl _abnormal_termination()
@ cdecl -ret64 _abs64(int64)
@ cdecl _access(str long) MSVCRT__access
@ cdecl _access_s(str long) MSVCRT__access_s
@ extern _acmdln MSVCRT__acmdln
@ stdcall -arch=i386 _adj_fdiv_m16i(long)
@ stdcall -arch=i386 _adj_fdiv_m32(long)
@ stdcall -arch=i386 _adj_fdiv_m32i(long)
@ stdcall -arch=i386 _adj_fdiv_m64(int64)
@ cdecl -arch=i386 _adj_fdiv_r()
@ stdcall -arch=i386 _adj_fdivr_m16i(long)
@ stdcall -arch=i386 _adj_fdivr_m32(long)
@ stdcall -arch=i386 _adj_fdivr_m32i(long)
@ stdcall -arch=i386 _adj_fdivr_m64(int64)
@ cdecl -arch=i386 _adj_fpatan()
@ cdecl -arch=i386 _adj_fprem()
@ cdecl -arch=i386 _adj_fprem1()
@ cdecl -arch=i386 _adj_fptan()
@ extern -arch=i386 _adjust_fdiv MSVCRT__adjust_fdiv
@ extern _aexit_rtn
@ cdecl _aligned_free(ptr)
# stub _aligned_free_dbg(ptr)
@ cdecl _aligned_malloc(long long)
# stub _aligned_malloc_dbg(long long str long)
@ cdecl _aligned_offset_malloc(long long long)
# stub _aligned_offset_malloc_dbg(long long long str long)
@ cdecl _aligned_offset_realloc(ptr long long long)
# stub _aligned_offset_realloc_dbg(ptr long long long str long)
@ cdecl _aligned_realloc(ptr long long)
# stub _aligned_realloc_dbg(ptr long long str long)
@ cdecl _amsg_exit(long)
@ cdecl _assert(str str long)
@ cdecl _atodbl(ptr str)
@ cdecl _atodbl_l(ptr str ptr)
@ cdecl _atof_l(str ptr)
@ cdecl _atoflt_l(ptr str ptr)
@ cdecl -ret64 _atoi64(str)
@ cdecl -ret64 _atoi64_l(str ptr)
@ cdecl _atoi_l(str ptr)
@ cdecl _atol_l(str ptr)
@ cdecl _atoldbl(ptr str)
@ cdecl _atoldbl_l(ptr str ptr)
@ cdecl _beep(long long)
@ cdecl _beginthread (ptr long ptr)
@ cdecl _beginthreadex (ptr long ptr ptr long ptr)
@ cdecl _c_exit()
@ cdecl _cabs(long)
@ cdecl _callnewh(long)
# stub _calloc_dbg(long long long str long)
@ cdecl _cexit()
@ cdecl _cgets(ptr)
# stub _cgets_s(ptr long ptr)
# stub _cgetws(ptr)
# stub _cgetws_s(ptr long ptr)
@ cdecl _chdir(str)
@ cdecl _chdrive(long)
@ cdecl _chgsign(double)
@ cdecl -arch=!i386 _chgsignf(float)
@ cdecl -arch=i386 -norelay _chkesp()
@ cdecl _chmod(str long) MSVCRT__chmod
@ cdecl _chsize(long long) MSVCRT__chsize
@ cdecl _chsize_s(long int64) MSVCRT__chsize_s
# stub _chvalidator(long long)
# stub _chvalidator_l(ptr long long)
@ cdecl _clearfp()
@ cdecl _close(long) MSVCRT__close
@ cdecl _commit(long) MSVCRT__commit
@ extern _commode MSVCRT__commode
@ cdecl _control87(long long)
@ cdecl _controlfp(long long)
@ cdecl _controlfp_s(ptr long long)
@ cdecl _copysign(double double)
@ cdecl -arch=!i386 _copysignf(float float)
@ varargs _cprintf(str)
# stub _cprintf_l(str ptr)
# stub _cprintf_p(str)
# stub _cprintf_p_l(str ptr)
# stub _cprintf_s(str)
# stub _cprintf_s_l(str ptr)
@ cdecl _cputs(str)
@ cdecl _cputws(wstr)
@ cdecl _creat(str long) MSVCRT__creat
@ cdecl _create_locale(long str)
# stub _crtAssertBusy
# stub _crtBreakAlloc
# stub _crtDbgFlag
@ varargs _cscanf(str)
@ varargs _cscanf_l(str ptr)
@ varargs _cscanf_s(str)
@ varargs _cscanf_s_l(str ptr)
@ cdecl _ctime32(ptr)
@ cdecl _ctime32_s(str long ptr)
@ cdecl _ctime64(ptr)
@ cdecl _ctime64_s(str long ptr)
@ extern _ctype MSVCRT__ctype
@ cdecl _cwait(ptr long long)
@ varargs _cwprintf(wstr)
# stub _cwprintf_l(wstr ptr)
# stub _cwprintf_p(wstr)
# stub _cwprintf_p_l(wstr ptr)
# stub _cwprintf_s(wstr)
# stub _cwprintf_s_l(wstr ptr)
@ varargs _cwscanf(wstr)
@ varargs _cwscanf_l(wstr ptr)
@ varargs _cwscanf_s(wstr)
@ varargs _cwscanf_s_l(wstr ptr)
@ extern _daylight MSVCRT___daylight
@ cdecl _difftime32(long long)
@ cdecl _difftime64(int64 int64)
@ extern _dstbias MSVCRT__dstbias
@ cdecl _dup (long) MSVCRT__dup
@ cdecl _dup2 (long long) MSVCRT__dup2
@ cdecl _ecvt(double long ptr ptr)
@ cdecl _ecvt_s(str long double long ptr ptr)
@ cdecl _endthread ()
@ cdecl _endthreadex(long)
@ extern _environ MSVCRT__environ
@ cdecl _eof(long) MSVCRT__eof
@ cdecl _errno()
@ cdecl -arch=i386 _except_handler2(ptr ptr ptr ptr)
@ cdecl -arch=i386 _except_handler3(ptr ptr ptr ptr)
@ cdecl -arch=i386 _except_handler4_common(ptr ptr ptr ptr ptr ptr)
@ varargs _execl(str str)
@ varargs _execle(str str)
@ varargs _execlp(str str)
@ varargs _execlpe(str str)
@ cdecl _execv(str ptr)
@ cdecl _execve(str ptr ptr)
@ cdecl _execvp(str ptr)
@ cdecl _execvpe(str ptr ptr)
@ cdecl _exit(long)
@ cdecl _expand(ptr long)
# stub _expand_dbg(ptr long long str long)
@ cdecl _fcloseall() MSVCRT__fcloseall
@ cdecl _fcvt(double long ptr ptr)
@ cdecl _fcvt_s(ptr long double long ptr ptr)
@ cdecl _fdopen(long str) MSVCRT__fdopen
@ cdecl _fgetchar() MSVCRT__fgetchar
@ cdecl _fgetwchar() MSVCRT__fgetwchar
@ cdecl _filbuf(ptr) MSVCRT__filbuf
# extern _fileinfo
@ cdecl _filelength(long) MSVCRT__filelength
@ cdecl -ret64 _filelengthi64(long) MSVCRT__filelengthi64
@ cdecl _fileno(ptr) MSVCRT__fileno
@ cdecl _findclose(long)
@ cdecl _findfirst(str ptr)
@ cdecl _findfirst32(str ptr)
@ cdecl _findfirst64(str ptr)
@ cdecl _findfirst64i32(str ptr)
@ cdecl _findfirsti64(str ptr)
@ cdecl _findnext(long ptr)
@ cdecl _findnext32(long ptr)
@ cdecl _findnext64(long ptr)
@ cdecl _findnext64i32(long ptr)
@ cdecl _findnexti64(long ptr)
@ cdecl _finite(double)
@ cdecl -arch=!i386 _finitef(float)
@ cdecl _flsbuf(long ptr) MSVCRT__flsbuf
@ cdecl _flushall() MSVCRT__flushall
@ extern _fmode MSVCRT__fmode
@ cdecl _fpclass(double)
@ cdecl -arch=!i386 _fpclassf(float)
@ cdecl -arch=i386,x86_64,arm,arm64 _fpieee_flt(long ptr ptr)
@ cdecl _fpreset()
# stub _fprintf_l(ptr str ptr)
# stub _fprintf_p(ptr str)
# stub _fprintf_p_l(ptr str ptr)
# stub _fprintf_s_l(ptr str ptr)
@ cdecl _fputchar(long) MSVCRT__fputchar
@ cdecl _fputwchar(long) MSVCRT__fputwchar
# stub _free_dbg(ptr long)
@ cdecl _free_locale(ptr)
# stub _freea(ptr)
# stub _freea_s
@ varargs _fscanf_l(ptr str ptr)
@ varargs _fscanf_s_l(ptr str ptr)
@ cdecl _fseeki64(ptr int64 long) MSVCRT__fseeki64
@ cdecl _fsopen(str str long) MSVCRT__fsopen
@ cdecl _fstat(long ptr) MSVCRT__fstat
@ cdecl _fstat64(long ptr) MSVCRT__fstat64
@ cdecl _fstati64(long ptr) MSVCRT__fstati64
@ cdecl -ret64 _ftelli64(ptr) MSVCRT__ftelli64
@ cdecl -arch=win32 _ftime(ptr) _ftime32
@ cdecl -arch=win64 _ftime(ptr) _ftime64
@ cdecl _ftime32(ptr)
@ cdecl _ftime32_s(ptr)
@ cdecl _ftime64(ptr)
@ cdecl _ftime64_s(ptr)
@ cdecl -arch=i386 -ret64 _ftol()
@ cdecl -arch=i386 -ret64 _ftol2() _ftol
@ cdecl -arch=i386 -ret64 _ftol2_sse() _ftol #FIXME: SSE variant should be implemented
# stub _ftol2_sse_excpt
@ cdecl _fullpath(ptr str long)
# stub _fullpath_dbg(ptr str long long str long)
@ cdecl -arch=win32 _futime(long ptr) _futime32
@ cdecl -arch=win64 _futime(long ptr) _futime64
@ cdecl _futime32(long ptr)
@ cdecl _futime64(long ptr)
@ varargs _fwprintf_l(ptr wstr ptr) MSVCRT__fwprintf_l
# stub _fwprintf_p(ptr wstr)
# stub _fwprintf_p_l(ptr wstr ptr)
# stub _fwprintf_s_l(ptr wstr ptr)
@ varargs _fwscanf_l(ptr wstr ptr)
@ varargs _fwscanf_s_l(ptr wstr ptr)
@ cdecl _gcvt(double long str)
@ cdecl _gcvt_s(ptr long  double long)
@ cdecl _get_current_locale()
@ cdecl _get_doserrno(ptr)
@ cdecl _get_environ(ptr)
@ cdecl _get_errno(ptr)
# stub _get_fileinfo(ptr)
@ cdecl _get_fmode(ptr)
@ cdecl _get_heap_handle()
@ cdecl _get_osfhandle(long) MSVCRT__get_osfhandle
@ cdecl _get_osplatform(ptr)
@ cdecl _get_osver(ptr)
@ cdecl _get_output_format()
@ cdecl _get_pgmptr(ptr)
@ cdecl _get_sbh_threshold()
@ cdecl _get_wenviron(ptr)
@ cdecl _get_winmajor(ptr)
@ cdecl _get_winminor(ptr)
# stub _get_winver(ptr)
@ cdecl _get_wpgmptr(ptr)
@ cdecl _get_terminate()
@ cdecl _get_tzname(ptr str long long)
@ cdecl _get_unexpected()
@ cdecl _getch()
@ cdecl _getche()
@ cdecl _getcwd(str long)
@ cdecl _getdcwd(long str long)
@ cdecl _getdiskfree(long ptr)
@ cdecl _getdllprocaddr(long str long)
@ cdecl _getdrive()
@ cdecl _getdrives() kernel32.GetLogicalDrives
@ cdecl _getmaxstdio() MSVCRT__getmaxstdio
@ cdecl _getmbcp()
@ cdecl _getpid() _getpid
@ stub _getsystime(ptr)
@ cdecl _getw(ptr) MSVCRT__getw
@ cdecl _getwch()
@ cdecl _getwche()
@ cdecl _getws(ptr) MSVCRT__getws
@ cdecl -arch=i386 _global_unwind2(ptr)
@ cdecl _gmtime32(ptr)
@ cdecl _gmtime32_s(ptr ptr)
@ cdecl _gmtime64(ptr)
@ cdecl _gmtime64_s(ptr ptr)
@ cdecl _heapadd (ptr long)
@ cdecl _heapchk()
@ cdecl _heapmin()
@ cdecl _heapset(long)
@ stub _heapused(ptr ptr)
@ cdecl _heapwalk(ptr)
@ cdecl _hypot(double double)
@ cdecl _hypotf(float float)
@ cdecl _i64toa(int64 ptr long) ntdll._i64toa
@ cdecl _i64toa_s(int64 ptr long long)
@ cdecl _i64tow(int64 ptr long) ntdll._i64tow
@ cdecl _i64tow_s(int64 ptr long long)
@ cdecl _initterm(ptr ptr)
@ cdecl _initterm_e(ptr ptr)
@ stub -arch=i386 _inp(long)
@ stub -arch=i386 _inpd(long)
@ stub -arch=i386 _inpw(long)
@ cdecl _invalid_parameter(wstr wstr wstr long long)
@ extern _iob MSVCRT__iob
@ cdecl _isalnum_l(long ptr)
@ cdecl _isalpha_l(long ptr)
@ cdecl _isatty(long) MSVCRT__isatty
@ cdecl _iscntrl_l(long ptr)
@ cdecl _isctype(long long)
@ cdecl _isctype_l(long long ptr)
@ cdecl _isdigit_l(long ptr)
@ cdecl _isgraph_l(long ptr)
@ cdecl _isleadbyte_l(long ptr)
@ cdecl _islower_l(long ptr)
@ stub _ismbbalnum(long)
# stub _ismbbalnum_l(long ptr)
@ stub _ismbbalpha(long)
# stub _ismbbalpha_l(long ptr)
@ stub _ismbbgraph(long)
# stub _ismbbgraph_l(long ptr)
@ stub _ismbbkalnum(long)
# stub _ismbbkalnum_l(long ptr)
@ cdecl _ismbbkana(long)
@ cdecl _ismbbkana_l(long ptr)
@ stub _ismbbkprint(long)
# stub _ismbbkprint_l(long ptr)
@ stub _ismbbkpunct(long)
# stub _ismbbkpunct_l(long ptr)
@ cdecl _ismbblead(long)
@ cdecl _ismbblead_l(long ptr)
@ stub _ismbbprint(long)
# stub _ismbbprint_l(long ptr)
@ stub _ismbbpunct(long)
# stub _ismbbpunct_l(long ptr)
@ cdecl _ismbbtrail(long)
@ cdecl _ismbbtrail_l(long ptr)
@ cdecl _ismbcalnum(long)
@ cdecl _ismbcalnum_l(long ptr)
@ cdecl _ismbcalpha(long)
@ cdecl _ismbcalpha_l(long ptr)
@ cdecl _ismbcdigit(long)
@ cdecl _ismbcdigit_l(long ptr)
@ cdecl _ismbcgraph(long)
@ cdecl _ismbcgraph_l(long ptr)
@ cdecl _ismbchira(long)
# stub _ismbchira_l(long ptr)
@ cdecl _ismbckata(long)
# stub _ismbckata_l(long ptr)
@ cdecl _ismbcl0(long)
@ cdecl _ismbcl0_l(long ptr)
@ cdecl _ismbcl1(long)
@ cdecl _ismbcl1_l(long ptr)
@ cdecl _ismbcl2(long)
@ cdecl _ismbcl2_l(long ptr)
@ cdecl _ismbclegal(long)
@ cdecl _ismbclegal_l(long ptr)
@ cdecl _ismbclower(long)
@ cdecl _ismbclower_l(long ptr)
@ cdecl _ismbcprint(long)
@ cdecl _ismbcprint_l(long ptr)
@ cdecl _ismbcpunct(long)
@ cdecl _ismbcpunct_l(long ptr)
@ cdecl _ismbcspace(long)
@ cdecl _ismbcspace_l(long ptr)
@ cdecl _ismbcsymbol(long)
# stub _ismbcsymbol_l(long ptr)
@ cdecl _ismbcupper(long)
@ cdecl _ismbcupper_l(long ptr)
@ cdecl _ismbslead(ptr ptr)
# stub _ismbslead_l(long ptr)
@ cdecl _ismbstrail(ptr ptr)
# stub _ismbstrail_l(long ptr)
@ cdecl _isnan(double)
@ cdecl -arch=x86_64 _isnanf(float)
@ cdecl _isprint_l(long ptr)
@ cdecl _isspace_l(long ptr)
@ cdecl _isupper_l(long ptr)
@ cdecl _iswalnum_l(long ptr)
@ cdecl _iswalpha_l(long ptr)
@ cdecl _iswcntrl_l(long ptr)
@ cdecl _iswctype_l(long long ptr)
@ cdecl _iswdigit_l(long ptr)
@ cdecl _iswgraph_l(long ptr)
@ cdecl _iswlower_l(long ptr)
@ cdecl _iswprint_l(long ptr)
@ cdecl _iswpunct_l(long ptr)
@ cdecl _iswspace_l(long ptr)
@ cdecl _iswupper_l(long ptr)
@ cdecl _iswxdigit_l(long ptr)
@ cdecl _isxdigit_l(long ptr)
@ cdecl _itoa(long ptr long)
@ cdecl _itoa_s(long ptr long long)
@ cdecl _itow(long ptr long) ntdll._itow
@ cdecl _itow_s(long ptr long long)
@ cdecl _j0(double)
@ cdecl _j1(double)
@ cdecl _jn(long double)
@ cdecl _kbhit()
@ cdecl _lfind(ptr ptr ptr long ptr)
@ cdecl _lfind_s(ptr ptr ptr long ptr ptr)
@ cdecl _loaddll(str)
@ cdecl -arch=x86_64 _local_unwind(ptr ptr)
@ cdecl -arch=i386 _local_unwind2(ptr long)
@ cdecl -arch=i386 _local_unwind4(ptr ptr long)
@ cdecl _localtime32(ptr)
@ cdecl _localtime32_s(ptr ptr)
@ cdecl _localtime64(ptr)
@ cdecl _localtime64_s(ptr ptr)
@ cdecl _lock(long)
@ cdecl _lock_file(ptr) MSVCRT__lock_file
@ cdecl _locking(long long long) MSVCRT__locking
@ cdecl _logb(double)
@ cdecl -arch=!i386 _logbf(float)
@ cdecl -arch=i386 _longjmpex(ptr long) MSVCRT_longjmp
@ cdecl _lrotl(long long)
@ cdecl _lrotr(long long)
@ cdecl _lsearch(ptr ptr ptr long ptr)
# stub _lsearch_s(ptr ptr ptr long ptr ptr)
@ cdecl _lseek(long long long) MSVCRT__lseek
@ cdecl -ret64 _lseeki64(long int64 long) MSVCRT__lseeki64
@ cdecl _ltoa(long ptr long) ntdll._ltoa
@ cdecl _ltoa_s(long ptr long long)
@ cdecl _ltow(long ptr long) ntdll._ltow
@ cdecl _ltow_s(long ptr long long)
@ cdecl _makepath(ptr str str str str)
@ cdecl _makepath_s(ptr long str str str str)
# stub _malloc_dbg(long long str long)
@ cdecl _mbbtombc(long)
# stub _mbbtombc_l(long ptr)
@ cdecl _mbbtype(long long)
# extern _mbcasemap
@ cdecl _mbccpy(ptr ptr)
@ cdecl _mbccpy_l(ptr ptr ptr)
@ cdecl _mbccpy_s(ptr long ptr ptr)
@ cdecl _mbccpy_s_l(ptr long ptr ptr ptr)
@ cdecl _mbcjistojms (long)
# stub _mbcjistojms_l(long ptr)
@ cdecl _mbcjmstojis(long)
# stub _mbcjmstojis_l(long ptr)
@ cdecl _mbclen(ptr)
# stub _mbclen_l(ptr ptr)
@ cdecl _mbctohira(long)
# stub _mbctohira_l(long ptr)
@ cdecl _mbctokata(long)
# stub _mbctokata_l(long ptr)
@ cdecl _mbctolower(long)
# stub _mbctolower_l(long ptr)
@ cdecl _mbctombb(long)
# stub _mbctombb_l(long ptr)
@ cdecl _mbctoupper(long)
# stub _mbctoupper_l(long ptr)
@ extern _mbctype MSVCRT_mbctype
# stub _mblen_l(str long ptr)
@ cdecl _mbsbtype(str long)
# stub _mbsbtype_l(str long ptr)
@ cdecl _mbscat(str str)
@ cdecl _mbscat_s(ptr long str)
@ cdecl _mbscat_s_l(ptr long str ptr)
@ cdecl _mbschr(str long)
# stub _mbschr_l(str long ptr)
@ cdecl _mbscmp(str str)
@ cdecl _mbscmp_l(str str ptr)
@ cdecl _mbscoll(str str)
@ cdecl _mbscoll_l(str str ptr)
@ cdecl _mbscpy(ptr str)
@ cdecl _mbscpy_s(ptr long str)
@ cdecl _mbscpy_s_l(ptr long str ptr)
@ cdecl _mbscspn(str str)
@ cdecl _mbscspn_l(str str ptr)
@ cdecl _mbsdec(ptr ptr)
# stub _mbsdec_l(ptr ptr ptr)
@ cdecl _mbsdup(str) _strdup
# stub _strdup_dbg(str long str long)
@ cdecl _mbsicmp(str str)
# stub _mbsicmp_l(str str ptr)
@ cdecl _mbsicoll(str str)
@ cdecl _mbsicoll_l(str str ptr)
@ cdecl _mbsinc(str)
# stub _mbsinc_l(str ptr)
@ cdecl _mbslen(str)
@ cdecl _mbslen_l(str ptr)
@ cdecl _mbslwr(str)
# stub _mbslwr_l(str ptr)
@ cdecl _mbslwr_s(str long)
# stub _mbslwr_s_l(str long ptr)
@ cdecl _mbsnbcat(str str long)
# stub _mbsnbcat_l(str str long ptr)
@ cdecl _mbsnbcat_s(str long ptr long)
# stub _mbsnbcat_s_l(str long ptr long ptr)
@ cdecl _mbsnbcmp(str str long)
# stub _mbsnbcmp_l(str str long ptr)
@ cdecl _mbsnbcnt(ptr long)
# stub _mbsnbcnt_l(ptr long ptr)
@ cdecl _mbsnbcoll(str str long)
@ cdecl _mbsnbcoll_l(str str long ptr)
@ cdecl _mbsnbcpy(ptr str long)
# stub _mbsnbcpy_l(ptr str long ptr)
@ cdecl _mbsnbcpy_s(ptr long str long)
@ cdecl _mbsnbcpy_s_l(ptr long str long ptr)
@ cdecl _mbsnbicmp(str str long)
# stub _mbsnbicmp_l(str str long ptr)
@ cdecl _mbsnbicoll(str str long)
@ cdecl _mbsnbicoll_l(str str long ptr)
@ cdecl _mbsnbset(ptr long long)
# stub _mbsnbset_l(str long long ptr)
# stub _mbsnbset_s(ptr long long long)
# stub _mbsnbset_s_l(ptr long long long ptr)
@ cdecl _mbsncat(str str long)
# stub _mbsncat_l(str str long ptr)
# stub _mbsncat_s(str long str long)
# stub _mbsncat_s_l(str long str long ptr)
@ cdecl _mbsnccnt(str long)
# stub _mbsnccnt_l(str long ptr)
@ cdecl _mbsncmp(str str long)
# stub _mbsncmp_l(str str long ptr)
@ stub _mbsncoll(str str long)
# stub _mbsncoll_l(str str long ptr)
@ cdecl _mbsncpy(ptr str long)
# stub _mbsncpy_l(ptr str long ptr)
# stub _mbsncpy_s(ptr long str long)
# stub _mbsncpy_s_l(ptr long str long ptr)
@ cdecl _mbsnextc(str)
@ cdecl _mbsnextc_l(str ptr)
@ cdecl _mbsnicmp(str str long)
# stub _mbsnicmp_l(str str long ptr)
@ stub _mbsnicoll(str str long)
# stub _mbsnicoll_l(str str long ptr)
@ cdecl _mbsninc(str long)
# stub _mbsninc_l(str long ptr)
@ cdecl _mbsnlen(str long)
@ cdecl _mbsnlen_l(str long ptr)
@ cdecl _mbsnset(ptr long long)
# stub _mbsnset_l(ptr long long ptr)
# stub _mbsnset_s(ptr long long long)
# stub _mbsnset_s_l(ptr long long long ptr)
@ cdecl _mbspbrk(str str)
# stub _mbspbrk_l(str str ptr)
@ cdecl _mbsrchr(str long)
# stub _mbsrchr_l(str long ptr)
@ cdecl _mbsrev(str)
# stub _mbsrev_l(str ptr)
@ cdecl _mbsset(ptr long)
# stub _mbsset_l(ptr long ptr)
# stub _mbsset_s(ptr long long)
# stub _mbsset_s_l(ptr long long ptr)
@ cdecl _mbsspn(str str)
@ cdecl _mbsspn_l(str str ptr)
@ cdecl _mbsspnp(str str)
# stub _mbsspnp_l(str str ptr)
@ cdecl _mbsstr(str str)
# stub _mbsstr_l(str str ptr)
@ cdecl _mbstok(str str)
@ cdecl _mbstok_l(str str ptr)
@ cdecl _mbstok_s(str str ptr)
@ cdecl _mbstok_s_l(str str ptr ptr)
@ cdecl _mbstowcs_l(ptr str long ptr)
@ cdecl _mbstowcs_s_l(ptr ptr long str long ptr)
@ cdecl _mbstrlen(str)
@ cdecl _mbstrlen_l(str ptr)
# stub _mbstrnlen(str long)
# stub _mbstrnlen_l(str long ptr)
@ cdecl _mbsupr(str)
# stub _mbsupr_l(str ptr)
@ cdecl _mbsupr_s(str long)
# stub _mbsupr_s_l(str long ptr)
@ cdecl _mbtowc_l(ptr str long ptr)
@ cdecl _memccpy(ptr ptr long long) ntdll._memccpy
@ cdecl _memicmp(str str long)
@ cdecl _memicmp_l(str str long ptr)
@ cdecl _mkdir(str)
@ cdecl -arch=win32 _mkgmtime(ptr) _mkgmtime32
@ cdecl -arch=win64 _mkgmtime(ptr) _mkgmtime64
@ cdecl _mkgmtime32(ptr)
@ cdecl _mkgmtime64(ptr)
@ cdecl _mktemp(str) MSVCRT__mktemp
@ cdecl _mktemp_s(str long) MSVCRT__mktemp_s
@ cdecl _mktime32(ptr)
@ cdecl _mktime64(ptr)
@ cdecl _msize(ptr)
# stub -arch=win32 _msize_debug(ptr long)
# stub -arch=win64 _msize_dbg(ptr long)
@ cdecl _nextafter(double double)
@ cdecl -arch=x86_64 _nextafterf(float float)
@ cdecl _onexit(ptr)
@ varargs _open(str long) MSVCRT__open
@ cdecl _open_osfhandle(long long) MSVCRT__open_osfhandle
@ extern _osplatform MSVCRT__osplatform
@ extern _osver MSVCRT__osver
@ stub -arch=i386 _outp(long long)
@ stub -arch=i386 _outpd(long long)
@ stub -arch=i386 _outpw(long long)
@ cdecl _pclose (ptr) _pclose
@ extern _pctype MSVCRT__pctype
@ extern _pgmptr MSVCRT__pgmptr
@ cdecl _pipe (ptr long long) MSVCRT__pipe
@ cdecl _popen (str str) _popen
# stub _printf_l(str ptr)
# stub _printf_p(str)
# stub _printf_p_l(str ptr)
# stub _printf_s_l(str ptr)
@ cdecl _purecall()
@ cdecl _putch(long)
@ cdecl _putenv(str)
@ cdecl _putenv_s(str str)
@ cdecl _putw(long ptr) MSVCRT__putw
@ cdecl _putwch(long)
@ cdecl _putws(wstr) MSVCRT__putws
@ extern _pwctype MSVCRT__pwctype
@ cdecl _read(long ptr long) MSVCRT__read
# stub _realloc_dbg(ptr long long str long)
@ cdecl _resetstkoflw()
@ cdecl _rmdir(str)
@ cdecl _rmtmp() MSVCRT__rmtmp
@ cdecl _rotl(long long)
@ cdecl -ret64 _rotl64(int64 long)
@ cdecl _rotr(long long)
@ cdecl -ret64 _rotr64(int64 long)
@ cdecl -arch=i386 _safe_fdiv()
@ cdecl -arch=i386 _safe_fdivr()
@ cdecl -arch=i386 _safe_fprem()
@ cdecl -arch=i386 _safe_fprem1()
@ cdecl _scalb(double long)
@ cdecl -arch=x86_64 _scalbf(float long)
@ varargs _scanf_l(str ptr)
@ varargs _scanf_s_l(str ptr)
@ varargs _scprintf(str)
# stub _scprintf_l(str ptr)
# stub _scprintf_p_l(str ptr)
@ varargs _scwprintf(wstr)
# stub _scwprintf_l(wstr ptr)
# stub _scwprintf_p_l(wstr ptr)
@ cdecl _searchenv(str str ptr)
@ cdecl _searchenv_s(str str ptr long)
@ stdcall -arch=i386 _seh_longjmp_unwind4(ptr)
@ stdcall -arch=i386 _seh_longjmp_unwind(ptr)
@ cdecl _set_SSE2_enable(long)
@ cdecl _set_controlfp(long long)
@ cdecl _set_doserrno(long)
@ cdecl _set_errno(long)
@ cdecl _set_error_mode(long)
# stub _set_fileinfo(long)
@ cdecl _set_fmode(long)
@ cdecl _set_output_format(long)
@ cdecl _set_sbh_threshold(long)
@ cdecl _seterrormode(long)
@ cdecl -arch=i386,x86_64,arm,arm64 -norelay _setjmp(ptr) MSVCRT__setjmp
@ cdecl -arch=i386 -norelay _setjmp3(ptr long) MSVCRT__setjmp3
@ cdecl -arch=x86_64,arm,arm64 -norelay _setjmpex(ptr ptr) __wine_setjmpex
@ cdecl _setmaxstdio(long) MSVCRT__setmaxstdio
@ cdecl _setmbcp(long)
@ cdecl _setmode(long long) MSVCRT__setmode
@ stub _setsystime(ptr long)
@ cdecl _sleep(long)
@ varargs _snprintf(ptr long str)
@ varargs _snprintf_c(ptr long str)
@ varargs _snprintf_c_l(ptr long str ptr)
@ varargs _snprintf_l(ptr long str ptr)
@ varargs _snprintf_s(ptr long long str)
@ varargs _snprintf_s_l(ptr long long str ptr)
@ varargs _snscanf(str long str)
@ varargs _snscanf_l(str long str ptr)
@ varargs _snscanf_s(str long str)
@ varargs _snscanf_s_l(str long str ptr)
@ varargs _snwprintf(ptr long wstr)
@ varargs _snwprintf_l(ptr long wstr ptr)
@ varargs _snwprintf_s(ptr long long wstr)
@ varargs _snwprintf_s_l(ptr long long wstr ptr)
@ varargs _snwscanf(wstr long wstr)
@ varargs _snwscanf_l(wstr long wstr ptr)
@ varargs _snwscanf_s(wstr long wstr)
@ varargs _snwscanf_s_l(wstr long wstr ptr)
@ varargs _sopen(str long long) MSVCRT__sopen
@ cdecl _sopen_s(ptr str long long long) MSVCRT__sopen_s
@ varargs _spawnl(long str str)
@ varargs _spawnle(long str str)
@ varargs _spawnlp(long str str)
@ varargs _spawnlpe(long str str)
@ cdecl _spawnv(long str ptr)
@ cdecl _spawnve(long str ptr ptr)
@ cdecl _spawnvp(long str ptr)
@ cdecl _spawnvpe(long str ptr ptr)
@ cdecl _splitpath(str ptr ptr ptr ptr)
@ cdecl _splitpath_s(str ptr long ptr long ptr long ptr long)
@ varargs _sprintf_l(ptr str ptr)
@ varargs _sprintf_p_l(ptr long str ptr)
@ varargs _sprintf_s_l(ptr long str ptr)
@ varargs _sscanf_l(str str ptr)
@ varargs _sscanf_s_l(str str ptr)
@ cdecl _stat(str ptr) MSVCRT_stat
@ cdecl _stat64(str ptr) MSVCRT_stat64
@ cdecl _stati64(str ptr) MSVCRT_stati64
@ cdecl _statusfp()
@ cdecl _strcmpi(str str) _stricmp
@ cdecl _strcoll_l(str str ptr)
@ cdecl _strdate(ptr)
@ cdecl _strdate_s(ptr long)
@ cdecl _strdup(str)
# stub _strdup_dbg(str long str long)
@ cdecl _strerror(long)
# stub _strerror_s(ptr long long)
@ cdecl _stricmp(str str)
@ cdecl _stricmp_l(str str ptr)
@ cdecl _stricoll(str str)
@ cdecl _stricoll_l(str str ptr)
@ cdecl _strlwr(str)
@ cdecl _strlwr_l(str ptr)
@ cdecl _strlwr_s(ptr long)
@ cdecl _strlwr_s_l(ptr long ptr)
@ cdecl _strncoll(str str long)
@ cdecl _strncoll_l(str str long ptr)
@ cdecl _strnicmp(str str long)
@ cdecl _strnicmp_l(str str long ptr)
@ cdecl _strnicoll(str str long)
@ cdecl _strnicoll_l(str str long ptr)
@ cdecl _strnset(str long long)
@ cdecl _strnset_s(str long long long)
@ cdecl _strrev(str)
@ cdecl _strset(str long)
# stub _strset_s(str long long)
@ cdecl _strtime(ptr)
@ cdecl _strtime_s(ptr long)
@ cdecl _strtod_l(str ptr ptr)
@ cdecl -ret64 _strtoi64(str ptr long)
@ cdecl -ret64 _strtoi64_l(str ptr long ptr)
@ cdecl _strtol_l(str ptr long ptr)
@ cdecl -ret64 _strtoui64(str ptr long)
@ cdecl -ret64 _strtoui64_l(str ptr long ptr)
@ cdecl _strtoul_l(str ptr long ptr)
@ cdecl _strupr(str)
@ cdecl _strupr_l(str ptr)
@ cdecl _strupr_s(str long)
@ cdecl _strupr_s_l(str long ptr)
@ cdecl _strxfrm_l(ptr str long ptr)
@ cdecl _swab(str str long)
@ varargs _swprintf(ptr wstr)
@ varargs _swprintf_c(ptr long str)
@ varargs _swprintf_c_l(ptr long str ptr)
@ varargs _swprintf_p_l(ptr long wstr ptr)
@ varargs _swprintf_s_l(ptr long wstr ptr)
@ varargs _swscanf_l(wstr wstr ptr)
@ varargs _swscanf_s_l(wstr wstr ptr)
@ extern _sys_errlist MSVCRT__sys_errlist
@ extern _sys_nerr MSVCRT__sys_nerr
@ cdecl _tell(long) MSVCRT__tell
@ cdecl -ret64 _telli64(long)
@ cdecl _tempnam(str str) MSVCRT__tempnam
# stub _tempnam_dbg(str str long str long)
@ cdecl _time32(ptr)
@ cdecl _time64(ptr)
@ extern _timezone MSVCRT___timezone
@ cdecl _tolower(long)
@ cdecl _tolower_l(long ptr)
@ cdecl _toupper(long)
@ cdecl _toupper_l(long ptr)
@ cdecl _towlower_l(long ptr)
@ cdecl _towupper_l(long ptr)
@ extern _tzname MSVCRT__tzname
@ cdecl _tzset()
@ cdecl _ui64toa(int64 ptr long) ntdll._ui64toa
@ cdecl _ui64toa_s(int64 ptr long long)
@ cdecl _ui64tow(int64 ptr long) ntdll._ui64tow
@ cdecl _ui64tow_s(int64 ptr long long)
@ cdecl _ultoa(long ptr long) ntdll._ultoa
@ cdecl _ultoa_s(long ptr long long)
@ cdecl _ultow(long ptr long) ntdll._ultow
@ cdecl _ultow_s(long ptr long long)
@ cdecl _umask(long) MSVCRT__umask
# stub _umask_s(long ptr)
@ cdecl _ungetch(long)
@ cdecl _ungetwch(long)
@ cdecl _unlink(str) MSVCRT__unlink
@ cdecl _unloaddll(long)
@ cdecl _unlock(long)
@ cdecl _unlock_file(ptr) MSVCRT__unlock_file
@ cdecl _utime32(str ptr)
@ cdecl _utime64(str ptr)
@ cdecl _vcprintf(str ptr)
# stub _vcprintf_l(str ptr ptr)
# stub _vcprintf_p(str ptr)
# stub _vcprintf_p_l(str ptr ptr)
# stub _vcprintf_s(str ptr)
# stub _vcprintf_s_l(str ptr ptr)
@ cdecl _vcwprintf(wstr ptr)
# stub _vcwprintf_l(wstr ptr ptr)
# stub _vcwprintf_p(wstr ptr)
# stub _vcwprintf_p_l(wstr ptr ptr)
# stub _vcwprintf_s(wstr ptr)
# stub _vcwprintf_s_l(wstr ptr ptr)
@ cdecl _vfprintf_l(ptr str ptr ptr) MSVCRT__vfprintf_l
@ cdecl _vfprintf_p(ptr str ptr) MSVCRT__vfprintf_p
@ cdecl _vfprintf_p_l(ptr str ptr ptr) MSVCRT__vfprintf_p_l
@ cdecl _vfprintf_s_l(ptr str ptr ptr) MSVCRT__vfprintf_s_l
@ cdecl _vfwprintf_l(ptr wstr ptr ptr) MSVCRT__vfwprintf_l
@ cdecl _vfwprintf_p(ptr wstr ptr) MSVCRT__vfwprintf_p
@ cdecl _vfwprintf_p_l(ptr wstr ptr ptr) MSVCRT__vfwprintf_p_l
@ cdecl _vfwprintf_s_l(ptr wstr ptr ptr) MSVCRT__vfwprintf_s_l
# stub _vprintf_l(str ptr ptr)
# stub _vprintf_p(str ptr)
# stub _vprintf_p_l(str ptr ptr)
# stub _vprintf_s_l(str ptr ptr)
@ cdecl -arch=win32 _utime(str ptr) _utime32
@ cdecl -arch=win64 _utime(str ptr) _utime64
@ cdecl _vscprintf(str ptr)
@ cdecl _vscprintf_l(str ptr ptr)
@ cdecl _vscprintf_p_l(str ptr ptr)
@ cdecl _vscwprintf(wstr ptr)
@ cdecl _vscwprintf_l(wstr ptr ptr)
@ cdecl _vscwprintf_p_l(wstr ptr ptr)
@ cdecl -norelay _vsnprintf(ptr long str ptr)
@ cdecl _vsnprintf_c(ptr long str ptr)
@ cdecl _vsnprintf_c_l(ptr long str ptr ptr)
@ cdecl _vsnprintf_l(ptr long str ptr ptr)
@ cdecl _vsnprintf_s(ptr long long str ptr)
@ cdecl _vsnprintf_s_l(ptr long long str ptr ptr)
@ cdecl _vsnwprintf(ptr long wstr ptr)
@ cdecl _vsnwprintf_l(ptr long wstr ptr ptr)
@ cdecl _vsnwprintf_s(ptr long long wstr ptr)
@ cdecl _vsnwprintf_s_l(ptr long long wstr ptr ptr)
@ cdecl _vsprintf_l(ptr str ptr ptr)
@ cdecl _vsprintf_p(ptr long str ptr)
@ cdecl _vsprintf_p_l(ptr long str ptr ptr)
@ cdecl _vsprintf_s_l(ptr long str ptr ptr)
@ cdecl _vswprintf(ptr wstr ptr)
@ cdecl _vswprintf_c(ptr long wstr ptr)
@ cdecl _vswprintf_c_l(ptr long wstr ptr ptr)
@ cdecl _vswprintf_l(ptr wstr ptr ptr)
@ cdecl _vswprintf_p_l(ptr long wstr ptr ptr)
@ cdecl _vswprintf_s_l(ptr long wstr ptr ptr)
# stub _vwprintf_l(wstr ptr ptr)
# stub _vwprintf_p(wstr ptr)
# stub _vwprintf_p_l(wstr ptr ptr)
# stub _vwprintf_s_l(wstr ptr ptr)
@ cdecl _waccess(wstr long) MSVCRT__waccess
@ cdecl _waccess_s(wstr long) MSVCRT__waccess_s
@ cdecl _wasctime(ptr)
@ cdecl _wasctime_s(ptr long ptr)
@ cdecl _wassert(wstr wstr long)
@ cdecl _wchdir(wstr)
@ cdecl _wchmod(wstr long) MSVCRT__wchmod
@ extern _wcmdln MSVCRT__wcmdln
@ cdecl _wcreat(wstr long) MSVCRT__wcreat
@ cdecl _wcscoll_l(wstr wstr ptr)
@ cdecl _wcsdup(wstr)
# stub _wcsdup_dbg(wstr long str long)
@ cdecl _wcserror(long)
@ cdecl _wcserror_s(ptr long long)
@ cdecl _wcsftime_l(ptr long wstr ptr ptr)
@ cdecl _wcsicmp(wstr wstr)
@ cdecl _wcsicmp_l(wstr wstr ptr)
@ cdecl _wcsicoll(wstr wstr)
@ cdecl _wcsicoll_l(wstr wstr ptr)
@ cdecl _wcslwr(wstr)
@ cdecl _wcslwr_l(wstr ptr)
@ cdecl _wcslwr_s(wstr long)
@ cdecl _wcslwr_s_l(wstr long ptr)
@ cdecl _wcsncoll(wstr wstr long)
@ cdecl _wcsncoll_l(wstr wstr long ptr)
@ cdecl _wcsnicmp(wstr wstr long)
@ cdecl _wcsnicmp_l(wstr wstr long ptr)
@ cdecl _wcsnicoll(wstr wstr long)
@ cdecl _wcsnicoll_l(wstr wstr long ptr)
@ cdecl _wcsnset(wstr long long)
@ cdecl _wcsnset_s(wstr long long long)
@ cdecl _wcsrev(wstr)
@ cdecl _wcsset(wstr long)
@ cdecl _wcsset_s(wstr long long)
@ cdecl _wcstod_l(wstr ptr ptr)
@ cdecl -ret64 _wcstoi64(wstr ptr long)
@ cdecl -ret64 _wcstoi64_l(wstr ptr long ptr)
@ cdecl _wcstol_l(wstr ptr long ptr)
@ cdecl _wcstombs_l(ptr ptr long ptr)
@ cdecl _wcstombs_s_l(ptr ptr long wstr long ptr)
@ cdecl -ret64 _wcstoui64(wstr ptr long)
@ cdecl -ret64 _wcstoui64_l(wstr ptr long ptr)
@ cdecl _wcstoul_l(wstr ptr long ptr)
@ cdecl _wcsupr(wstr)
@ cdecl _wcsupr_l(wstr ptr)
@ cdecl _wcsupr_s(wstr long)
@ cdecl _wcsupr_s_l(wstr long ptr)
@ cdecl _wcsxfrm_l(ptr wstr long ptr)
@ cdecl -arch=win32 _wctime(ptr) _wctime32
@ cdecl -arch=win64 _wctime(ptr) _wctime64
@ cdecl _wctime32(ptr)
@ cdecl _wctime32_s(ptr long ptr)
@ cdecl _wctime64(ptr)
@ cdecl _wctime64_s(ptr long ptr)
@ cdecl _wctomb_l(ptr long ptr)
@ cdecl _wctomb_s_l(ptr ptr long long ptr)
@ extern _wctype MSVCRT__wctype
@ extern _wenviron MSVCRT__wenviron
@ varargs _wexecl(wstr wstr)
@ varargs _wexecle(wstr wstr)
@ varargs _wexeclp(wstr wstr)
@ varargs _wexeclpe(wstr wstr)
@ cdecl _wexecv(wstr ptr)
@ cdecl _wexecve(wstr ptr ptr)
@ cdecl _wexecvp(wstr ptr)
@ cdecl _wexecvpe(wstr ptr ptr)
@ cdecl _wfdopen(long wstr) MSVCRT__wfdopen
@ cdecl _wfindfirst(wstr ptr)
@ cdecl _wfindfirst32(wstr ptr)
@ cdecl _wfindfirst64(wstr ptr)
@ cdecl _wfindfirsti64(wstr ptr)
@ cdecl _wfindfirst64i32(wstr ptr)
@ cdecl _wfindnext(long ptr)
@ cdecl _wfindnext64(long ptr)
@ cdecl _wfindnext64i32(long ptr)
@ cdecl _wfindnexti64(long ptr)
@ cdecl _wfopen(wstr wstr) MSVCRT__wfopen
@ cdecl _wfopen_s(ptr wstr wstr) MSVCRT__wfopen_s
@ cdecl _wfreopen(wstr wstr ptr) MSVCRT__wfreopen
@ cdecl _wfreopen_s(ptr wstr wstr ptr) MSVCRT__wfreopen_s
@ cdecl _wfsopen(wstr wstr long) MSVCRT__wfsopen
@ cdecl _wfullpath(ptr wstr long)
# stub _wfullpath_dbg(ptr wstr long long str long)
@ cdecl _wgetcwd(wstr long)
@ cdecl _wgetdcwd(long wstr long)
@ cdecl _wgetenv(wstr)
@ cdecl _wgetenv_s(ptr ptr long wstr)
@ extern _winmajor MSVCRT__winmajor
@ extern _winminor MSVCRT__winminor
# stub _winput_s
@ extern _winver MSVCRT__winver
@ cdecl _wmakepath(ptr wstr wstr wstr wstr)
@ cdecl _wmakepath_s(ptr long wstr wstr wstr wstr)
@ cdecl _wmkdir(wstr)
@ cdecl _wmktemp(wstr) MSVCRT__wmktemp
@ cdecl _wmktemp_s(wstr long) MSVCRT__wmktemp_s
@ varargs _wopen(wstr long) MSVCRT__wopen
# stub _woutput_s
@ cdecl _wperror(wstr)
@ extern _wpgmptr MSVCRT__wpgmptr
@ cdecl _wpopen (wstr wstr) _wpopen
# stub _wprintf_l(wstr ptr)
# stub _wprintf_p(wstr)
# stub _wprintf_p_l(wstr ptr)
# stub _wprintf_s_l(wstr ptr)
@ cdecl _wputenv(wstr)
@ cdecl _wputenv_s(wstr wstr)
@ cdecl _wremove(wstr) MSVCRT__wremove
@ cdecl _wrename(wstr wstr) MSVCRT__wrename
@ cdecl _write(long ptr long) MSVCRT__write
@ cdecl _wrmdir(wstr)
@ varargs _wscanf_l(wstr ptr)
@ varargs _wscanf_s_l(wstr ptr)
@ cdecl _wsearchenv(wstr wstr ptr)
@ cdecl _wsearchenv_s(wstr wstr ptr long)
@ cdecl _wsetlocale(long wstr)
@ varargs _wsopen(wstr long long) MSVCRT__wsopen
@ cdecl _wsopen_s(ptr wstr long long long) MSVCRT__wsopen_s
@ varargs _wspawnl(long wstr wstr)
@ varargs _wspawnle(long wstr wstr)
@ varargs _wspawnlp(long wstr wstr)
@ varargs _wspawnlpe(long wstr wstr)
@ cdecl _wspawnv(long wstr ptr)
@ cdecl _wspawnve(long wstr ptr ptr)
@ cdecl _wspawnvp(long wstr ptr)
@ cdecl _wspawnvpe(long wstr ptr ptr)
@ cdecl _wsplitpath(wstr ptr ptr ptr ptr)
@ cdecl _wsplitpath_s(wstr ptr long ptr long ptr long ptr long)
@ cdecl _wstat(wstr ptr) MSVCRT__wstat
@ cdecl _wstati64(wstr ptr) MSVCRT__wstati64
@ cdecl _wstat64(wstr ptr) MSVCRT__wstat64
@ cdecl _wstrdate(ptr)
@ cdecl _wstrdate_s(ptr long)
@ cdecl _wstrtime(ptr)
@ cdecl _wstrtime_s(ptr long)
@ cdecl _wsystem(wstr)
@ cdecl _wtempnam(wstr wstr) MSVCRT__wtempnam
# stub _wtempnam_dbg(wstr wstr long str long)
@ cdecl _wtmpnam(ptr) MSVCRT__wtmpnam
@ cdecl _wtmpnam_s(ptr long) MSVCRT__wtmpnam_s
@ cdecl _wtof(wstr)
@ cdecl _wtof_l(wstr ptr)
@ cdecl _wtoi(wstr)
@ cdecl -ret64 _wtoi64(wstr)
@ cdecl -ret64 _wtoi64_l(wstr ptr)
@ cdecl _wtoi_l(wstr ptr)
@ cdecl _wtol(wstr)
@ cdecl _wtol_l(wstr ptr)
@ cdecl _wunlink(wstr) MSVCRT__wunlink
@ cdecl -arch=win32 _wutime(wstr ptr) _wutime32
@ cdecl -arch=win64 _wutime(wstr ptr) _wutime64
@ cdecl _wutime32(wstr ptr)
@ cdecl _wutime64(wstr ptr)
@ cdecl _y0(double)
@ cdecl _y1(double)
@ cdecl _yn(long double)
@ cdecl abort()
@ cdecl abs(long)
@ cdecl acos(double)
@ cdecl -arch=!i386 acosf(float)
@ cdecl asctime(ptr)
@ cdecl asctime_s(ptr long ptr)
@ cdecl asin(double)
@ cdecl atan(double)
@ cdecl atan2(double double)
@ cdecl -arch=!i386 asinf(float)
@ cdecl -arch=!i386 atanf(float)
@ cdecl -arch=!i386 atan2f(float float)
@ cdecl -private atexit(ptr) MSVCRT_atexit  # not imported to avoid conflicts with Mingw
@ cdecl atof(str)
@ cdecl atoi(str)
@ cdecl atol(str)
@ cdecl bsearch(ptr ptr long long ptr)
@ cdecl bsearch_s(ptr ptr long long ptr ptr)
@ cdecl btowc(long)
@ cdecl calloc(long long)
@ cdecl ceil(double)
@ cdecl -arch=!i386 ceilf(float)
@ cdecl clearerr(ptr) MSVCRT_clearerr
@ cdecl clearerr_s(ptr) MSVCRT_clearerr_s
@ cdecl clock()
@ cdecl cos(double)
@ cdecl cosh(double)
@ cdecl -arch=!i386 cosf(float)
@ cdecl -arch=!i386 coshf(float)
@ cdecl -arch=win32 ctime(ptr) _ctime32
@ cdecl -arch=win64 ctime(ptr) _ctime64
@ cdecl -arch=win32 difftime(long long) _difftime32
@ cdecl -arch=win64 difftime(long long) _difftime64
@ cdecl -ret64 div(long long)
@ cdecl exit(long)
@ cdecl exp(double)
@ cdecl -arch=!i386 expf(float)
@ cdecl fabs(double)
@ cdecl -arch=!i386 fabsf(float)
@ cdecl fclose(ptr) MSVCRT_fclose
@ cdecl feof(ptr) MSVCRT_feof
@ cdecl ferror(ptr) MSVCRT_ferror
@ cdecl fflush(ptr) MSVCRT_fflush
@ cdecl fgetc(ptr) MSVCRT_fgetc
@ cdecl fgetpos(ptr ptr) MSVCRT_fgetpos
@ cdecl fgets(ptr long ptr) MSVCRT_fgets
@ cdecl fgetwc(ptr) MSVCRT_fgetwc
@ cdecl fgetws(ptr long ptr) MSVCRT_fgetws
@ cdecl floor(double)
@ cdecl -arch=!i386 floorf(float)
@ cdecl fma(double double double)
@ cdecl -arch=!i386 fmaf(float float float)
@ cdecl fmod(double double)
@ cdecl -arch=!i386 fmodf(float float)
@ cdecl fopen(str str) MSVCRT_fopen
@ cdecl fopen_s(ptr str str) MSVCRT_fopen_s
@ varargs fprintf(ptr str) MSVCRT_fprintf
@ varargs fprintf_s(ptr str) MSVCRT_fprintf_s
@ cdecl fputc(long ptr) MSVCRT_fputc
@ cdecl fputs(str ptr) MSVCRT_fputs
@ cdecl fputwc(long ptr) MSVCRT_fputwc
@ cdecl fputws(wstr ptr) MSVCRT_fputws
@ cdecl fread(ptr long long ptr) MSVCRT_fread
@ cdecl free(ptr)
@ cdecl freopen(str str ptr) MSVCRT_freopen
@ cdecl freopen_s(ptr str str ptr) MSVCRT_freopen_s
@ cdecl frexp(double ptr)
@ cdecl -arch=x86_64 frexpf(float ptr)
@ varargs fscanf(ptr str)
@ varargs fscanf_s(ptr str)
@ cdecl fseek(ptr long long) MSVCRT_fseek
@ cdecl fsetpos(ptr ptr) MSVCRT_fsetpos
@ cdecl ftell(ptr) MSVCRT_ftell
@ varargs fwprintf(ptr wstr) MSVCRT_fwprintf
@ varargs fwprintf_s(ptr wstr) MSVCRT_fwprintf_s
@ cdecl fwrite(ptr long long ptr) MSVCRT_fwrite
@ varargs fwscanf(ptr wstr)
@ varargs fwscanf_s(ptr wstr)
@ cdecl getc(ptr) MSVCRT_getc
@ cdecl getchar() MSVCRT_getchar
@ cdecl getenv(str)
@ cdecl getenv_s(ptr ptr long str)
@ cdecl gets(str) MSVCRT_gets
@ cdecl getwc(ptr) MSVCRT_getwc
@ cdecl getwchar() MSVCRT_getwchar
@ cdecl -arch=win32 gmtime(ptr) _gmtime32
@ cdecl -arch=win64 gmtime(ptr) _gmtime64
@ cdecl is_wctype(long long) iswctype
@ cdecl isalnum(long)
@ cdecl isalpha(long)
@ cdecl iscntrl(long)
@ cdecl isdigit(long)
@ cdecl isgraph(long)
@ cdecl isleadbyte(long)
@ cdecl islower(long)
@ cdecl isprint(long)
@ cdecl ispunct(long)
@ cdecl isspace(long)
@ cdecl isupper(long)
@ cdecl iswalnum(long)
@ cdecl iswalpha(long)
@ cdecl iswascii(long)
@ cdecl iswcntrl(long)
@ cdecl iswctype(long long)
@ cdecl iswdigit(long)
@ cdecl iswgraph(long)
@ cdecl iswlower(long)
@ cdecl iswprint(long)
@ cdecl iswpunct(long)
@ cdecl iswspace(long)
@ cdecl iswupper(long)
@ cdecl iswxdigit(long)
@ cdecl isxdigit(long)
@ cdecl labs(long)
@ cdecl ldexp(double long)
@ cdecl -ret64 ldiv(long long)
@ cdecl localeconv()
@ cdecl -arch=win32 localtime(ptr) _localtime32
@ cdecl -arch=win64 localtime(ptr) _localtime64
@ cdecl log(double)
@ cdecl log10(double)
@ cdecl -arch=!i386 logf(float)
@ cdecl -arch=!i386 log10f(float)
@ cdecl -arch=i386,x86_64,arm,arm64 longjmp(ptr long) MSVCRT_longjmp
@ cdecl malloc(long)
@ cdecl mblen(ptr long)
@ cdecl mbrlen(ptr long ptr)
@ cdecl mbrtowc(ptr str long ptr)
# stub mbsdup_dbg(wstr long ptr long)
@ cdecl mbsrtowcs(ptr ptr long ptr)
@ cdecl mbsrtowcs_s(ptr ptr long ptr long ptr)
@ cdecl mbstowcs(ptr str long)
@ cdecl mbstowcs_s(ptr ptr long str long) _mbstowcs_s
@ cdecl mbtowc(ptr str long)
@ cdecl memchr(ptr long long)
@ cdecl memcmp(ptr ptr long)
@ cdecl memcpy(ptr ptr long)
@ cdecl memcpy_s(ptr long ptr long)
@ cdecl memmove(ptr ptr long)
@ cdecl memmove_s(ptr long ptr long)
@ cdecl memset(ptr long long)
@ cdecl -arch=win32 mktime(ptr) _mktime32
@ cdecl -arch=win64 mktime(ptr) _mktime64
@ cdecl modf(double ptr)
@ cdecl -arch=!i386 modff(float ptr)
@ cdecl perror(str)
@ cdecl pow(double double)
@ cdecl -arch=!i386 powf(float float)
@ varargs printf(str) MSVCRT_printf
@ varargs printf_s(str) MSVCRT_printf_s
@ cdecl putc(long ptr) MSVCRT_putc
@ cdecl putchar(long) MSVCRT_putchar
@ cdecl puts(str) MSVCRT_puts
@ cdecl putwc(long ptr) MSVCRT_fputwc
@ cdecl putwchar(long) MSVCRT__fputwchar
@ cdecl qsort(ptr long long ptr)
@ cdecl qsort_s(ptr long long ptr ptr)
@ cdecl raise(long)
@ cdecl rand()
@ cdecl rand_s(ptr)
@ cdecl realloc(ptr long)
@ cdecl remove(str) MSVCRT_remove
@ cdecl rename(str str) MSVCRT_rename
@ cdecl rewind(ptr) MSVCRT_rewind
@ varargs scanf(str)
@ varargs scanf_s(str)
@ cdecl setbuf(ptr ptr) MSVCRT_setbuf
@ cdecl -arch=arm,x86_64 -norelay -private setjmp(ptr) MSVCRT__setjmp
@ cdecl setlocale(long str)
@ cdecl setvbuf(ptr str long long) MSVCRT_setvbuf
@ cdecl signal(long long)
@ cdecl sin(double)
@ cdecl sinh(double)
@ cdecl -arch=!i386 sinf(float)
@ cdecl -arch=!i386 sinhf(float)
@ varargs sprintf(ptr str)
@ varargs sprintf_s(ptr long str)
@ cdecl sqrt(double)
@ cdecl -arch=!i386 sqrtf(float)
@ cdecl srand(long)
@ varargs sscanf(str str)
@ varargs sscanf_s(str str)
@ cdecl strcat(str str)
@ cdecl strcat_s(str long str)
@ cdecl strchr(str long)
@ cdecl strcmp(str str)
@ cdecl strcoll(str str)
@ cdecl strcpy(ptr str)
@ cdecl strcpy_s(ptr long str)
@ cdecl strcspn(str str)
@ cdecl strerror(long)
@ cdecl strerror_s(ptr long long)
@ cdecl strftime(ptr long str ptr)
@ cdecl strlen(str)
@ cdecl strncat(str str long)
@ cdecl strncat_s(str long str long)
@ cdecl strncmp(str str long)
@ cdecl strncpy(ptr str long)
@ cdecl strncpy_s(ptr long str long)
@ cdecl strnlen(str long)
@ cdecl strpbrk(str str)
@ cdecl strrchr(str long)
@ cdecl strspn(str str) ntdll.strspn
@ cdecl strstr(str str)
@ cdecl strtod(str ptr)
@ cdecl strtok(str str)
@ cdecl strtok_s(ptr str ptr)
@ cdecl strtol(str ptr long)
@ cdecl strtoul(str ptr long)
@ cdecl strxfrm(ptr str long)
@ varargs swprintf(ptr wstr) _swprintf
@ varargs swprintf_s(ptr long wstr)
@ varargs swscanf(wstr wstr)
@ varargs swscanf_s(wstr wstr)
@ cdecl system(str)
@ cdecl tan(double)
@ cdecl tanh(double)
@ cdecl -arch=!i386 tanf(float)
@ cdecl -arch=!i386 tanhf(float)
@ cdecl -arch=win32 time(ptr) _time32
@ cdecl -arch=win64 time(ptr) _time64
@ cdecl tmpfile() MSVCRT_tmpfile
@ cdecl tmpfile_s(ptr) MSVCRT_tmpfile_s
@ cdecl tmpnam(ptr) MSVCRT_tmpnam
@ cdecl tmpnam_s(ptr long) MSVCRT_tmpnam_s
@ cdecl tolower(long)
@ cdecl toupper(long)
@ cdecl towlower(long)
@ cdecl towupper(long)
@ cdecl ungetc(long ptr) MSVCRT_ungetc
@ cdecl ungetwc(long ptr) MSVCRT_ungetwc
# stub utime
@ cdecl vfprintf(ptr str ptr) MSVCRT_vfprintf
@ cdecl vfprintf_s(ptr str ptr) MSVCRT_vfprintf_s
@ cdecl vfwprintf(ptr wstr ptr) MSVCRT_vfwprintf
@ cdecl vfwprintf_s(ptr wstr ptr) MSVCRT_vfwprintf_s
@ cdecl vprintf(str ptr) MSVCRT_vprintf
@ cdecl vprintf_s(str ptr) MSVCRT_vprintf_s
@ cdecl vsnprintf(ptr long str ptr) _vsnprintf
@ cdecl vsprintf(ptr str ptr)
@ cdecl vsprintf_s(ptr long str ptr)
@ cdecl vswprintf(ptr wstr ptr) _vswprintf
@ cdecl vswprintf_s(ptr long wstr ptr)
@ cdecl vwprintf(wstr ptr) MSVCRT_vwprintf
@ cdecl vwprintf_s(wstr ptr) MSVCRT_vwprintf_s
@ cdecl wcrtomb(ptr long ptr)
@ cdecl wcrtomb_s(ptr ptr long long ptr)
@ cdecl wcscat(wstr wstr)
@ cdecl wcscat_s(wstr long wstr)
@ cdecl wcschr(wstr long)
@ cdecl wcscmp(wstr wstr)
@ cdecl wcscoll(wstr wstr)
@ cdecl wcscpy(ptr wstr)
@ cdecl wcscpy_s(ptr long wstr)
@ cdecl wcscspn(wstr wstr) ntdll.wcscspn
@ cdecl wcsftime(ptr long wstr ptr)
@ cdecl wcslen(wstr)
@ cdecl wcsncat(wstr wstr long) ntdll.wcsncat
@ cdecl wcsncat_s(wstr long wstr long)
@ cdecl wcsncmp(wstr wstr long)
@ cdecl wcsncpy(ptr wstr long)
@ cdecl wcsncpy_s(ptr long wstr long)
@ cdecl wcsnlen(wstr long)
@ cdecl wcspbrk(wstr wstr)
@ cdecl wcsrchr(wstr long)
@ cdecl wcsrtombs(ptr ptr long ptr)
@ cdecl wcsrtombs_s(ptr ptr long ptr long ptr)
@ cdecl wcsspn(wstr wstr) ntdll.wcsspn
@ cdecl wcsstr(wstr wstr)
@ cdecl wcstod(wstr ptr)
@ cdecl wcstok(wstr wstr)
@ cdecl wcstok_s(ptr wstr ptr)
@ cdecl wcstol(wstr ptr long)
@ cdecl wcstombs(ptr ptr long)
@ cdecl wcstombs_s(ptr ptr long wstr long)
@ cdecl wcstoul(wstr ptr long)
@ cdecl wcsxfrm(ptr wstr long)
@ cdecl wctob(long)
@ cdecl wctomb(ptr long)
@ cdecl wctomb_s(ptr ptr long long)
@ varargs wprintf(wstr) MSVCRT_wprintf
@ varargs wprintf_s(wstr) MSVCRT_wprintf_s
@ varargs wscanf(wstr)
@ varargs wscanf_s(wstr)
