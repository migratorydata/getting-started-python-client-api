import abc
class Rxo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def PlX(self, host):
        pass
    @abc.abstractmethod
    def zRT(self, qOm):
        pass
    @abc.abstractmethod
    def gXx(self, host, encrypted):
        pass
import threading
class itA:
    def __init__(self, value):
        self._lock = threading.Lock()
        self._value = value
    def NJq(self, value):
        with self._lock:
            self._value = value
    def jOA(self):
        with self._lock:
            return self._value
    def __repr__(self) -> str:
        return str(self._value)
class MQT:
    def __init__(self, _start, _end):
        self._start = _start
        self._end = _end
    def UOp(self):
        return self._start
    def FWA(self):
        return self._end
import abc
class MigratoryDataListener(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def on_message(self, message):
        pass
    @abc.abstractmethod
    def on_status(self, status, info):
        pass
class MigratoryDataLogLevel:
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
import abc
class MigratoryDataLogListener(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractmethod
    def on_log(self, log, migratory_data_log_level):
        pass
class QoS:
    STANDARD = 0
    GUARANTEED = 1
class MessageType:
    SNAPSHOT = 0
    UPDATE = 1
    RECOVERED = 2
    HISTORICAL = 3
class MigratoryDataMessage:
    def __init__(self, _subject, _content, closure=None, qos=QoS.GUARANTEED, retained=True, reply_subject=None):
        self._subject = _subject
        self._content = _content
        self._closure = closure
        self._reply_to_subject = reply_subject
        self.wLy = qos
        self._retained = retained
        self._message_type = MessageType.UPDATE
        self._seq = None
        self._epoch = None
        self._compression = None
    def get_subject(self):
        return self._subject
    def get_content(self):
        return self._content
    def get_closure(self):
        return self._closure
    def get_reply_to_subject(self):
        return self._reply_to_subject
    def is_retained(self):
        return self._retained
    def get_seq(self):
        return self._seq
    def get_epoch(self):
        return self._epoch
    def get_qos(self):
        return self.wLy
    def get_message_type(self):
        return self._message_type
    def set_compressed(self, compression_bool):
        self._compression = compression_bool
    def is_compressed(self):
        return self._compression
    def __repr__(self) -> str:
        pYk = "["
        pYk += "Subj = " + str(self._subject) + ", "
        pYk += "Content =  " + str(self._content.decode("utf-8")) + ", "
        pYk += "Closure =  " + str(self._closure) + ", "
        pYk += "ReplyToSubject =  " + str(self._reply_to_subject) + ", "
        pYk += "Retained = " + str(self._retained) + ", "
        pYk += "QOS = " + self.upa() + ", "
        pYk += "MessageType = " + self.FMb() + ", "
        pYk += "Seq = " + str(self._seq) + ", "
        pYk += "Epoch = " + str(self._epoch) + " "
        pYk += "Compression = " + str(self._compression) + " "
        pYk += "]"
        return pYk
    def upa(self):
        if self.wLy == QoS.STANDARD:
            return "STANDARD"
        return "GUARANTEED"
    def FMb(self):
        if self._message_type == MessageType.SNAPSHOT:
            return "SNAPSHOT"
        if self._message_type == MessageType.UPDATE:
            return "UPDATE"
        if self._message_type == MessageType.RECOVERED:
            return "RECOVERED"
        return "HISTORICAL"
class MaL:
    def __init__(self):
        self.scK = bytearray()
        self.qvv = 0
        self.content_length_mark = -1
        self.payload_mark = -1
        self.body_start_mark = -1
        self.body_end_mark = -1
    def kMb(self, qvv):
        self.qvv = qvv
    def extend(self, NUn):
        self.scK.extend(NUn)
    def append(self, NUn):
        self.scK.append(NUn)
    def iQt(self):
        self.scK = self.scK[self.qvv:]
        self.qvv = 0
    def clear(self):
        self.scK = bytearray()
        self.qvv = 0
    def dKt(self):
        if self.qvv == 0:
            return self.scK
        else:
            return self.scK[self.qvv:]
import threading
import socket
class niY(threading.Thread):
    def __init__(self, _socket, connection, uuid):
        threading.Thread.__init__(self)
        self._socket = _socket
        self._connection = connection
        self._buf = MaL()
        self._uuid = uuid
        self._run = True
    def run(self):
        while self._run:
            try:
                ULC = self._socket.recv(32768)
                if len(ULC) == 0:
                    break
                self._buf.extend(ULC)
                self._connection.kOr(self._buf)
                if self._buf.qvv > 0 and self._buf.qvv < len(self._buf.scK):
                    self._buf.iQt()
                elif self._buf.qvv >= len(self._buf.scK):
                    self._buf.clear()
            except (OSError, socket.error) as tcU:
                pass
        self._connection.gBI(self._uuid, ePo.DMb, "read_thread")
    def EZz(self):
        self._run = False
import queue
import threading
import socket
class xqG(threading.Thread):
    def __init__(self, _socket):
        threading.Thread.__init__(self)
        self._socket = _socket
        self._message_queue = queue.Queue()
        self._run = True
        self._stop_event = None
    def run(self):
        while self._run:
            try:
                message = self._message_queue.get(True, 0.1)
                if message is not None:
                    self._socket.send(bytes(message))
            except (queue.Empty or socket.error) as tcU:
                pass
    def cBR(self, message):
        self._message_queue.put(message)
    def EZz(self):
        self._run = False
import logging
class Rci(MigratoryDataLogListener):
    def __init__(self):
        self.log1 = logging.getLogger("CLIENT")
        self.log1.setLevel(logging.INFO)
        mvv = logging.StreamHandler()
        mvv.setLevel(logging.INFO)
        NtO = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        mvv.setFormatter(NtO)
        del self.log1.handlers[:]
        self.log1.addHandler(mvv)
    def on_log(self, log, migratory_data_log_level):
        if migratory_data_log_level == MigratoryDataLogLevel.TRACE:
            self.log1.debug(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.DEBUG:
            self.log1.debug(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.INFO:
            self.log1.info(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.WARN:
            self.log1.warning(log)
        elif migratory_data_log_level == MigratoryDataLogLevel.ERROR:
            self.log1.error(log)
import abc
class SMh(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def trace(self, message):
        pass
    @abc.abstractmethod
    def debug(self, message):
        pass
    @abc.abstractmethod
    def info(self, message):
        pass
    @abc.abstractmethod
    def warn(self, message):
        pass
    @abc.abstractmethod
    def error(self, message):
        pass
import threading
class hmN(SMh):
    def __init__(self):
        self._lock = threading.Lock()
        self._log_listener = Rci()
        self._log_level = MigratoryDataLogLevel.INFO
    def WXL(self, log_listener, log_level):
        with self._lock:
            self._log_listener = log_listener
            self._log_level = log_level
    def error(self, message):
        if self._log_level <= MigratoryDataLogLevel.ERROR:
            self._log_listener.on_log(message, MigratoryDataLogLevel.ERROR)
    def trace(self, message):
        if self._log_level <= MigratoryDataLogLevel.TRACE:
            self._log_listener.on_log(message, MigratoryDataLogLevel.TRACE)
    def debug(self, message):
        if self._log_level <= MigratoryDataLogLevel.DEBUG:
            self._log_listener.on_log(message, MigratoryDataLogLevel.DEBUG)
    def warn(self, message):
        if self._log_level <= MigratoryDataLogLevel.WARN:
            self._log_listener.on_log(message, MigratoryDataLogLevel.WARN)
    def info(self, message):
        if self._log_level <= MigratoryDataLogLevel.INFO:
            self._log_listener.on_log(message, MigratoryDataLogLevel.INFO)
class NWM:
    UUl = "[READ_EVENT]"
    tTw = "[PING_EVENT]"
    plL = "[CONNECT_EVENT]"
    cQS = "[DISCONNECT_EVENT]"
    IZI = "[READER_DISCONNECT_EVENT]"
    Tow = "[MESSAGE_RECEIVED_EVENT]"
    Mvc = "[WRITE_EVENT]"
    cEZ = "[CLIENT_PUBLISH_RESPONSE]"
    OKZ = "[OKZ]"
    CzO = "[ENTITLEMENT_CHECK_RESPONSE]"
    lua = "[DISPOSE_EVENT]"
    AxS = "[PAUSE_EVENT]"
    Jkt = "[RESUME_EVENT]"
    XkY = "[SUBSCRIBE_EVENT]"
    wWM = "[UNSUBSCRIBE_EVENT]"
    Ozz = "[PUBLISH_EVENT]"
    Bro = "[REPUBLISH_EVENT"
    oix = "[PING_SERVER_EVENT]"
    qMN = "[CONNECT_SERVER_EVENT]"
    pmT = "[RECONNECT_EVENT]"
class oYH:
    eSN = 0
    AWZ = 1
    Rbt = 2
class neA:
    fPH = "cache_ok"
    fMn = 2
    def __init__(self, OzJ, history):
        self._subject = OzJ
        self._history = history
        self._seq = 0
        self._seq_id = 70000
        self._need_recovery = False
        self._nr_of_consecutive_recoveries = 0
        self._messages_recieved_until_recovery = 0
        self._cache_recovery_status = neA.fPH
        self._current_subscribe_type = oYH.eSN
    def get_seq(self):
        return self._seq
    def nPZ(self, VYj):
        self._seq = VYj
        self._messages_recieved_until_recovery += 1
    def kpt(self):
        return self._seq_id
    def Lrx(self, QQw):
        self._seq_id = QQw
    def get_subject(self):
        return self._subject
    def zVf(self):
        return self._history
    def AIP(self):
        self._messages_recieved_until_recovery = 0
        if self.YiO():
            self._nr_of_consecutive_recoveries += 1
    def XQa(self):
        self._nr_of_consecutive_recoveries = 0
    def iHb(self):
        return self._messages_recieved_until_recovery
    def ywx(self, status):
        self._cache_recovery_status = status
    def YeV(self):
        return self._cache_recovery_status
    def YiO(self):
        return self._seq_id != 70000
    def lcO(self):
        type = oYH.eSN
        if self.YiO():
            if self._nr_of_consecutive_recoveries >= neA.fMn:
                if self._history > 0:
                    type = oYH.AWZ
            else:
                type = oYH.Rbt
        else:
            if self._history > 0:
                type = oYH.AWZ
        if type == oYH.eSN or type == oYH.AWZ:
            self.ywx(neA.fPH)
            self.XQa()
        self._current_subscribe_type = type
        return type
    def ytv(self):
        return self._current_subscribe_type
    def fGY(self):
        self._current_subscribe_type = oYH.eSN
    def JfS(self):
        self._seq = 0
        self._seq_id = 70000
        self._need_recovery = False
        self._nr_of_consecutive_recoveries = 0
        self._messages_recieved_until_recovery = 0
        self._cache_recovery_status = self.fPH
        self._current_subscribe_type = oYH.eSN
    def __repr__(self) -> str:
        pYk = "["
        pYk += "Subj = " + str(self._subject) + ", "
        pYk += "Seq = " + str(self._seq) + ", "
        pYk += "SeqId = " + str(self._seq_id) + ", "
        pYk += "NeedRecovery = " + str(self._need_recovery) + ", "
        pYk += "MessagesReceivedUntilRecovery = " + str(self._messages_recieved_until_recovery) + ", "
        pYk += "CacheRecoveryStatus = " + str(self._cache_recovery_status) + ", "
        pYk += "SubsType = " + str(self._current_subscribe_type) + ", "
        pYk += "NrOfConsecutiveRecovery = " + str(self._nr_of_consecutive_recoveries)
        pYk += "]"
        return pYk
class ICX:
    def __init__(self, operation, lGN):
        self.operation = operation
        self.lGN = lGN
    def __repr__(self) -> str:
        pYk = "OPERATION " + str(self.vjp(int(self.operation))) + " - "
        pYk += "Headers "
        for pAK in self.lGN:
            Ldc = str(self.dqh(int(pAK)))
            value = None
            if Ldc == "MESSAGE_TYPE" and isinstance(Ldc, int):
                value = self.AiS(int(self.lGN.get(pAK)))
            else:
                value = str(self.lGN.get(pAK))
            pYk += Ldc + ": " + value + " - "
        return pYk
    def vjp(self, number):
        if number == 0:
            return "SUBSCRIBE"
        elif number == 1:
            return "UNSUBSCRIBE"
        elif number == 2:
            return "PUBLISH"
        elif number == 3:
            return "PING"
        elif number == 4:
            return "IFRAME"
        elif number == 5:
            return "DISCONNECT"
        elif number == 6:
            return "RECOVERY_CACHE"
        elif number == 7:
            return "ENTITLEMENT_CHECK"
        elif number == 8:
            return "PROXY"
        elif number == 9:
            return "CLIENT_PUBLISH"
        elif number == 10:
            return "CLIENT_PUBLISH_RESPONSE"
        elif number == 11:
            return "CONNECT"
        elif number == 12:
            return "STATUS_EVENT"
        elif number == 13:
            return "AUTHORIZATION_TOKEN_UPDATE"
    def dqh(self, number):
        if number == 0:
            return "SUBJECT"
        elif number == 1:
            return "DATA"
        elif number == 2:
            return "SEQ"
        elif number == 3:
            return "SEQ_ID"
        elif number == 4:
            return "ENCODING"
        elif number == 5:
            return "SESSION_ID"
        elif number == 6:
            return "DOMAIN"
        elif number == 7:
            return "CALLBACK"
        elif number == 8:
            return "IFRAME_FUNCTION"
        elif number == 9:
            return "ERROR"
        elif number == 10:
            return "PUBLISH_PASSWORD"
        elif number == 11:
            return "DOUBLE_PING"
        elif number == 12:
            return "SUBJECT_CACHE_END"
        elif number == 13:
            return "ENTITLEMENT_TOKEN"
        elif number == 14:
            return "ENTITLEMENT_STATUS"
        elif number == 15:
            return "WORKGROUP"
        elif number == 16:
            return "ACK_SUBSCRIBE"
        elif number == 17:
            return "PUBLICATION_RETAINED"
        elif number == 18:
            return "PUBLICATION_QOS"
        elif number == 19:
            return "AGENT_NAME"
        elif number == 20:
            return "PUSH_NOTIFICATION"
        elif number == 21:
            return "MESSAGE_TYPE"
        elif number == 22:
            return "USER_AGENT"
        elif number == 23:
            return "SESSION_TYPE"
        elif number == 24:
            return "SERVER_CLIENT_PING_TIME"
        elif number == 25:
            return "CLOSURE"
        elif number == 26:
            return "NODE_TYPE"
        elif number == 27:
            return "HISTORICAL_MESSAGES"
        elif number == 28:
            return "REPLY_SUBJECT"
        elif number == 29:
            return "VERSION"
        elif number == 30:
            return "PUBLISH_SAMPLE"
        elif number == 31:
            return "PUBLISH_SAMPLE_TIMESTAMP"
        elif number == 32:
            return "CLUSTER_TOKEN"
    def AiS(self, number):
        if number == 1:
            return "SNAPSHOT"
        elif number == 2:
            return "UPDATE"
        elif number == 3:
            return "RECOVERY"
class xjU:
    WIY = 0
    hFL = 1
    ZSv = 2
    kkU = 3
import struct
class mGi:
    CuL = []
    drb = []
    APG = []
    dWc = []
    sMB = 0x19
    rwC = 0x7F
    IDL = 0x1E
    mRu = 0x1F
    sKU = []
    lGN = []
    Djt = []
    @staticmethod
    def yuT():
        for Dke in range(0, 128):
            mGi.CuL.append(-1)
        mGi.CuL[WUY.IRI] = 0x01
        mGi.CuL[WUY.IRf] = 0x02
        mGi.CuL[WUY.iYv] = 0x03
        mGi.CuL[WUY.pyt] = 0x04
        mGi.CuL[WUY.YsY] = 0x05
        mGi.CuL[WUY.xGO] = 0x06
        mGi.CuL[WUY.GHC] = 0x08
        mGi.CuL[WUY.ufk] = 0x09
        mGi.CuL[WUY.HAi] = 0x0C
        mGi.CuL[WUY.Ych] = 0x10
        mGi.CuL[WUY.CLIENT_PUBLISH_RESPONSE] = 0x13
        mGi.CuL[WUY.CIe] = 0x1A
        mGi.CuL[WUY.oVM] = 0x07
        mGi.CuL[WUY.tly] = 0x0B
        for Dke in range(0, 128):
            mGi.sKU.append(-1)
        for cUX in range(0, WUY.tly + 1):
            mGi.sKU[mGi.ZAi(cUX)] = cUX
        for Dke in range(0, 128):
            mGi.drb.append(-1)
        mGi.drb[kDW.oqX] = 0x01
        mGi.drb[kDW.hkG] = 0x02
        mGi.drb[kDW.bZd] = 0x03
        mGi.drb[kDW.zHl] = 0x04
        mGi.drb[kDW.BGQ] = 0x05
        mGi.drb[kDW.ikH] = 0x06
        mGi.drb[kDW.ZLS] = 0x07
        mGi.drb[kDW.OAK] = 0x08
        mGi.drb[kDW.obi] = 0x09
        mGi.drb[kDW.ERROR] = 0x0B
        mGi.drb[kDW.JeP] = 0x0C
        mGi.drb[kDW.uRk] = 0x0F
        mGi.drb[kDW.GWZ] = 0x10
        mGi.drb[kDW.GvT] = 0x11
        mGi.drb[kDW.Pgv] = 0x12
        mGi.drb[kDW.jfs] = 0x13
        mGi.drb[kDW.HKe] = 0x14
        mGi.drb[kDW.ZtG] = 0x15
        mGi.drb[kDW.lHc] = 0x16
        mGi.drb[kDW.aeZ] = 0x17
        mGi.drb[kDW.lXT] = 0x18
        mGi.drb[kDW.gyv] = 0x1A
        mGi.drb[kDW.cSO] = 0x20
        mGi.drb[kDW.TUh] = 0x27
        mGi.drb[kDW.Znl] = 0x28
        mGi.drb[kDW.QBt] = 0x23
        mGi.drb[kDW.hxh] = 0x24
        mGi.drb[kDW.Vqk] = 0x25
        mGi.drb[kDW.AeZ] = 0x2C
        mGi.drb[kDW.NCS] = 0x2D
        mGi.drb[kDW.lwp] = 0x2E
        mGi.drb[kDW.ikQ] = 0x2F
        mGi.drb[kDW.JLy] = 0x30
        mGi.drb[kDW.xbr] = 0x1D
        mGi.drb[kDW.Rhf] = 0x26
        for Dke in range(0, 128):
            mGi.lGN.append(-1)
        for cUX in range(0, kDW.Rhf + 1):
            mGi.lGN[mGi.xwk(cUX)] = cUX
        for Dke in range(0, 128):
            mGi.Djt.append(-1)
        mGi.Jjn(kDW.oqX, MzE.lJf)
        mGi.Jjn(kDW.hkG, MzE.TmD)
        mGi.Jjn(kDW.bZd, MzE.YMx)
        mGi.Jjn(kDW.zHl, MzE.YMx)
        mGi.Jjn(kDW.BGQ, MzE.YMx)
        mGi.Jjn(kDW.ikH, MzE.YMx)
        mGi.Jjn(kDW.ZLS, MzE.TmD)
        mGi.Jjn(kDW.OAK, MzE.TmD)
        mGi.Jjn(kDW.obi, MzE.TmD)
        mGi.Jjn(kDW.ERROR, MzE.YMx)
        mGi.Jjn(kDW.JeP, MzE.TmD)
        mGi.Jjn(kDW.uRk, MzE.YMx)
        mGi.Jjn(kDW.Pgv, MzE.lJf)
        mGi.Jjn(kDW.jfs, MzE.lJf)
        mGi.Jjn(kDW.HKe, MzE.lJf)
        mGi.Jjn(kDW.ZtG, MzE.YMx)
        mGi.Jjn(kDW.lHc, MzE.YMx)
        mGi.Jjn(kDW.aeZ, MzE.YMx)
        mGi.Jjn(kDW.lXT, MzE.YMx)
        mGi.Jjn(kDW.gyv, MzE.lJf)
        mGi.Jjn(kDW.cSO, MzE.lJf)
        mGi.Jjn(kDW.TUh, MzE.lJf)
        mGi.Jjn(kDW.QBt, MzE.lJf)
        mGi.Jjn(kDW.hxh, MzE.YMx)
        mGi.Jjn(kDW.Vqk, MzE.YMx)
        mGi.Jjn(kDW.GWZ, MzE.lJf)
        mGi.Jjn(kDW.GvT, MzE.YMx)
        mGi.Jjn(kDW.Znl, MzE.YMx)
        mGi.Jjn(kDW.AeZ, MzE.lJf)
        mGi.Jjn(kDW.NCS, MzE.YMx)
        mGi.Jjn(kDW.lwp, MzE.YMx)
        mGi.Jjn(kDW.ikQ, MzE.YMx)
        mGi.Jjn(kDW.JLy, MzE.lJf)
        mGi.Jjn(kDW.xbr, MzE.YMx)
        mGi.Jjn(kDW.Rhf, MzE.YMx)
        for Dke in range(0, 255):
            mGi.dWc.append(-1)
        mGi.dWc[mGi.rwC] = 0x01;
        mGi.dWc[mGi.IDL] = 0x02;
        mGi.dWc[mGi.mRu] = 0x03;
        mGi.dWc[Vjo.QZJ] = 0x04;
        mGi.dWc[Vjo.qRg] = 0x05;
        mGi.dWc[Vjo.HUj] = 0x06;
        mGi.dWc[Vjo.KPC] = 0x07;
        mGi.dWc[Vjo.GTB] = 0x08;
        mGi.dWc[33] = 0x09;
        mGi.dWc[mGi.sMB] = 0x0B;
        for Dke in range(0, 255):
            mGi.APG.append(-1)
        for cUX in range(0, 128):
            tcU = mGi.mjs(cUX)
            if tcU != -1:
                mGi.APG[tcU] = cUX
    @staticmethod
    def Jjn(GyM, hdr_type):
        mGi.Djt[mGi.xwk(GyM)] = hdr_type
    @staticmethod
    def SWu(LMa):
        hXI = mGi.CTk(LMa)
        ydo = 0
        for Txv in range(0, len(hXI)):
            dWc = mGi.mjs(hXI[Txv])
            if dWc != -1:
                ydo += 1
        if ydo == 0:
            scK = bytearray()
            scK.extend(hXI)
            return scK
        pMX = []
        for cUX in range(0, len(hXI) + ydo):
            pMX.append(0)
        Txv = 0
        rJz = 0
        while Txv < len(hXI):
            dWc = mGi.mjs(hXI[Txv])
            if dWc != -1:
                pMX[rJz] = mGi.mRu
                pMX[rJz + 1] = dWc
                rJz += 1
            else:
                pMX[rJz] = hXI[Txv]
            Txv += 1
            rJz += 1
        scK = bytearray()
        scK.extend(pMX)
        return scK
    @staticmethod
    def fjR(hXI):
        ydo = 0
        for Txv in range(0, len(hXI)):
            dWc = mGi.mjs(hXI[Txv])
            if dWc != -1:
                ydo += 1
        if ydo == 0:
            return hXI
        pMX = []
        for cUX in range(0, len(hXI) + ydo):
            pMX.append(0)
        Txv = 0
        rJz = 0
        while Txv < len(hXI):
            dWc = mGi.mjs(hXI[Txv])
            if dWc != -1:
                pMX[rJz] = mGi.mRu
                pMX[rJz + 1] = dWc
                rJz += 1
            else:
                pMX[rJz] = hXI[Txv]
            Txv += 1
            rJz += 1
        scK = bytearray()
        scK.extend(pMX)
        return scK
    @staticmethod
    def vAI(LMa):
        hXI = list(struct.unpack(len(LMa) * 'B', LMa))
        ydo = 0
        if len(hXI) == 0:
            return LMa
        for Txv in range(0, len(hXI)):
            if hXI[Txv] == mGi.mRu:
                ydo += 1
        pMX = []
        for cUX in range(0, len(hXI) - ydo):
            pMX.append(0)
        Txv = 0
        rJz = 0
        while Txv < len(hXI):
            NLN = hXI[Txv]
            if NLN == mGi.mRu:
                if Txv + 1 < len(hXI):
                    pMX[rJz] = mGi.mVK(hXI[Txv + 1])
                    if pMX[rJz] == -1:
                        raise ValueError()
                    Txv += 1
                else:
                    raise ValueError()
            else:
                pMX[rJz] = NLN
            Txv += 1
            rJz += 1
        scK = bytearray()
        scK.extend(pMX)
        return scK
    @staticmethod
    def PxB(LMa, _headerId, _headerType):
        TFi = None
        Pzw = LMa.find(chr(mGi.xwk(_headerId)))
        OiJ = LMa.find(chr(mGi.IDL), Pzw)
        if Pzw != -1 and OiJ != -1:
            ZFB = LMa[Pzw + 1:OiJ]
            if _headerType == MzE.gys:
                TFi = ZFB
            elif _headerType == MzE.TmD:
                TFi = ZFB
            elif _headerType == MzE.lJf:
                TFi = ZFB
            elif _headerType == MzE.YMx:
                TFi = mGi.HDS(ZFB);
        return TFi
    @staticmethod
    def HDS(_dataString):
        LMa = list(struct.unpack(len(_dataString) * 'B', _dataString))
        pMX = 0
        EIQ = -1
        _val = 0
        xsk = len(LMa)
        RLk = 0
        if xsk == 1:
            return LMa[0]
        elif xsk == 2 and LMa[RLk] == mGi.mRu:
            NLN = mGi.mVK(LMa[RLk + 1])
            if NLN != -1:
                return NLN
            else:
                raise ValueError()
        while xsk > 0:
            NLN = LMa[RLk]
            RLk += 1
            if NLN == mGi.mRu:
                if xsk - 1 < 0:
                    raise ValueError()
                xsk -= 1
                NLN = LMa[RLk]
                RLk += 1
                wII = mGi.mVK(NLN)
                if wII == -1:
                    raise ValueError()
            else:
                wII = NLN
            if EIQ > 0:
                _val |= wII >> EIQ
                pMX = pMX << 8 | (_val if _val >= 0   else _val + 256)
                _val = (wII << (8 - EIQ))
            else:
                _val = (wII << - EIQ)
            EIQ = (EIQ + 7) % 8;
            xsk -= 1
        return pMX
    @staticmethod
    def hcr(_val):
        if (int(_val) & 0xFFFFFF80) == 0:
            cUX = mGi.mjs(_val)
            if cUX == -1:
                return struct.pack('B', _val)
            else:
                return struct.pack('BB', mGi.mRu, cUX)
        zom = 0
        if (int(_val) & 0xFF000000) != 0:
            zom = 24
        elif (int(_val) & 0x00FF0000) != 0:
            zom = 16
        else:
            zom = 8
        pMX = []
        for cUX in range(0, 10):
            pMX.append(0)
        TRb = 0
        zES = 0
        while zom >= 0:
            b = ((int(_val) >> zom) & 0xFF)
            zES += 1
            pMX[TRb] |= ((b if b >= 0 else b + 256) >> zES)
            dWc = mGi.mjs(pMX[TRb])
            if dWc != -1:
                pMX[TRb] = mGi.mRu
                pMX[TRb + 1] = dWc
                TRb += 1
            TRb += 1
            pMX[TRb] |= (b << (7 - zES)) & 0x7F;
            zom -= 8
        dWc = mGi.mjs(pMX[TRb])
        if dWc != -1:
            pMX[TRb] = mGi.mRu
            pMX[TRb + 1] = dWc
            TRb += 1
        TRb += 1
        if TRb < len(pMX):
            pMX = pMX[0:TRb]
        scK = bytearray()
        scK.extend(pMX)
        return scK
    @staticmethod
    def mVK(b):
        if b >= 0:
            return mGi.APG[int(b)]
        else:
            return -1
    @staticmethod
    def mjs(b):
        if b >= 0:
            return mGi.dWc[int(b)]
        else:
            return -1
    @staticmethod
    def xwk(h):
        return mGi.drb[int(h)]
    @staticmethod
    def ZAi(o):
        return mGi.CuL[int(o)]
    @staticmethod
    def YnD(GyM):
        oMs = mGi.xwk(GyM)
        return mGi.Djt[oMs]
    @staticmethod
    def CTk(str_value):
        NYd = str_value.encode('utf-8')
        return list(struct.unpack(len(NYd) * 'B', NYd))
    @staticmethod
    def Byf(b):
        if b < 0:
            return None
        return mGi.lGN[b]
class WUY:
    IRI = 0
    IRf = 1
    iYv = 2
    pyt = 3
    YsY = 4
    xGO = 5
    GHC = 6
    ufk = 7
    HAi = 8
    Ych = 9
    CLIENT_PUBLISH_RESPONSE = 10
    CIe = 11
    oVM = 12
    tly = 13
class kDW:
    oqX = 0
    hkG = 1
    bZd = 2
    zHl = 3
    BGQ = 4
    ikH = 5
    ZLS = 6
    OAK = 7
    obi = 8
    ERROR = 9
    JeP = 10
    uRk = 11
    Pgv = 12
    jfs = 13
    HKe = 14
    ZtG = 15
    lHc = 16
    aeZ = 17
    lXT = 18
    gyv = 19
    cSO = 20
    TUh = 21
    QBt = 22
    hxh = 23
    Vqk = 24
    GWZ = 25
    GvT = 26
    Znl = 27
    AeZ = 28
    NCS = 29
    lwp = 30
    ikQ = 31
    JLy = 32
    xbr = 33
    Rhf = 34
class MzE:
    gys = 0
    TmD = 1
    lJf = 2
    YMx = 3
class Vjo:
    QZJ = 0x00
    KPC = 0x22
    qRg = 0x0A
    HUj = 0x0D
    GTB = 0x5C
class tYP:
    qEJ = 1
    APP = 2
    gPE = 3
    TMz = 4
class ZHq:
    Yfh = 0
    kFD = 1
    ntw = 2
    evv = 3
    MHJ = 4
    khN = 5
    ocr = 6
    jhY = 7
    mBr = 8
class yIi:
    SNAPSHOT = "1"
    UPDATE = "2"
    RECOVERED = "3"
    HISTORICAL = "4"
class XUH:
    TUy = "d"
    gsR = "a"
mGi.yuT()
class qIy(Rxo):
    NfK = "POST / HTTP/1.1\r\n"
    wSY = "Host: "
    aaX = "Content-Length: "
    Pgb = "000"
    PNg = "\r\n"
    def __init__(self):
        pass
    def PlX(self, host):
        qOm = MaL()
        qOm.extend(bytes(qIy.NfK, 'utf-8'))
        qOm.extend(bytes(qIy.wSY, 'utf-8'))
        qOm.extend(bytes(host, 'utf-8'))
        qOm.extend(bytes(qIy.PNg, 'utf-8'))
        qOm.extend(bytes(qIy.aaX, 'utf-8'))
        qOm.content_length_mark = len(qOm.scK)
        qOm.extend(bytes(qIy.Pgb, 'utf-8'))
        qOm.extend(bytes(qIy.PNg, 'utf-8'))
        qOm.extend(bytes(qIy.PNg, 'utf-8'))
        qOm.payload_mark = len(qOm.scK)
        return qOm
    def zRT(self, qOm):
        qvv = len(qOm.scK)
        UYw = len(qOm.scK) - qOm.payload_mark
        qXr = bytes(str(UYw), 'utf-8')
        if len(qXr) <= len(qIy.Pgb):
            qoc = 0
            for cUX in range(len(qIy.Pgb) - len(qXr),
                           len(qIy.Pgb)):
                qOm.scK[qOm.content_length_mark + cUX] = qXr[qoc]
                qoc = qoc + 1
        else:
            cbz = qOm.scK[0:qOm.content_length_mark]
            cbz.extend(qXr)
            cbz.extend(qOm.scK[(qOm.content_length_mark + len(qIy.Pgb)):])
            qOm.scK = cbz
    def gXx(self, host, encrypted):
        qOm = MaL()
        return qOm
import random
class IhQ(Rxo):
    pGS = "GET /WebSocketConnection HTTP/1.1\r\n"
    brw = "GET /WebSocketConnection-Secure HTTP/1.1\r\n"
    meX = "Host: "
    PRo = "Origin: "
    ggs = "Upgrade: websocket\r\n"
    yHp = "Sec-WebSocket-Key: 23eds34dfvce4\r\n"
    xcd = "Sec-WebSocket-Version: 13\r\n"
    ReC = "Sec-WebSocket-Protocol: pushv1\r\n"
    ied = "Connection: Upgrade\r\n"
    PNg = "\r\n"
    Ysu = 2
    pVK = 10
    ziS = 128
    DxW = 128
    def PlX(self, host):
        qOm = MaL()
        qvv = IhQ.pVK
        for cUX in range(0, 10):
            qOm.extend(bytes([0]))
        for cUX in range(0, 4):
            qvv += 1
            gtZ = random.randint(0, 255)
            qOm.extend([gtZ])
        qOm.kMb(qvv)
        qOm.body_start_mark = qvv
        return qOm
    def zRT(self, qOm):
        XNK = IhQ.DxW
        XNK |= IhQ.Ysu
        qOm.body_end_mark = len(qOm.scK)
        TwP = qOm.body_end_mark - qOm.body_start_mark
        lXf = self.vsA(TwP)
        qoG = self.xBq(TwP, lXf)
        PFV = 0
        rdn = 0
        if lXf == 1:
            PFV = 8
            rdn = 8
            qOm.scK[rdn] = XNK
            qOm.scK[rdn + 1] = qoG[0] | IhQ.ziS
        elif lXf == 2:
            PFV = 6
            rdn = 6
            qOm.scK[rdn] = XNK
            qOm.scK[rdn + 1] = 126 | IhQ.ziS
            rdn += 2
            for cUX in range(0, 2):
                qOm.scK[rdn + cUX] = qoG[cUX]
        else:
            qOm.scK[rdn] = XNK
            qOm.scK[rdn + 1] = 127 | IhQ.ziS
            rdn += 2
            for cUX in range(0, 8):
                qOm.scK[rdn + cUX] = qoG[cUX]
        HNa = bytearray()
        HNa.extend([qOm.scK[qOm.body_start_mark - 4]])
        HNa.extend([qOm.scK[qOm.body_start_mark - 3]])
        HNa.extend([qOm.scK[qOm.body_start_mark - 2]])
        HNa.extend([qOm.scK[qOm.body_start_mark - 1]])
        tvc = 0
        for cUX in range(qOm.body_start_mark, qOm.body_end_mark):
            b = qOm.scK[cUX] ^ HNa[tvc]
            qOm.scK[cUX] = b
            if tvc == 3:
                tvc = 0
            else:
                tvc += 1
        qOm.kMb(PFV)
    def gXx(self, host, encrypted):
        qOm = MaL()
        if encrypted is False:
            qOm.extend(bytes(IhQ.pGS, 'utf-8'))
        else:
            qOm.extend(bytes(IhQ.brw, 'utf-8'))
        qOm.extend(bytes(IhQ.PRo, 'utf-8'))
        qOm.extend(bytes("http://" + str(host), 'utf-8'))
        qOm.extend(bytes(IhQ.PNg, 'utf-8'))
        qOm.extend(bytes(IhQ.meX, 'utf-8'))
        qOm.extend(bytes(str(host), 'utf-8'))
        qOm.extend(bytes(IhQ.PNg, 'utf-8'))
        qOm.extend(bytes(IhQ.ggs, 'utf-8'))
        qOm.extend(bytes(IhQ.ied, 'utf-8'))
        qOm.extend(bytes(IhQ.yHp, 'utf-8'))
        qOm.extend(bytes(IhQ.xcd, 'utf-8'))
        qOm.extend(bytes(IhQ.ReC, 'utf-8'))
        qOm.extend(bytes(IhQ.PNg, 'utf-8'))
        return qOm
    def vsA(self, size):
        if size <= 125:
            return 1
        elif size <= 65535:
            return 2
        return 8
    def xBq(self, value, lXf):
        OcO = bytearray()
        Ixn = 8 * lXf - 8
        for cUX in range(0, lXf):
            GQv = self.toV(value, Ixn - 8 * cUX)
            xXz = GQv - (256 * int(GQv / 256))
            OcO.extend([xXz])
        return OcO
    def toV(self, val, n):
        return (val % 0x100000000) >> n
import time
import zlib
import base64
class sMm:
    def __init__(self):
        self._encoding = ZHq.mBr
    def MPg(self):
        self._encoding = ZHq.MHJ
    def eph(self, scK, entitlement_token, session_type, user_agent, version):
        scK.extend(bytes(chr(mGi.ZAi(WUY.CIe)), 'utf-8'))
        if entitlement_token is not None:
            self.mJK(scK, mGi.xwk(kDW.jfs),
                                   mGi.SWu(entitlement_token))
        if session_type is not None:
            self.mJK(scK, mGi.xwk(kDW.hxh),
                                   mGi.hcr(session_type))
        if user_agent is not None:
            self.mJK(scK, mGi.xwk(kDW.QBt),
                                   mGi.SWu(user_agent))
        self.mJK(scK, mGi.xwk(kDW.NCS),
                               mGi.hcr(version))
        self.mJK(scK, mGi.xwk(kDW.BGQ),
                               mGi.hcr(self._encoding))
        scK.extend(bytes(chr(mGi.rwC), 'utf-8'))
    def Ygn(self, scK, OzJ, session_id):
        scK.extend(bytes(chr(mGi.ZAi(WUY.IRI)), 'utf-8'))
        self.mJK(scK, mGi.xwk(kDW.oqX),
                               mGi.SWu(OzJ.get_subject()))
        if session_id is not None and session_id >= 0:
            self.mJK(scK, mGi.xwk(kDW.ikH),
                                   mGi.hcr(session_id))
        lhp = OzJ.lcO()
        if lhp == oYH.AWZ:
            self.mJK(scK, mGi.xwk(kDW.Znl),
                                   mGi.hcr(OzJ.zVf()))
        elif lhp == oYH.Rbt:
            self.mJK(scK, mGi.xwk(kDW.zHl),
                                   mGi.hcr(OzJ.kpt()))
            self.mJK(scK, mGi.xwk(kDW.bZd),
                                   mGi.hcr((OzJ.get_seq() + 1)))
        self.mJK(scK, mGi.xwk(kDW.BGQ),
                               mGi.hcr(self._encoding))
        scK.extend(bytes(chr(mGi.rwC), 'utf-8'))
    def uHk(self, scK, session_id, OzJ):
        scK.extend(bytes(chr(mGi.ZAi(WUY.IRf)), 'utf-8'))
        self.mJK(scK, mGi.xwk(kDW.oqX),
                               mGi.SWu(OzJ.get_subject()))
        if session_id >= 0:
            self.mJK(scK, mGi.xwk(kDW.ikH),
                                   mGi.hcr(session_id))
        self.mJK(scK, mGi.xwk(kDW.BGQ),
                               mGi.hcr(self._encoding))
        scK.extend(bytes(chr(mGi.rwC), 'utf-8'))
    def rwB(self, scK, message, session_id):
        scK.extend(bytes(chr(mGi.ZAi(WUY.Ych)), 'utf-8'))
        self.mJK(scK, mGi.xwk(kDW.oqX),
                               mGi.SWu(message.get_subject()))
        if message.is_compressed():
            Bww = self.dKt(message.get_content())
            if len(Bww) < len(message.get_content()):
                self.mJK(scK, mGi.xwk(kDW.hkG),
                                       mGi.fjR(Bww))
            else:
                self.mJK(scK, mGi.xwk(kDW.hkG),
                                       mGi.fjR(message.get_content()))
                message.set_compressed(False)
        else:
            self.mJK(scK, mGi.xwk(kDW.hkG),
                                   mGi.fjR(message.get_content()))
        if message.get_reply_to_subject() is not None:
            self.mJK(scK, mGi.xwk(kDW.AeZ),
                                   mGi.SWu(message.get_reply_to_subject()))
        if message.get_closure() is not None and len(message.get_content()) > 0:
            self.mJK(scK, mGi.xwk(kDW.GWZ),
                                   mGi.SWu(message.get_closure()))
        if session_id >= 0:
            self.mJK(scK, mGi.xwk(kDW.ikH),
                                   mGi.hcr(session_id))
        if message.is_retained() is True:
            self.mJK(scK, mGi.xwk(kDW.aeZ),
                                   mGi.hcr(1))
        else:
            self.mJK(scK, mGi.xwk(kDW.aeZ),
                                   mGi.hcr(0))
        rXq = message.get_qos()
        if rXq == QoS.GUARANTEED:
            self.mJK(scK, mGi.xwk(kDW.lXT),
                                   mGi.hcr(QoS.GUARANTEED))
        elif rXq == QoS.STANDARD:
            self.mJK(scK, mGi.xwk(kDW.lXT),
                                   mGi.hcr(QoS.STANDARD))
        if message.is_compressed():
            self.mJK(scK, mGi.xwk(kDW.Rhf),
                                   mGi.hcr(1))
        self.mJK(scK, mGi.xwk(kDW.BGQ),
                               mGi.hcr(self._encoding))
        scK.extend(bytes(chr(mGi.rwC), 'utf-8'))
    def zCg(self, scK, session_id):
        scK.extend(bytes(chr(mGi.ZAi(WUY.pyt)), 'utf-8'))
        if session_id >= 0:
            self.mJK(scK, mGi.xwk(kDW.ikH),
                                   mGi.hcr(session_id))
        self.mJK(scK, mGi.xwk(kDW.BGQ),
                               mGi.hcr(self._encoding))
        scK.extend(bytes(chr(mGi.rwC), 'utf-8'))
    def xRg(self, scK, token, session_id):
        scK.extend(bytes(chr(mGi.ZAi(WUY.tly)), 'utf-8'))
        if session_id >= 0:
            self.mJK(scK, mGi.xwk(kDW.ikH),
                                   mGi.hcr(session_id))
        self.mJK(scK, mGi.xwk(kDW.BGQ),
                               mGi.hcr(self._encoding))
        if token is not None:
            self.mJK(scK, mGi.xwk(kDW.jfs), mGi.SWu(token))
        scK.extend(bytes(chr(mGi.rwC), 'utf-8'))
    def oMW(self, scK, OzJ, VYj, epoch, session_id):
        scK.extend(bytes(chr(mGi.ZAi(WUY.PUBLISH_ACK)), 'utf-8'))
        self.mJK(scK, mGi.xwk(kDW.oqX),
                               mGi.SWu(OzJ))
        self.mJK(scK, mGi.xwk(kDW.bZd),
                               mGi.hcr(VYj))
        self.mJK(scK, mGi.xwk(kDW.zHl),
                               mGi.hcr(epoch))
        self.mJK(scK, mGi.xwk(kDW.ikH),
                               mGi.hcr(session_id))
        self.mJK(scK, mGi.xwk(kDW.BGQ),
                               mGi.hcr(self._encoding))
        scK.extend(bytes(chr(mGi.rwC), 'utf-8'))
    def mJK(self, scK, yvB, NUn):
        scK.append(yvB)
        scK.extend(NUn)
        scK.append(mGi.IDL)
    def dKt(self, tSP):
        try:
            eNc = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
            gUU = eNc.compress(tSP)
            gUU += eNc.flush()
            ckm = base64.b64encode(gUU)
        except zlib.error as ex:
            return tSP
        return ckm
    def DFI(self, NUn):
        try:
            QMJ = base64.b64decode(NUn)
            if not QMJ:
                return NUn
            JSk = zlib.decompress(QMJ, -15)
        except base64.binascii.Error as ex:
            return NUn
        except zlib.error as ex:
            return NUn
        return JSk
import socket
import ssl
class FTk:
    @staticmethod
    def wgy(host, mdu, encryption, socket_timeout_seconds):
        ZqH = None
        if encryption is False:
            ZqH = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ZqH.settimeout(socket_timeout_seconds)
            ZqH.connect((host, mdu))
        else:
            bqJ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            bqJ.settimeout(socket_timeout_seconds)
            try:
                Nzr = ssl.create_default_context()
                ZqH = Nzr.wrap_socket(bqJ, server_hostname=host)
            except Exception as tcU: print(tcU)
            ZqH.connect((host, mdu))
        return ZqH
class NOh:
    IsN = 80
    BQh = 443
    Qmy = 100
    def __init__(self, address, encryption):
        self._weight = NOh.Qmy
        self._unparsed_address = address
        AYq = address.find(' ')
        if AYq != -1:
            self._weight = int(address[0:AYq])
            if self._weight < 0 or self._weight > 100:
                raise ValueError(
                    "The Weight of a clust Member must be between 0 and 100, Weight: " + str(self._weight))
        cUX = address.find(']')
        tvc = address.rfind(":")
        yXj = None
        mdu = None
        if tvc != -1 and tvc + 1 < len(address) and tvc >= cUX:
            yXj = address[0:tvc]
            mdu = int(address[tvc + 1:])
        else:
            yXj = address
            if encryption:
                mdu = self.BQh
            else:
                mdu = self.IsN
        if mdu < 0 or mdu > 65535:
            raise ValueError("Invalid Port number")
        if yXj == "":
            raise ValueError("Clust Member with null address")
        if yXj == "*":
            raise ValueError("Wildcard address (*) cannot be used to define a clust Member")
        self._address = yXj
        self._port = mdu
    def ULW(self):
        return self._weight
    def bbk(self):
        return self._port
    def gGk(self):
        return self._address
    def jon(self, IGe):
        if (self._address == IGe._address):
            if self._port == IGe._port:
                return True
        return False
    def JFG(self):
        return self._unparsed_address
    def __repr__(self) -> str:
        pYk = "[Host="
        pYk += str(self.gGk())
        pYk += ", Port="
        pYk += str(self.bbk())
        pYk += "]"
        return pYk
import random
class WFl:
    def __init__(self, servers, encryption):
        self._members = []
        self._inactive_members = []
        self._current_member = None
        for cUX in range(0, len(servers)):
            self._members.append(NOh(servers[cUX], encryption))
    def avM(self):
        Mdf = self.RUd()
        if len(Mdf) == 0:
            self._inactive_members = []
            Mdf = list(self._members)
        DrI = self.cib(Mdf)
        self._current_member = Mdf[DrI]
        return self._current_member
    def RUd(self):
        Mdf = list(self._members)
        for oNG in self._members:
            for IyA in self._inactive_members:
                if oNG.jon(IyA):
                    Mdf.remove(oNG)
        return Mdf
    def cib(self, Mdf):
        DrI = -1
        pmk = 0
        for oNG in Mdf:
            pmk = pmk + oNG.ULW()
        if pmk == 0:
            DrI = int(len(Mdf) * random.uniform(0, 1))
        else:
            cLH = int(pmk * random.uniform(0, 1))
            pmk = 0
            for cUX in range(0 < len(Mdf)):
                pmk = pmk + Mdf[cUX].ULW()
                if pmk > cLH:
                    DrI = cUX
                    break
        return DrI
    def JPk(self):
        return self._current_member
    def ABf(self, IGe):
        self._inactive_members.append(IGe)
import threading
class AML:
    xGO = 0
    ypG = 1
class Kke:
    def __init__(self):
        self._state = AML.xGO
        self._lock = threading.Lock()
    def lOq(self, state):
        with self._lock:
            self._state = state
    def szt(self):
        with self._lock:
            return self._state
class EKF:
    @staticmethod
    def search(NUn, dataLength, pattern, patternLength):
        BGm = [0] * patternLength
        tvc = 0
        len = 0
        cUX = 1
        while cUX < patternLength:
            if pattern[cUX] == pattern[len]:
                len += 1
                BGm[cUX] = len
                cUX += 1
            else:
                if len != 0:
                    len = BGm[len - 1]
                else:
                    BGm[cUX] = 0
                    cUX += 1
        cUX = 0
        while cUX < dataLength:
            if pattern[tvc] == NUn[cUX]:
                cUX += 1
                tvc += 1
            if tvc == patternLength:
                return cUX - tvc
            elif cUX < dataLength and pattern[tvc] != NUn[cUX]:
                if tvc != 0:
                    tvc = BGm[tvc - 1]
                else:
                    cUX += 1
        return -1
import abc
class RPR(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def DnJ(self, bow):
        pass
import abc
class sdO(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def nQl(self, bow):
        pass
    @abc.abstractmethod
    def NZY(self):
        pass
import abc
class OmM(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def MFe(self, status, info):
        pass
    @abc.abstractmethod
    def bjQ(self, message):
        pass
import abc
class WUH(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def yHX(self, DMp, connection, keep_alive):
        pass
    @abc.abstractmethod
    def gBI(self, DMp, connection, disconnect_info):
        pass
    @abc.abstractmethod
    def bab(self, connection):
        pass
    @abc.abstractmethod
    def cancel(self):
        pass
    @abc.abstractmethod
    def wAP(self, value):
        pass
class ioF(MigratoryDataMessage):
    def __init__(self, _subject, _content, closure, retained, _message_type, qos_, _reply_subject, _compression):
        super().__init__(_subject, _content, closure)
        self._retained = retained
        self._message_type = _message_type
        self.wLy = qos_
        self._reply_to_subject = _reply_subject
        self._compression = _compression
    def nPZ(self, VYj):
        self._seq = VYj
    def BhN(self, epoch):
        self._epoch = epoch
class UcV:
    def __init__(self, IOJ, status, info, migratory_data_message):
        self.IOJ = IOJ
        self.status = status
        self.info = info
        self.migratory_data_message = migratory_data_message
class NcR:
    mYL = 0
    hvz = 1
class JDV:
    CIe = 1,
    zCD = 2,
    aVG = 3,
    xbn = 4,
    IRI = 5,
    IRf = 6,
    xGO = 7,
    cRk = 8,
    UOb = 9,
    tWS = 10,
    iYv = 11,
    fsh = 12,
    tly = 13
class omM:
    def __init__(self, operation):
        self.operation = operation
        self.connection_uuid = None
        self.disconnect_reason = None
        self.Gse = None
        self.history = None
        self.md_message = None
        self.message = None
        self.info = None
    @staticmethod
    def vMS():
        return omM(JDV.CIe)
    @staticmethod
    def JyK(Gse, history):
        bow = omM(JDV.IRI)
        bow.Gse = Gse
        bow.history = history
        return bow
    @staticmethod
    def ePL():
        bow = omM(JDV.tly)
        return bow
    @staticmethod
    def ZuX(Gse):
        bow = omM(JDV.IRf)
        bow.Gse = Gse
        return bow
    @staticmethod
    def SKw(message):
        bow = omM(JDV.iYv)
        bow.md_message = message
        return bow
    @staticmethod
    def Sbi(message):
        bow = omM(JDV.tWS)
        bow.message = message
        return bow
    @staticmethod
    def vZj(uuid, disconnect_reason):
        bow = omM(JDV.xGO)
        bow.connection_uuid = uuid
        bow.disconnect_reason = disconnect_reason
        return bow
    @staticmethod
    def vkb(disconnect_info):
        bow = omM(JDV.UOb)
        bow.info = disconnect_info
        return bow
    @staticmethod
    def Ets():
        bow = omM(JDV.cRk)
        return bow
    @staticmethod
    def Jjl():
        bow = omM(JDV.zCD)
        return bow
    @staticmethod
    def Aap():
        bow = omM(JDV.xbn)
        return bow
    @staticmethod
    def sdv():
        bow = omM(JDV.aVG)
        return bow
    @staticmethod
    def rDE():
        bow = omM(JDV.fsh)
        return bow
import re
class IXx:
    jkl = 0
    QKg = 1
    Kdf = 2
class ePo:
    uPO = "OK"
    mWB = "DENY"
    Glg = "connection_active_close_keep_alive"
    XVc = "connection_active_close_seq_higher"
    DMb = "connection_passive_close"
    LLU = "connection_error"
    fPH = "cache_ok"
    lxR = "cache_ok_no_new_message"
    gqj = "cache_ok_new_epoch"
    Fra = "end"
    jAY = "^\/([^\/]+\/)*([^\/]+|\*)$"
    @staticmethod
    def GYQ(ZFB):
        if not isinstance(ZFB, str):
            return False
        afy = re.compile(ePo.jAY)
        if afy.search(ZFB) is not None:
            return True
        return False
    @staticmethod
    def peU(Gse):
        Zmn = []
        for OzJ in Gse:
            if OzJ is not None and ePo.GYQ(OzJ):
                Zmn.append(OzJ)
        return Zmn
    @staticmethod
    def HqS(SNo, recv_seq, recv_seq_id, listener_notifier, logger):
        if SNo.kpt() != recv_seq_id:
            SNo.nPZ(recv_seq)
            SNo.Lrx(recv_seq_id)
            return IXx.jkl
        if recv_seq <= SNo.get_seq():
            return IXx.QKg
        if recv_seq == SNo.get_seq() + 1:
            if SNo.ytv() == oYH.Rbt:
                SNo.fGY()
                listener_notifier.MFe(MigratoryDataClient.NOTIFY_DATA_SYNC, SNo.get_subject())
                logger.debug(str(NWM.Tow) + str(
                    MigratoryDataClient.NOTIFY_DATA_SYNC) + str(SNo))
            SNo.nPZ(SNo.get_seq() + 1)
            return IXx.jkl
        if SNo.iHb() > 0:
            logger.info("Missing Messages: expected message with sequence number: " + str(
                SNo.get_seq() + 1) + ", received instead message with sequence number:  " + str(recv_seq) + " !")
            return IXx.Kdf
        logger.info("Reset sequence: '" + str(SNo.get_seq() + 1) + "'. The new sequence is: '" + str(recv_seq) + "' !")
        SNo.nPZ(recv_seq)
        listener_notifier.MFe(MigratoryDataClient.NOTIFY_DATA_RESYNC, SNo.get_subject())
        logger.debug(
            NWM.Tow + MigratoryDataClient.NOTIFY_DATA_RESYNC + str(SNo))
        return IXx.jkl
    @staticmethod
    def Gbf(SNo, recv_seq, recv_seq_id, listener_notifier, logger):
        if SNo.kpt() != recv_seq_id:
            SNo.nPZ(recv_seq)
            SNo.Lrx(recv_seq_id)
            return IXx.jkl
        if recv_seq <= SNo.get_seq():
            return IXx.QKg
        if SNo.ytv() == oYH.Rbt:
            SNo.fGY()
        SNo.nPZ(recv_seq)
        return IXx.jkl
import threading
class KZh:
    def __init__(self):
        self._subject_table = {}
        self._empty_subject = neA("", 0)
        self._lock = threading.Lock()
    def cSB(self, Gse, history):
        with self._lock:
            for OzJ in Gse:
                UCh = self._subject_table.get(OzJ)
                if UCh is None:
                    self._subject_table[OzJ] = neA(OzJ, history)
    def WYy(self, Gse):
        with self._lock:
            qHh = []
            for OzJ in Gse:
                UCh = self._subject_table.get(OzJ)
                if UCh is not None:
                    try:
                        del self._subject_table[OzJ]
                        qHh.append(UCh)
                    except KeyError:
                        pass
            return qHh
    def kUv(self):
        with self._lock:
            return self._subject_table.keys()
    def get_subject(self, OzJ):
        with self._lock:
            return self._subject_table.get(OzJ)
    def OPK(self, OzJ):
        with self._lock:
            ZNY = self._subject_table.get(OzJ)
            if ZNY is None:
                return False
            else:
                return True
    def EiW(self):
        with self._lock:
            return self._empty_subject
    def Fzp(self):
        with self._lock:
            for pAK in self._subject_table:
                self._subject_table[pAK].JfS()
import threading
import queue
import time
class Kag(sdO, threading.Thread):
    def __init__(self, JRp, logger):
        threading.Thread.__init__(self)
        self._logger = logger
        self._event_handler = JRp
        self._control_queue = queue.Queue()
        self._running = itA(True)
    def run(self):
        while self._running.jOA():
            self.clg()
        self._event_handler.DnJ(omM.Jjl())
        self._logger.debug("Exit single_thread_event_loop thread")
    def nQl(self, bow):
        if self._running.jOA():
            self._control_queue.put(bow)
    def clg(self):
        try:
            CbL = self._control_queue.get(True, 0.1)
            if CbL is not None:
                self._event_handler.DnJ(CbL)
        except queue.Empty:
            pass
    def NZY(self):
        self._running.NJq(False)
class EfR:
    @staticmethod
    def GAt(qOm, kMb):
        aXg = MQT(-1, -1)
        if kMb == len(qOm.scK):
            return aXg
        qvv = kMb
        rck = 2
        gLt = 0
        IWn = 0
        eah = len(qOm.scK) - qvv
        if eah < rck:
            return aXg
        b = qOm.scK[qvv]
        XNK = (b >> 7) & 0x01
        QIJ = b & 0x40
        pji = b & 0x20
        LIw = b & 0x10
        if XNK != 1 or QIJ != 0 or pji != 0 or LIw != 0:
            return aXg
        qvv += 1
        b = qOm.scK[qvv]
        ahs = b & 0x7F
        if ahs < 126:
            IWn = 0
            gLt = ahs
        elif ahs == 126:
            IWn = 2
            if eah < rck + IWn:
                return aXg
            Lxo = bytearray()
            for cUX in range(qvv + 1, qvv + 1 + IWn):
                Lxo.extend([qOm.scK[cUX]])
            gLt = EfR.Qxr(Lxo)
            qvv += IWn
        elif ahs == 127:
            IWn = 8
            if eah < rck + IWn:
                return aXg
            Lxo = bytearray()
            for cUX in range(qvv + 1, qvv + 1 + IWn):
                Lxo.extend([qOm.scK[cUX]])
            gLt = EfR.Qxr(Lxo)
            qvv += IWn
        if eah < (rck + IWn + gLt):
            return aXg
        qvv += 1
        return MQT(qvv, qvv + gLt)
    @staticmethod
    def Qxr(NUn):
        if len(NUn) == 2:
            return ((NUn[0] & 0xFF) << 8) | (NUn[1] & 0xFF)
        else:
            return ((NUn[4] & 0x7F) << 24) | ((NUn[5] & 0xFF) << 16) | ((NUn[6] & 0xFF) << 8) | (NUn[7] & 0xFF)
import re
class bFh:
    @staticmethod
    def KBg(qOm, logger):
        NZC = qOm.qvv
        if qOm.scK[NZC] == 72:
            NZC = bFh.srK(qOm)
        if NZC == -1:
            return []
        qOm.kMb(NZC)
        iGe = []
        while True:
            if NZC >= len(qOm.scK):
                return iGe
            if qOm.scK[NZC] == mGi.sMB:
                NZC += 1
            else:
                try:
                    MIx = EfR.GAt(qOm, NZC)
                except IndexError:
                    MIx = MQT(-1, -1)
                ZyP = MIx.UOp()
                aOB = MIx.FWA()
                if ZyP == -1:
                    return iGe
                while True:
                    cUX = bFh.GVp(qOm, ZyP, aOB, mGi.rwC)
                    if cUX == -1:
                        break
                    lGN = bFh.hzy(qOm, ZyP + 1, cUX, logger)
                    if lGN is not None:
                        message = ICX(mGi.sKU[qOm.scK[ZyP]], lGN)
                        iGe.append(message)
                    ZyP = cUX + 1
                    qOm.kMb(ZyP)
                NZC = qOm.qvv
    @staticmethod
    def jXW(qOm, logger):
        qvv = bFh.mEX(qOm)
        if qvv == -1:
            return []
        qOm.kMb(qvv)
        iGe = []
        while True:
            cUX = bFh.GVp(qOm, qvv, len(qOm.scK), mGi.rwC)
            if cUX == -1:
                break
            if qOm.scK[qvv] == 72:
                iGe.extend(bFh.jXW(qOm, logger))
                break
            lGN = bFh.hzy(qOm, qvv + 1, cUX, logger)
            if lGN is not None:
                message = ICX(mGi.sKU[qOm.scK[qvv]], lGN)
                iGe.append(message)
            qvv = cUX + 1
            qOm.kMb(qvv)
        return iGe
    @staticmethod
    def mEX(qOm):
        qvv = qOm.qvv
        if qOm.scK[qvv] == 72:
            pby = "\r\n\r\n".encode("utf-8")
            nMy = EKF.search(qOm.scK[qvv:], len(qOm.scK), pby,
                                                   len(pby))
            if nMy != -1:
                qvv += nMy + len(pby)
                qOm.kMb(qvv)
            else:
                return -1
        return qvv
    @staticmethod
    def srK(qOm):
        pby = "\r\n\r\n".encode("utf-8")
        qvv = qOm.qvv
        cUX = EKF.search(qOm.scK[qvv:], len(qOm.scK), pby,
                             len(pby))
        if cUX == -1:
            return -1
        qvv = cUX + len(pby)
        return qvv
    @staticmethod
    def GVp(qOm, start, end, value):
        for cUX in range(start, end):
            if qOm.scK[cUX] == value:
                return cUX
        return -1
    @staticmethod
    def hzy(qOm, start, end, logger):
        lGN = None
        while True:
            if start >= end:
                break
            GyM = qOm.scK[start]
            VER = bFh.GVp(qOm, start + 1, end, mGi.IDL)
            if VER == -1:
                logger.trace(
                    "Received an invalid msg: Hdr end missing - msg ignored, Hdr Position: " + str(
                        start) + ", " + str(qOm.scK[start:end]))
                return None
            yvB = mGi.Byf(GyM)
            if yvB is None:
                logger.trace("Received an unknown Hdr - Hdr ignored, Hdr Position: " + str(qOm.scK))
                start = VER + 1
            start = start + 1
            if lGN is None:
                lGN = {}
            value = None
            ScZ = mGi.YnD(yvB)
            JnQ = qOm.scK[start:VER]
            if ScZ == MzE.YMx:
                value = mGi.HDS(JnQ)
            elif ScZ == MzE.lJf:
                NYd = mGi.vAI(JnQ)
                value = NYd.decode('utf-8')
            elif ScZ == MzE.TmD:
                value = mGi.vAI(JnQ)
            elif ScZ == MzE.gys:
                value = JnQ
            UgJ = lGN.get(yvB)
            if UgJ is None:
                lGN[yvB] = value
            else:
                values = [UgJ, value]
                lGN[yvB] = values
            start = VER + 1
        return lGN
import threading
import queue
class Nwr(OmM, threading.Thread):
    def __init__(self, listener):
        super().__init__()
        self._queue = queue.Queue()
        self._run = True
        self._migratory_data_listener = listener
    def MFe(self, status, info):
        self._queue.put(UcV(NcR.mYL, status, info, None))
    def bjQ(self, message):
        self._queue.put(UcV(NcR.hvz, None, None, message))
    def run(self):
        while self._run:
            try:
                DEF = self._queue.get(True, 0.1)
                if self._migratory_data_listener is not None:
                    if DEF.IOJ == NcR.mYL:
                        self._migratory_data_listener.on_status(DEF.status, DEF.info)
                    elif DEF.IOJ == NcR.hvz:
                        self._migratory_data_listener.on_message(DEF.migratory_data_message)
            except queue.Empty:
                pass
    def EZz(self):
        self._run = False
import socket
import uuid
import threading
class Ral:
    CIe = 0
    ely = 1
class jYX:
    qUo = 0
    xbn = 1
    DfN = 2
class TVH:
    jnL = 0
    pBJ = 1
    xXH = 2
class Connection:
    def __init__(self, configuration, listener_notifier, Ecy, WzD, client_state, logger):
        self._lock = threading.Lock()
        self._reconnect_retries = 0
        self._session = -1
        self._socket = None
        self._reader = None
        self._writer = None
        self._reconnected = False
        self._session_received = False
        self._loop = None
        self._listener_notifier = None
        self._servers_down_count = 0
        self._is_server_down = False
        self._max_message_size = None
        self._publish_closures = []
        self._current_connection_id = None
        self._app_state = jYX.DfN
        self._node_type = TVH.jnL
        self._subject_manager = KZh()
        self._logger = logger
        self._configuration = configuration
        self._listener_notifier = listener_notifier
        self._cluster = Ecy
        self._scheduler = WzD
        self._client_state = client_state
        self._push_encoder = sMm()
        self._transport_type = self._configuration.trans_type
        if self._transport_type == pNL.HTTP:
            self._transport_encoder = qIy()
            self._push_encoder.MPg()
        else:
            self._transport_encoder = IhQ()
        self._message_listener = QjI()
        self._message_listener.JDJ(self)
        self._cluster_token = None
    def Zdo(self):
        return self._message_listener
    def kOr(self, qOm):
        iGe = None
        if self._transport_type == pNL.AKZ:
            iGe = bFh.KBg(qOm, self._logger)
        else:
            iGe = bFh.jXW(qOm, self._logger)
        if len(iGe) > 0:
            self.cjM(iGe)
        else:
            self._loop.nQl(omM.rDE())
            self._logger.debug(str(NWM.tTw))
    def cjM(self, iGe):
        for cUX in range(0, len(iGe)):
            message = iGe[cUX]
            if message.operation == WUY.CLIENT_PUBLISH_RESPONSE or message.operation == WUY.iYv or message.operation == WUY.ufk or message.operation == WUY.GHC \
                    or message.operation == WUY.IRI or message.operation == WUY.IRf or message.operation == WUY.CIe or message.operation == WUY.oVM:
                self._loop.nQl(omM.Sbi(message))
                self._logger.debug(NWM.UUl + str(message))
            elif message.operation == WUY.pyt:
                self._loop.nQl(omM.rDE())
                self._logger.debug(str(NWM.tTw))
            elif message.operation == WUY.Ych:
                break
            else:
                self._logger.warn("No existing operation for msg: " + str(message))
    def connect(self):
        DMp = uuid.uuid4()
        self.QaU(DMp)
        if self._socket is not None:
            self.disconnect()
        try:
            IGe = self._cluster.avM()
            self._logger.info("Connecting to the clust Member: " + str(self._cluster.JPk()))
            self._socket = FTk.wgy(IGe.gGk(), IGe.bbk(),
                                                    self._configuration.encryption,
                                                    self._configuration.socket_timeout_seconds)
            self._writer = xqG(self._socket)
            self._writer.start()
            self._reader = niY(self._socket, self, DMp)
            self._reader.start()
            qOm = self._transport_encoder.gXx(self._cluster.JPk().gGk(),
                                                                  self._configuration.encryption)
            if len(qOm.scK) > 0:
                self._writer.cBR(qOm.scK)
        except:
            self._logger.info("Failed to Connect: " + str(self._cluster.JPk()))
            self._scheduler.gBI(DMp, self, ePo.LLU)
            return
        self._scheduler.yHX(DMp, self, Ral.CIe)
        self._scheduler.bab(self)
        self.oaE()
    def oaE(self):
        qOm = self._transport_encoder.PlX(self._cluster.JPk().gGk())
        qoc = self._configuration
        self._push_encoder.eph(qOm.scK, qoc.entitlement_token, qoc.session_type, qoc.user_agent, qoc.NCS)
        self._transport_encoder.zRT(qOm)
        self._write(qOm.dKt())
    def fvc(self):
        self.disconnect()
        if self._app_state == jYX.qUo:
            return
        self._cluster.ABf(self._cluster.JPk())
        self._reconnected = True
        self.connect()
    def disconnect(self):
        if self._socket is not None:
            self._socket.close()
        if self._writer is not None:
            self._writer.EZz()
        if self._reader is not None:
            self._reader.EZz()
        self._socket = None
        self._writer = None
        self._reader = None
        self._scheduler.cancel()
        self.keC()
    def NWn(self):
        self._app_state = jYX.qUo
        self.disconnect()
    def keC(self):
        self._client_state.lOq(AML.xGO)
        self._session = -1
        self._session_received = False
    def QVm(self):
        if self._app_state != jYX.DfN:
            return
        self._logger.info("Call pause")
        self._app_state = jYX.xbn
        self.disconnect()
    def resume(self):
        if self._app_state != jYX.xbn:
            return
        self._logger.info("Call resume")
        self._app_state = jYX.DfN
        self.uIn()
        self.fvc()
    def subscribe(self, Gse, history):
        if Gse is None or len(Gse) == 0:
            return
        Gse = ePo.peU(Gse)
        LzR = list(set(Gse) - set(self._subject_manager.kUv()))
        if len(LzR) == 0:
            return
        self._subject_manager.cSB(LzR, history)
        if self._client_state.szt() == AML.ypG:
            self.Dcs(LzR)
    def Dcs(self, subjects_string):
        qOm = self._transport_encoder.PlX(self._cluster.JPk().gGk())
        for OzJ in subjects_string:
            self.UGJ(qOm, self._subject_manager.get_subject(OzJ))
        self._transport_encoder.zRT(qOm)
        self._write(qOm.dKt())
    def _write(self, message):
        if self._writer is not None:
            self._writer.cBR(message)
            try:
                self._logger.debug(NWM.Mvc + message.decode('utf-8'))
            except UnicodeDecodeError:
                self._logger.debug(NWM.Mvc + str(message))
    def UGJ(self, qOm, OzJ):
        self._push_encoder.Ygn(qOm.scK, OzJ, self._session)
    def unsubscribe(self, subjects_string):
        if subjects_string is None or len(subjects_string) == 0:
            return
        cLl = list(set(subjects_string) & set(self._subject_manager.kUv()))
        if len(cLl) == 0:
            return
        qHh = self._subject_manager.WYy(cLl)
        if self._client_state.szt() == AML.ypG:
            self.MIv(qHh)
    def MIv(self, Gse):
        qOm = self._transport_encoder.PlX(self._cluster.JPk().gGk())
        for OzJ in Gse:
            self._push_encoder.uHk(qOm.scK, self._session, OzJ)
        self._transport_encoder.zRT(qOm)
        self._write(qOm.dKt())
    def publish(self, message):
        if self._client_state.szt() != AML.ypG:
            self.PbO(MigratoryDataClient.NOTIFY_PUBLISH_FAILED, message)
        self.peY(message)
    def peY(self, message):
        dQa = message.get_reply_to_subject()
        if dQa is not None and ePo.GYQ(
                dQa) is True and self._subject_manager.OPK(dQa) is False:
            self.subscribe([dQa], 0)
        qOm = self._transport_encoder.PlX(self._cluster.JPk().gGk())
        self._push_encoder.rwB(qOm.scK, message, self._session)
        self._transport_encoder.zRT(qOm)
        if self._max_message_size is not None and (len(qOm.scK) - qOm.qvv) > self._max_message_size:
            self.PbO(MigratoryDataClient.NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED, message)
            return
        closure = message.get_closure()
        if closure is not None and len(closure) > 0:
            self._publish_closures.append(closure)
        self._write(qOm.dKt())
    def JeB(self):
        for closure in self._publish_closures:
            self._listener_notifier.MFe(MigratoryDataClient.NOTIFY_PUBLISH_FAILED, closure)
        self._publish_closures = []
    def PbO(self, notification, message):
        if message is not None and message.get_closure() is not None:
            self._listener_notifier.MFe(notification, message.get_closure())
    def mOV(self):
        qOm = self._transport_encoder.PlX(self._cluster.JPk().gGk())
        self._push_encoder.zCg(qOm.scK, self._session)
        self._transport_encoder.zRT(qOm)
        if self._writer is not None:
            self._write(qOm.dKt())
    def wUN(self):
        qOm = self._transport_encoder.PlX(self._cluster.JPk().gGk())
        self._push_encoder.xRg(qOm.scK, self._configuration.entitlement_token, self._session)
        self._transport_encoder.zRT(qOm)
        if self._writer is not None:
            self._write(qOm.dKt())
    def gBI(self, uuid, disconnect_reason, from_):
        if uuid == self.xNp():
            self._client_state.lOq(AML.xGO)
            self._loop.nQl(omM.vZj(uuid, disconnect_reason))
            self._logger.debug(
                NWM.IZI + str(self._current_connection_id) + str(from_))
    def VrA(self, disconnect_info):
        self._logger.error("[" + str(disconnect_info) + "] [" + str(self._cluster.JPk()) + "]")
        self._logger.info("Lost connection with the clust Member: " + str(self._cluster.JPk()))
        if self._session_received is False:
            self._servers_down_count += 1
            if self._is_server_down is False:
                if self._servers_down_count >= self._configuration.servers_down_before_notify:
                    self._is_server_down = True
                    self._listener_notifier.MFe(MigratoryDataClient.NOTIFY_SERVER_DOWN,
                                                         self._cluster.JPk().JFG())
                    self._logger.debug(NWM.cQS + str(disconnect_info))
    def uIn(self):
        self._is_server_down = False
        self._servers_down_count = 0
    def Yek(self):
        self._logger.info("Connected to the clust Member: " + str(self._cluster.JPk()))
        self.uIn()
        self._listener_notifier.MFe(MigratoryDataClient.NOTIFY_SERVER_UP,
                                             self._cluster.JPk().JFG())
        self._logger.debug(NWM.plL + MigratoryDataClient.NOTIFY_SERVER_UP + str(
            self.xNp()))
    def uVR(self):
        return self._reconnect_retries
    def hbX(self):
        self._reconnect_retries += 1
        return self._reconnect_retries
    def QaU(self, DMp):
        with self._lock:
            self._current_connection_id = DMp
    def xNp(self):
        with self._lock:
            return self._current_connection_id
    def GqO(self, loop):
        self._loop = loop
    def RzF(self):
        return self._loop
    def BrZ(self):
        return self._app_state
class QjI:
    def __init__(self):
        self._connection = None
    def JDJ(self, connection):
        self._connection = connection
    def on_message(self, message):
        self._connection._scheduler.yHX(self._connection.xNp(),
                                                                   self._connection, Ral.ely)
        
        lGN = message.lGN
        if message.operation == WUY.IRI:
            self.twS(lGN)
        elif message.operation == WUY.iYv:
            self.wuo(lGN, message)
        elif message.operation == WUY.CIe:
            self.irK(lGN)
        elif message.operation == WUY.CLIENT_PUBLISH_RESPONSE:
            self.fkR(lGN)
        elif message.operation == WUY.IRf:
            self.yhP()
        elif message.operation == WUY.ufk:
            self.FwT(lGN)
        elif message.operation == WUY.GHC:
            self.FBq(lGN)
        elif message.operation == WUY.oVM:
            self.xMY(lGN)
        else:
            self._connection._logger.warn("No existing operation for msg: " + str(message))
    def irK(self, lGN):
        dXK = lGN.get(kDW.ikH)
        if dXK is not None:
            self._connection.Yek()
            self._connection._session = dXK
            self._connection._session_received = True
            self._connection._reconnect_retries = 0
            OCa = lGN.get(kDW.GvT)
            if OCa is not None and OCa == 1:
                self._connection._node_type = TVH.pBJ
            if OCa is not None and OCa == 2:
                self._connection._node_type = TVH.xXH
            hHW = lGN.get(kDW.Vqk)
            if hHW is not None:
                self._connection._scheduler.wAP(hHW)
                self._connection._scheduler.yHX(
                    self._connection.xNp(), self._connection, Ral.ely)
            self._connection._client_state.lOq(AML.ypG)
            UXd = lGN.get(kDW.JLy)
            self.PKP(UXd)
            EtP = lGN.get(kDW.xbr)
            if EtP is not None:
                self._connection._max_message_size = EtP
            NAf = lGN.get(kDW.HKe)
            error = lGN.get(kDW.ERROR)
            if (error is not None and error == xjU.kkU):
                self._connection._listener_notifier.MFe(MigratoryDataClient.YrN, NAf if NAf != None else "")
            else:
                self._connection._listener_notifier.MFe(MigratoryDataClient.qWn, NAf if NAf != None else "")
            Gse = self._connection._subject_manager.kUv()
            if len(Gse) > 0:
                self._connection.Dcs(Gse)
    def twS(self, lGN):
        pass
    def yhP(self):
        pass
    def wuo(self, lGN, msg):
        OzJ = lGN.get(kDW.oqX)
        SNo = self._connection._subject_manager.get_subject(OzJ)
        if SNo is None:
            return
        UXd = lGN.get(kDW.JLy)
        self.PKP(UXd)
        NUn = lGN.get(kDW.hkG)
        closure = lGN.get(kDW.GWZ)
        retained = False
        BbN = lGN.get(kDW.aeZ)
        if BbN is not None and BbN == 1:
            retained = True
        jFq = False
        tqC = lGN.get(kDW.Rhf)
        if tqC is not None and tqC == 1:
            jFq = True
        if jFq == True:
            NUn = self._connection._push_encoder.DFI(NUn)
        iUk = MessageType.UPDATE
        IOJ = lGN.get(kDW.TUh)
        if IOJ is not None:
            if IOJ == yIi.SNAPSHOT:
                iUk = MessageType.SNAPSHOT
            elif IOJ == yIi.RECOVERED:
                iUk = MessageType.RECOVERED
            elif IOJ == yIi.HISTORICAL:
                iUk = MessageType.HISTORICAL
        wLy = QoS.GUARANTEED
        eTv = lGN.get(kDW.lXT)
        if eTv is not None and eTv == QoS.STANDARD:
            wLy = QoS.STANDARD
        if self._connection._node_type == TVH.pBJ and wLy == QoS.GUARANTEED:
            message = ioF(OzJ, NUn, closure, retained, iUk, QoS.GUARANTEED,
                                                   lGN.get(kDW.AeZ), jFq)
            VYj = lGN.get(kDW.bZd)
            QQw = lGN.get(kDW.zHl)
            message.nPZ(VYj)
            message.BhN(QQw)
            QJk = ePo.HqS(SNo, VYj, QQw, self._connection._listener_notifier,
                                             self._connection._logger)
            if QJk == IXx.jkl:
                self._connection._listener_notifier.bjQ(message)
                self._connection._logger.debug(NWM.Tow + str(message))
            elif QJk == IXx.Kdf:
                self._connection.gBI(self._connection.xNp(),
                                           ePo.XVc, "seq_higher")
        elif self._connection._node_type == TVH.xXH and wLy == QoS.GUARANTEED:
            message = ioF(OzJ, NUn, closure, retained, iUk, QoS.GUARANTEED,
                                                   lGN.get(kDW.AeZ), jFq)
            VYj = lGN.get(kDW.bZd)
            QQw = lGN.get(kDW.zHl)
            message.nPZ(VYj)
            message.BhN(QQw)
            QJk = ePo.Gbf(SNo, VYj, QQw, self._connection._listener_notifier,
                                             self._connection._logger)
            if QJk == IXx.jkl:
                self._connection._listener_notifier.bjQ(message)
                self._connection._logger.debug(NWM.Tow + str(message))
        else:
            message = ioF(OzJ, NUn, closure, retained, iUk, QoS.STANDARD,
                                                   lGN.get(kDW.AeZ), jFq)
            self._connection._listener_notifier.bjQ(message)
            self._connection._logger.debug(NWM.Tow + str(message))
    def fkR(self, lGN):
        if lGN is None:
            return
        closure = lGN.get(kDW.GWZ)
        xvH = lGN.get(kDW.HKe)
        if closure is not None and xvH is not None:
            status = MigratoryDataClient.NOTIFY_PUBLISH_FAILED
            if xvH == ePo.mWB:
                status = MigratoryDataClient.NOTIFY_PUBLISH_DENIED
            elif xvH == ePo.uPO:
                status = MigratoryDataClient.NOTIFY_PUBLISH_OK
            self._connection._listener_notifier.MFe(status, closure)
            self._connection._logger.debug(
                NWM.cEZ + str(status) + str(closure))
            if self._connection._publish_closures.__contains__(closure):
                self._connection._publish_closures.remove(closure)
    def FwT(self, lGN):
        BbM = lGN.get(kDW.HKe)
        OzJ = lGN.get(kDW.oqX)
        if BbM is not None and OzJ is not None:
            lBU = True
            XOr = MigratoryDataClient.NOTIFY_SUBSCRIBE_DENY
            if BbM == XUH.gsR:
                XOr = MigratoryDataClient.NOTIFY_SUBSCRIBE_ALLOW
                lBU = False
            elif BbM == XUH.TUy:
                XOr = MigratoryDataClient.NOTIFY_SUBSCRIBE_DENY
            if lBU is True:
                self._connection._subject_manager.WYy([OzJ])
            self._connection._listener_notifier.MFe(XOr, OzJ)
            self._connection._logger.debug(NWM.CzO + str(
                OzJ + str(BbM) + str(XOr)))
    def FBq(self, lGN):
        OzJ = lGN.get(kDW.oqX)
        status = lGN.get(kDW.TUh)
        self._connection._logger.info("Recovery Status for subj: " + str(OzJ) + " is:" + str(status))
        if ePo.Fra == status:
            Gse = self._connection._subject_manager.kUv()
            for s in Gse:
                SNo = self._connection._subject_manager.get_subject(s)
                FAI = SNo.YeV()
                if ePo.fPH == FAI or ePo.gqj == FAI or ePo.lxR == FAI:
                    SNo.XQa()
                else:
                    SNo.AIP()
        else:
            SNo = self._connection._subject_manager.get_subject(OzJ)
            if SNo is not None:
                SNo.ywx(status)
    def xMY(self, lGN):
        status = lGN.get(kDW.HKe)
        info = lGN.get(kDW.jfs)
        self._connection._listener_notifier.MFe(status, info)
    def PKP(self, _received_cluster_token):
        if _received_cluster_token is not None:
            if self._connection._cluster_token is None:
                self._connection._cluster_token = _received_cluster_token
            else:
                if _received_cluster_token != self._connection._cluster_token:
                    self._connection._cluster_token = _received_cluster_token
                    self._connection._subject_manager.Fzp()
import uuid
class pNL:
    HTTP = 0
    AKZ = 1
class IAR:
    def __init__(self, session_type, user_agent):
        self.NCS = 6
        self.id = str(uuid.uuid4())
        self.session_type = session_type
        self.user_agent = user_agent + ", version:" + str(self.NCS)
        self.DEFAULT_KEEP_ALIVE_TIMEOUT = 30
        self.PING_INTERVAL = 900
        self.OPERATION_TIMEOUT_INTERVAL = 10
        self.reconnect_policy = MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF
        self.reconnect_time_interval = 20
        self.reconnect_max_delay = 360
        self.quick_reconnect_max_retries = 3
        self.quick_reconnect_initial_delay = 5
        self.servers_down_before_notify = 1
        self.entitlement_token = None
        self.encryption = False
        self.socket_timeout_seconds = 2
        self._subjects = {}
        self.trans_type = pNL.AKZ
    def cSB(self, Gse, history):
        for OzJ in Gse:
            self._subjects[OzJ] = history
    def SzU(self, Gse):
        for OzJ in Gse:
            try:
                del self._subjects[OzJ]
            except KeyError:
                pass
    def get_subjects(self):
        return self._subjects
class rjC(RPR):
    def __init__(self, connection, WzD):
        self._connection = connection
        self._scheduler = WzD
    def DnJ(self, bow):
        if bow.operation == JDV.CIe:
            self._connection.connect()
        elif bow.operation == JDV.IRI:
            self._connection.subscribe(bow.Gse, bow.history)
        elif bow.operation == JDV.IRf:
            self._connection.unsubscribe(bow.Gse)
        elif bow.operation == JDV.iYv:
            self._connection.publish(bow.md_message)
        elif bow.operation == JDV.tWS:
            self._connection.Zdo().on_message(bow.message)
        elif bow.operation == JDV.xGO:
            if bow.connection_uuid == self._connection.xNp():
                self._connection.disconnect()
                self._connection.JeB()
                self._scheduler.gBI(bow.connection_uuid, self._connection,
                                          bow.disconnect_reason)
        elif bow.operation == JDV.cRk:
            self._connection.mOV()
            self._scheduler.bab(self._connection)
        elif bow.operation == JDV.UOb:
            self._connection.fvc()
        elif bow.operation == JDV.zCD:
            self._connection.NWn()
        elif bow.operation == JDV.xbn:
            self._connection.QVm()
        elif bow.operation == JDV.aVG:
            self._connection.resume()
        elif bow.operation == JDV.fsh:
            self._scheduler.yHX(self._connection.xNp(),
                                                           self._connection, Ral.ely)
        elif bow.operation == JDV.tly:
            self._connection.wUN()
import threading
import random
import time
class YOq(WUH):
    def __init__(self, configuration, client_state):
        self._keep_alive_timer_task = None
        self._reconnect_timer_task = None
        self._ping_operation_timer_task = None
        self._configuration = configuration
        self._client_state = client_state
        self._keep_alive_timeout = self._configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
    def gBI(self, DMp, connection, disconnect_info):
        if connection.BrZ() != jYX.DfN:
            return
        Wyi = connection.xNp()
        if Wyi is None or Wyi != DMp:
            return
        connection.QaU(None)
        connection.VrA(disconnect_info)
        tEv = connection.hbX()
        fRc = self.waQ(tEv, False)
        if self._reconnect_timer_task is not None:
            self._reconnect_timer_task.cancel()
        self._reconnect_timer_task = threading.Timer(fRc, self.LxY, [connection, disconnect_info])
        self._reconnect_timer_task.start()
    def LxY(self, connection, disconnect_info):
        connection.RzF().nQl(omM.vkb(disconnect_info))
    def bab(self, connection):
        if self._ping_operation_timer_task is not None:
            self._ping_operation_timer_task.cancel()
        self._ping_operation_timer_task = threading.Timer(self._configuration.PING_INTERVAL,
                                                          self.zQH, [connection])
        self._ping_operation_timer_task.start()
    def zQH(self, connection):
        connection.RzF().nQl(omM.Ets())
    def cancel(self):
        if self._keep_alive_timer_task is not None:
            self._keep_alive_timer_task.cancel()
        if self._ping_operation_timer_task is not None:
            self._ping_operation_timer_task.cancel()
        if self._reconnect_timer_task is not None:
            self._reconnect_timer_task.cancel()
    def yHX(self, DMp, connection, keep_alive):
        if self._keep_alive_timer_task is not None:
            self._keep_alive_timer_task.cancel()
        fRc = self._keep_alive_timeout
        if keep_alive == Ral.CIe:
            tEv = connection.uVR()
            fRc = self.waQ(tEv, True)
        if fRc > 0:
            self._keep_alive_timer_task = threading.Timer(fRc,
                                                          self.Xac, [DMp, connection])
            self._keep_alive_timer_task.start()
    def Xac(self, uuid, connection):
        Wyi = connection.xNp()
        if Wyi is None or Wyi != uuid:
            return
        self._client_state.lOq(AML.xGO)
        connection.RzF().nQl(
            omM.vZj(uuid, ePo.Glg))
    def wAP(self, value):
        self._keep_alive_timeout = value * 1.4
    def waQ(self, tEv, verify_timeout):
        fRc = self._configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
        if tEv > 0:
            if tEv <= self._configuration.quick_reconnect_max_retries:
                fRc = (tEv * self._configuration.quick_reconnect_initial_delay) - int(
                    random.uniform(0, 1) * self._configuration.quick_reconnect_initial_delay)
            else:
                if self._configuration.reconnect_policy == MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF:
                    count = tEv - self._configuration.quick_reconnect_max_retries
                    fRc = int(min(self._configuration.reconnect_time_interval * pow(2, count) - int(
                        random.uniform(0, 1) * self._configuration.reconnect_time_interval * count),
                                      self._configuration.reconnect_max_delay))
                else:
                    fRc = self._configuration.reconnect_time_interval
            if verify_timeout and fRc < self._configuration.OPERATION_TIMEOUT_INTERVAL:
                fRc = self._configuration.OPERATION_TIMEOUT_INTERVAL
        return fRc
import sys
import threading
class vHk:
    def __init__(self):
        self._lock = threading.Lock()
        self._running = False
        self._configuration = None
        self._connection = None
        self._single_thread_event_loop = None
        self._listener_notifier = None
        self._servers = None
        self._migratory_data_listener = None
        self._client_state = Kke()
        self.hxh = tYP.gPE
        self.QBt = "MigratoryDataClient/v6.0 Python/" + str(sys.version)
        self._logger = hmN()
        self._configuration = IAR(self.hxh, self.QBt)
    def yfA(self):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError("Error: connect() - already connected")
            if self._servers is None:
                raise RuntimeError(
                    "Error: connect() - no server to connect to; use set_servers() to specify one or more servers")
            if self._migratory_data_listener is None:
                raise RuntimeError(
                    "Error: connect() - no listener set; use set_listener() to specify a listener handler")
            self._running = True
            Ecy = WFl(self._servers, self._configuration.encryption)
            self._listener_notifier = Nwr(self._migratory_data_listener)
            self._listener_notifier.start()
            WzD = YOq(self._configuration, self._client_state)
            self._connection = Connection(self._configuration, self._listener_notifier, Ecy, WzD,
                                          self._client_state, self._logger)
            JRp = rjC(self._connection, WzD)
            self._single_thread_event_loop = Kag(JRp, self._logger)
            self._connection.GqO(self._single_thread_event_loop)
            self._single_thread_event_loop.nQl(omM.vMS())
            Gse = self._configuration.get_subjects()
            for pAK in Gse:
                self._single_thread_event_loop.nQl(
                    omM.JyK([pAK], Gse[pAK]))
                self._logger.debug(NWM.XkY + str([pAK]))
            self._single_thread_event_loop.start()
        finally:
            self._lock.release()
    def LxP(self, _servers):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError("Error: set_servers() - already connected; use this method before connect()")
            if _servers is None:
                raise TypeError("Error: set_servers() - servers has None value")
            if len(_servers) == 0:
                raise ValueError("Error: set_servers() - The list of servers is empty")
            self._logger.info("Setting Servers to connect to: " + str(_servers))
            self._servers = _servers
        finally:
            self._lock.release()
    def apc(self):
        self._lock.acquire()
        try:
            listener = self._migratory_data_listener
        finally:
            self._lock.release()
        return listener
    def clu(self, _listener):
        self._lock.acquire()
        try:
            if self._running is False:
                if _listener is None:
                    raise TypeError("Listener has None value")
                self._migratory_data_listener = _listener
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def Pxm(self, _log_listener, _log_level):
        self._lock.acquire()
        try:
            if self._running is False:
                self._logger.WXL(_log_listener, _log_level)
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def NWn(self):
        self._lock.acquire()
        try:
            self._logger.info("Disposing")
            if self._running is False:
                return
            self._running = False
            if self._single_thread_event_loop is not None:
                self._single_thread_event_loop.nQl(omM.Jjl())
                self._logger.debug(NWM.lua)
                self._single_thread_event_loop.NZY()
                self._single_thread_event_loop = None
            if self._listener_notifier is not None:
                self._listener_notifier.EZz()
                self._listener_notifier = None
        finally:
            self._lock.release()
    def zGd(self, token):
        self._lock.acquire()
        try:
            if token is None or len(token) == 0:
                raise TypeError("Token is null or empty.")
            self._configuration.entitlement_token = token
            self._logger.info("Configuring Entitlement token: " + token)
            if self._running is True:
                self._single_thread_event_loop.nQl(
                    omM.ePL())
        finally:
            self._lock.release()
    def EZq(self, _subjects, history):
        self._lock.acquire()
        try:
            if _subjects is None or len(_subjects) == 0:
                raise ValueError("Error: subscribe() - invalid argument; expected a list of valid topics")
            for OzJ in _subjects:
                if OzJ is None or len(OzJ) == 0 or ePo.GYQ(OzJ) is False:
                    raise TypeError("Subscribe with invalid OzJ: " + str(OzJ))
            if history < 0:
                raise ValueError(
                    "Error: subscribeWithHistory() - the argument numberOfHistoricalMessages should be a positive number or zero!")
            self._logger.info("Subscribing to: " + str(_subjects))
            self._configuration.cSB(_subjects, history)
            if self._running is True:
                self._single_thread_event_loop.nQl(
                    omM.JyK(_subjects, history))
                self._logger.debug(NWM.XkY + str(_subjects))
        finally:
            self._lock.release()
    def KJJ(self, _subjects):
        self._lock.acquire()
        try:
            if _subjects is None or len(_subjects) == 0:
                raise ValueError("Error: subscribe() - invalid argument; expected a list of valid topics")
            for OzJ in _subjects:
                if OzJ is None or len(OzJ) == 0 or ePo.GYQ(OzJ) is False:
                    raise TypeError("Unsubscribe with invalid OzJ: " + str(OzJ))
            self._logger.info("Unsubscribing from: " + str(_subjects))
            self._configuration.SzU(_subjects)
            if self._running is True:
                self._single_thread_event_loop.nQl(omM.ZuX(_subjects))
                self._logger.debug(NWM.wWM + str(_subjects))
        finally:
            self._lock.release()
    def HeD(self, _message):
        self._lock.acquire()
        try:
            if self._running is True:
                OzJ = _message.get_subject()
                tSP = _message.get_content()
                if OzJ is None or len(OzJ) == 0 or ePo.GYQ(OzJ) is False:
                    raise TypeError("Msg with invalid subj: " + str(OzJ))
                if tSP is None:
                    raise TypeError("Msg with null content")
                self._single_thread_event_loop.nQl(omM.SKw(_message))
                self._logger.debug(NWM.Ozz + str(_message))
            else:
                raise RuntimeError("Error: publish() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def Kns(self, _encryption_bool):
        self._lock.acquire()
        try:
            if self._running is False:
                self._logger.info("Configuring encryption to: " + str(_encryption_bool))
                self._configuration.encryption = _encryption_bool
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def KnQ(self, nr):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Notify_after_reconnect_retries() - already connected; use this method before connect")
            if nr < 1:
                raise ValueError(
                    "Error: Notify_after_reconnect_retries() - invalid argument; expected a positive integer")
            self._configuration.servers_down_before_notify = nr
            self._logger.info(
                "Configuring the number of failed connection attempts before sending a notification: " + str(nr))
        finally:
            self._lock.release()
    def PJb(self):
        self._lock.acquire()
        try:
            return list(self._configuration.get_subjects().keys())
        finally:
            self._lock.release()
    def QVm(self):
        self._lock.acquire()
        try:
            if self._running is True:
                self._logger.info("Migratorydata client calls pause")
                self._logger.debug(NWM.AxS)
                self._single_thread_event_loop.nQl(omM.Aap())
            else:
                raise RuntimeError("Error: pause() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def guW(self):
        self._lock.acquire()
        try:
            if self._running is True:
                self._logger.info("Migratorydata client calls resume")
                self._logger.debug(NWM.Jkt)
                self._single_thread_event_loop.nQl(omM.sdv())
            else:
                raise RuntimeError("Error: resume() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def xJp(self, nr):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_quick_reconnect_max_retries() - already connected; use this method before connect")
            if nr < 2:
                raise ValueError(
                    "Error: Set_quick_reconnect_max_retries() - invalid argument; expected an integer integer higher or equal to 2")
            self._configuration.quick_reconnect_max_retries = nr
            self._logger.info("Configuring quickReconnect max Retries to: " + str(nr))
        finally:
            self._lock.release()
    def cNl(self, interval):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_quick_reconnect_initial_delay() - already connected; use this method before connect")
            if interval < 1:
                raise ValueError(
                    "Error: Set_quick_reconnect_initial_delay() - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.quick_initial_delay = interval
            self._logger.info("Configuring quickReconnectInitial delay to: " + str(interval))
        finally:
            self._lock.release()
    def ZSj(self, _policy):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_policy - already connected; use this method before connect")
            if _policy or (
                            _policy != MigratoryDataClient.CONSTANT_WINDOW_BACKOFF and _policy != MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF):
                raise ValueError(
                    "Error: Set_reconnect_policy - invalid argument; expected MigratoryDataClient.CONSTANT_WINDOW_BACKOFF_ or MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF_")
            self._configuration.reconnect_policy = _policy
            self._logger.info("Configuring Reconnect Policy to: " + _policy)
        finally:
            self._lock.release()
    def hEp(self, interval):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_time_interval() - already connected; use this method before connect")
            if interval < 1:
                raise ValueError(
                    "Error: Set_reconnect_time_interval - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.reconnect_time_interval = interval
            self._logger.info("Configuring setReconnectTime interval  to: " + str(interval))
        finally:
            self._lock.release()
    def pCX(self, delay):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_reconnect_max_delay() - already connected; use this method before connect")
            if delay < 1:
                raise ValueError(
                    "Error: Set_reconnect_max_delay() - invalid argument; expected an integer integer higher or equal to 1")
            self._configuration.reconnect_max_delay = delay
            self._logger.info("Configuring setReconnectMax delay  to: " + str(delay))
        finally:
            self._lock.release()
    def bmw(self, type):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_transport() - already connected; use this method before connect")
            if type == MigratoryDataClient.TRANSPORT_HTTP:
                self._configuration.trans_type = pNL.HTTP
            self._logger.info("Configuring transport type to: " + type)
        finally:
            self._lock.release()
class MigratoryDataClient:
    NOTIFY_SERVER_UP = "NOTIFY_SERVER_UP"
    NOTIFY_SERVER_DOWN = "NOTIFY_SERVER_DOWN"
    NOTIFY_DATA_SYNC = "NOTIFY_DATA_SYNC"
    NOTIFY_DATA_RESYNC = "NOTIFY_DATA_RESYNC"
    NOTIFY_SUBSCRIBE_ALLOW = "NOTIFY_SUBSCRIBE_ALLOW"
    NOTIFY_SUBSCRIBE_DENY = "NOTIFY_SUBSCRIBE_DENY"
    NOTIFY_PUBLISH_OK = "NOTIFY_PUBLISH_OK"
    NOTIFY_PUBLISH_FAILED = "NOTIFY_PUBLISH_FAILED"
    NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED = "NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED"
    NOTIFY_PUBLISH_DENIED = "NOTIFY_PUBLISH_DENIED"
    qWn = "NOTIFY_CONNECT_OK"
    YrN = "NOTIFY_CONNECT_DENY"
    CONSTANT_WINDOW_BACKOFF = "CONSTANT_WINDOW_BACKOFF"
    TRUNCATED_EXPONENTIAL_BACKOFF = "TRUNCATED_EXPONENTIAL_BACKOFF"
    TRANSPORT_HTTP = "TRANSPORT_HTTP"
    TRANSPORT_WEBSOCKET = "TRANSPORT_WEBSOCKET"
    def __init__(self):
        self._client_impl = vHk()
    def connect(self):
        self._client_impl.yfA()
    def disconnect(self):
        self._client_impl.NWn()
    def set_listener(self, listener):
        if issubclass(type(listener), MigratoryDataListener) is False:
            raise TypeError("Argument for set_listener must be a subclass MigratoryDataListener")
        self._client_impl.clu(listener)
    def get_listener(self):
        return self._client_impl.apc()
    def set_log_listener(self, log_listener, log_level):
        if issubclass(type(log_listener), MigratoryDataLogListener) is False:
            raise TypeError("First argument for set_log_listener must be a subclass MigratoryDataLogListener")
        if type(log_level) is not int:
            raise TypeError("Second argument for set_log_level must be a MigratoryDataLogLevel")
        if log_level < 0 or log_level > 4:
            raise TypeError("Second argument for set_log_level must be a MigratoryDataLogLevel")
        self._client_impl.Pxm(log_listener, log_level)
    def set_entitlement_token(self, entitlement_token):
        if type(entitlement_token) is not str:
            raise TypeError("Argument for set_entitlement_token must be of type string")
        self._client_impl.zGd(entitlement_token)
    def set_servers(self, servers):
        self._check_if_is_string_list(servers, "set_servers")
        self._client_impl.LxP(servers)
    def _check_if_is_string_list(self, string_list, method_name):
        if type(string_list) is not list:
            raise TypeError("First argument for " + method_name + " must be a list of strings")
        for uDC in string_list:
            if type(uDC) is not str:
                raise TypeError("First argument for " + method_name + " must be a list of strings")
    def subscribe(self, subject_list):
        self._check_if_is_string_list(subject_list, "subscribe")
        self._client_impl.EZq(subject_list, 0)
    def subscribe_with_history(self, subject_list, number_of_historical_messages):
        self._check_if_is_string_list(subject_list, "subscribe_with_history")
        if type(number_of_historical_messages) is not int:
            raise TypeError("Second argument for subscribe_with_history must be of type int")
        self._client_impl.EZq(subject_list, number_of_historical_messages)
    def unsubscribe(self, subject_list):
        self._check_if_is_string_list(subject_list, "unsubscribe")
        self._client_impl.KJJ(subject_list)
    def publish(self, message):
        if type(message) is not MigratoryDataMessage:
            raise TypeError("Argument for publish must be of type MigratoryDataMessage")
        self._client_impl.HeD(message)
    def set_encryption(self, encryption_bool):
        if type(encryption_bool) is not bool:
            raise TypeError("Argument for set_encryption must be of type bool")
        self._client_impl.Kns(encryption_bool)
    def get_subjects(self):
        return self._client_impl.PJb()
    def pause(self):
        self._client_impl.QVm()
    def resume(self):
        self._client_impl.guW()
    def notify_after_failed_connection_attempts(self, retries_number):
        if type(retries_number) is not int:
            raise TypeError("Argument for notify_after_failed_connection_attempts must be of type int")
        self._client_impl.KnQ(retries_number)
    def set_quick_reconnect_max_retries(self, retries_number):
        if type(retries_number) is not int:
            raise TypeError("Argument for set_quick_reconnect_max_retries must be of type int")
        self._client_impl.xJp(retries_number)
    def set_quick_reconnect_initial_delay(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_quick_reconnect_initial_delay must be of type int")
        self._client_impl.cNl(seconds)
    def set_reconnect_policy(self, policy):
        if type(policy) is not str:
            raise TypeError("Argument for set_reconnect_policy must be of type string")
        self._client_impl.ZSj(policy)
    def set_reconnect_time_interval(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_reconnect_time_interval must be of type int")
        self._client_impl.hEp(seconds)
    def set_reconnect_max_delay(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_reconnect_max_delay must be of type int")
        self._client_impl.pCX(seconds)
    def set_transport(self, transport_type):
        if transport_type != MigratoryDataClient.TRANSPORT_HTTP and transport_type != MigratoryDataClient.TRANSPORT_WEBSOCKET:
            raise TypeError(
                "Argument for set_transport must be MigratoryDataClient.TRANSPORT_WEBSOCKET or MigratoryDataClient.TRANSPORT_HTTP")
        self._client_impl.bmw(transport_type)
