import abc
class lYT(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def EWQ(self, host):
        pass
    @abc.abstractmethod
    def WTN(self, MXh):
        pass
    @abc.abstractmethod
    def AZx(self, host, encrypted):
        pass
import threading
class UsT:
    def __init__(self, value):
        self._lock = threading.Lock()
        self._value = value
    def NuT(self, value):
        with self._lock:
            self._value = value
    def UHJ(self):
        with self._lock:
            return self._value
    def __repr__(self) -> str:
        return str(self._value)
class rWc:
    def __init__(self, _start, _end):
        self._start = _start
        self._end = _end
    def MSp(self):
        return self._start
    def xIf(self):
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
        self.HQg = qos
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
        return self.HQg
    def get_message_type(self):
        return self._message_type
    def set_compressed(self, compression_bool):
        self._compression = compression_bool
    def is_compressed(self):
        return self._compression
    def __repr__(self) -> str:
        bIs = "["
        bIs += "Subj = " + str(self._subject) + ", "
        bIs += "Content =  " + str(self._content.decode("utf-8")) + ", "
        bIs += "Closure =  " + str(self._closure) + ", "
        bIs += "ReplyToSubject =  " + str(self._reply_to_subject) + ", "
        bIs += "Retained = " + str(self._retained) + ", "
        bIs += "QOS = " + self.yNq() + ", "
        bIs += "MessageType = " + self.MUC() + ", "
        bIs += "Seq = " + str(self._seq) + ", "
        bIs += "Epoch = " + str(self._epoch) + " "
        bIs += "Compression = " + str(self._compression) + " "
        bIs += "]"
        return bIs
    def yNq(self):
        if self.HQg == QoS.STANDARD:
            return "STANDARD"
        return "GUARANTEED"
    def MUC(self):
        if self._message_type == MessageType.SNAPSHOT:
            return "SNAPSHOT"
        if self._message_type == MessageType.UPDATE:
            return "UPDATE"
        if self._message_type == MessageType.RECOVERED:
            return "RECOVERED"
        return "HISTORICAL"
class qQA:
    def __init__(self):
        self.mcf = bytearray()
        self.VON = 0
        self.content_length_mark = -1
        self.payload_mark = -1
        self.body_start_mark = -1
        self.body_end_mark = -1
    def GAH(self, VON):
        self.VON = VON
    def extend(self, ALH):
        self.mcf.extend(ALH)
    def append(self, ALH):
        self.mcf.append(ALH)
    def Fdz(self):
        self.mcf = self.mcf[self.VON:]
        self.VON = 0
    def clear(self):
        self.mcf = bytearray()
        self.VON = 0
    def INS(self):
        if self.VON == 0:
            return self.mcf
        else:
            return self.mcf[self.VON:]
import threading
import socket
class ZrB(threading.Thread):
    def __init__(self, _socket, connection, uuid):
        threading.Thread.__init__(self)
        self._socket = _socket
        self._connection = connection
        self._buf = qQA()
        self._uuid = uuid
        self._run = True
    def run(self):
        while self._run:
            try:
                ORI = self._socket.recv(32768)
                if len(ORI) == 0:
                    break
                self._buf.extend(ORI)
                self._connection.Tpi(self._buf)
                if self._buf.VON > 0 and self._buf.VON < len(self._buf.mcf):
                    self._buf.Fdz()
                elif self._buf.VON >= len(self._buf.mcf):
                    self._buf.clear()
            except (OSError, socket.error) as ifQ:
                pass
        self._connection.ArA(self._uuid, gHQ.XHM, "read_thread")
    def oBS(self):
        self._run = False
import queue
import threading
import socket
class XBk(threading.Thread):
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
            except (queue.Empty or socket.error) as ifQ:
                pass
    def RUH(self, message):
        self._message_queue.put(message)
    def oBS(self):
        self._run = False
import logging
class hKu(MigratoryDataLogListener):
    def __init__(self):
        self.log1 = logging.getLogger("CLIENT")
        self.log1.setLevel(logging.INFO)
        qGy = logging.StreamHandler()
        qGy.setLevel(logging.INFO)
        xkY = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        qGy.setFormatter(xkY)
        del self.log1.handlers[:]
        self.log1.addHandler(qGy)
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
class ySB(metaclass=abc.ABCMeta):
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
class osA(ySB):
    def __init__(self):
        self._lock = threading.Lock()
        self._log_listener = hKu()
        self._log_level = MigratoryDataLogLevel.INFO
    def wsC(self, log_listener, log_level):
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
class fqD:
    yRC = "[READ_EVENT]"
    tPH = "[PING_EVENT]"
    iMT = "[CONNECT_EVENT]"
    raC = "[DISCONNECT_EVENT]"
    SCB = "[READER_DISCONNECT_EVENT]"
    SgG = "[MESSAGE_RECEIVED_EVENT]"
    lLA = "[WRITE_EVENT]"
    tRt = "[CLIENT_PUBLISH_RESPONSE]"
    Vpe = "[Vpe]"
    KtW = "[ENTITLEMENT_CHECK_RESPONSE]"
    hZv = "[DISPOSE_EVENT]"
    wso = "[PAUSE_EVENT]"
    aTg = "[RESUME_EVENT]"
    dsq = "[SUBSCRIBE_EVENT]"
    fXo = "[UNSUBSCRIBE_EVENT]"
    jid = "[PUBLISH_EVENT]"
    egj = "[REPUBLISH_EVENT"
    IkC = "[PING_SERVER_EVENT]"
    ZLJ = "[CONNECT_SERVER_EVENT]"
    sBE = "[RECONNECT_EVENT]"
class fdd:
    mzp = 0
    lwB = 1
    jgb = 2
class TOP:
    eWz = "cache_ok"
    gDG = 2
    def __init__(self, guq, history):
        self._subject = guq
        self._history = history
        self._seq = 0
        self._seq_id = 70000
        self._need_recovery = False
        self._nr_of_consecutive_recoveries = 0
        self._messages_recieved_until_recovery = 0
        self._cache_recovery_status = TOP.eWz
        self._current_subscribe_type = fdd.mzp
    def get_seq(self):
        return self._seq
    def Wmn(self, AMA):
        self._seq = AMA
        self._messages_recieved_until_recovery += 1
    def jrJ(self):
        return self._seq_id
    def jBO(self, lbh):
        self._seq_id = lbh
    def get_subject(self):
        return self._subject
    def FZC(self):
        return self._history
    def iwQ(self):
        self._messages_recieved_until_recovery = 0
        if self.Urh():
            self._nr_of_consecutive_recoveries += 1
    def GgL(self):
        self._nr_of_consecutive_recoveries = 0
    def IbH(self):
        return self._messages_recieved_until_recovery
    def zIF(self, status):
        self._cache_recovery_status = status
    def SvO(self):
        return self._cache_recovery_status
    def Urh(self):
        return self._seq_id != 70000
    def HNj(self):
        type = fdd.mzp
        if self.Urh():
            if self._nr_of_consecutive_recoveries >= TOP.gDG:
                if self._history > 0:
                    type = fdd.lwB
            else:
                type = fdd.jgb
        else:
            if self._history > 0:
                type = fdd.lwB
        if type == fdd.mzp or type == fdd.lwB:
            self.zIF(TOP.eWz)
            self.GgL()
        self._current_subscribe_type = type
        return type
    def ucU(self):
        return self._current_subscribe_type
    def emd(self):
        self._current_subscribe_type = fdd.mzp
    def wan(self):
        self._seq = 0
        self._seq_id = 70000
        self._need_recovery = False
        self._nr_of_consecutive_recoveries = 0
        self._messages_recieved_until_recovery = 0
        self._cache_recovery_status = self.eWz
        self._current_subscribe_type = fdd.mzp
    def __repr__(self) -> str:
        bIs = "["
        bIs += "Subj = " + str(self._subject) + ", "
        bIs += "Seq = " + str(self._seq) + ", "
        bIs += "SeqId = " + str(self._seq_id) + ", "
        bIs += "NeedRecovery = " + str(self._need_recovery) + ", "
        bIs += "MessagesReceivedUntilRecovery = " + str(self._messages_recieved_until_recovery) + ", "
        bIs += "CacheRecoveryStatus = " + str(self._cache_recovery_status) + ", "
        bIs += "SubsType = " + str(self._current_subscribe_type) + ", "
        bIs += "NrOfConsecutiveRecovery = " + str(self._nr_of_consecutive_recoveries)
        bIs += "]"
        return bIs
class joo:
    def __init__(self, operation, gNU):
        self.operation = operation
        self.gNU = gNU
    def __repr__(self) -> str:
        bIs = "OPERATION " + str(self.YQT(int(self.operation))) + " - "
        bIs += "Headers "
        for WLq in self.gNU:
            zIW = str(self.VmQ(int(WLq)))
            value = None
            if zIW == "MESSAGE_TYPE" and isinstance(zIW, int):
                value = self.fyj(int(self.gNU.get(WLq)))
            else:
                value = str(self.gNU.get(WLq))
            bIs += zIW + ": " + value + " - "
        return bIs
    def YQT(self, number):
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
            return "AGENT_CONNECT"
        elif number == 7:
            return "RECOVERY_CACHE"
        elif number == 8:
            return "RECOVERY_IMAGE"
        elif number == 9:
            return "ENTITLEMENT_CHECK"
        elif number == 10:
            return "RESET_SUBJECT"
        elif number == 11:
            return "PROXY"
        elif number == 12:
            return "ACK"
        elif number == 13:
            return "STALE"
        elif number == 14:
            return "ADD_DATA_REF"
        elif number == 15:
            return "CLIENT_PUBLISH"
        elif number == 16:
            return "CLIENT_PUBLISH_RESPONSE"
        elif number == 17:
            return "SYNC_SUBSCRIPTION"
        elif number == 18:
            return "PUBLISH_ACK"
        elif number == 19:
            return "CONNECT"
    def VmQ(self, number):
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
    def fyj(self, number):
        if number == 1:
            return "SNAPSHOT"
        elif number == 2:
            return "UPDATE"
        elif number == 3:
            return "RECOVERY"
class RKL:
    NbO = 0
    Sdl = 1
    jax = 2
import struct
class ETB:
    YuP = []
    FRG = []
    qUm = []
    UNE = []
    qvi = 0x19
    EEH = 0x7F
    tWC = 0x1E
    Lke = 0x1F
    kLV = []
    gNU = []
    eKo = []
    @staticmethod
    def xlW():
        for DKW in range(0, 128):
            ETB.YuP.append(-1)
        ETB.YuP[sJO.KLK] = 0x01
        ETB.YuP[sJO.vKi] = 0x02
        ETB.YuP[sJO.dQH] = 0x03
        ETB.YuP[sJO.TYb] = 0x04
        ETB.YuP[sJO.blF] = 0x05
        ETB.YuP[sJO.klX] = 0x06
        ETB.YuP[sJO.IzP] = 0x08
        ETB.YuP[sJO.cRR] = 0x09
        ETB.YuP[sJO.KDO] = 0x0C
        ETB.YuP[sJO.fqS] = 0x10
        ETB.YuP[sJO.CLIENT_PUBLISH_RESPONSE] = 0x13
        ETB.YuP[sJO.ojR] = 0x1A
        for DKW in range(0, 128):
            ETB.kLV.append(-1)
        for JlT in range(0, sJO.ojR + 1):
            ETB.kLV[ETB.waX(JlT)] = JlT
        for DKW in range(0, 128):
            ETB.FRG.append(-1)
        ETB.FRG[aZG.SZC] = 0x01
        ETB.FRG[aZG.Zwl] = 0x02
        ETB.FRG[aZG.EME] = 0x03
        ETB.FRG[aZG.BLq] = 0x04
        ETB.FRG[aZG.Xvv] = 0x05
        ETB.FRG[aZG.AAX] = 0x06
        ETB.FRG[aZG.JqS] = 0x07
        ETB.FRG[aZG.frl] = 0x08
        ETB.FRG[aZG.Yof] = 0x09
        ETB.FRG[aZG.ERROR] = 0x0B
        ETB.FRG[aZG.RvJ] = 0x0C
        ETB.FRG[aZG.hPV] = 0x0F
        ETB.FRG[aZG.PNz] = 0x10
        ETB.FRG[aZG.VPu] = 0x11
        ETB.FRG[aZG.TXN] = 0x12
        ETB.FRG[aZG.vsJ] = 0x13
        ETB.FRG[aZG.rqV] = 0x14
        ETB.FRG[aZG.JeD] = 0x15
        ETB.FRG[aZG.SQj] = 0x16
        ETB.FRG[aZG.TJE] = 0x17
        ETB.FRG[aZG.zGr] = 0x18
        ETB.FRG[aZG.jLU] = 0x1A
        ETB.FRG[aZG.Qeq] = 0x20
        ETB.FRG[aZG.opV] = 0x27
        ETB.FRG[aZG.ODC] = 0x28
        ETB.FRG[aZG.Fxg] = 0x23
        ETB.FRG[aZG.lSg] = 0x24
        ETB.FRG[aZG.dbx] = 0x25
        ETB.FRG[aZG.CjW] = 0x2C
        ETB.FRG[aZG.lfM] = 0x2D
        ETB.FRG[aZG.AlZ] = 0x2E
        ETB.FRG[aZG.sZU] = 0x2F
        ETB.FRG[aZG.Iov] = 0x30
        ETB.FRG[aZG.Oaa] = 0x1D
        ETB.FRG[aZG.gHn] = 0x26
        for DKW in range(0, 128):
            ETB.gNU.append(-1)
        for JlT in range(0, aZG.gHn + 1):
            ETB.gNU[ETB.Rgs(JlT)] = JlT
        for DKW in range(0, 128):
            ETB.eKo.append(-1)
        ETB.heU(aZG.SZC, For.BTj)
        ETB.heU(aZG.Zwl, For.Cph)
        ETB.heU(aZG.EME, For.wiZ)
        ETB.heU(aZG.BLq, For.wiZ)
        ETB.heU(aZG.Xvv, For.wiZ)
        ETB.heU(aZG.AAX, For.wiZ)
        ETB.heU(aZG.JqS, For.Cph)
        ETB.heU(aZG.frl, For.Cph)
        ETB.heU(aZG.Yof, For.Cph)
        ETB.heU(aZG.ERROR, For.wiZ)
        ETB.heU(aZG.RvJ, For.Cph)
        ETB.heU(aZG.hPV, For.wiZ)
        ETB.heU(aZG.TXN, For.BTj)
        ETB.heU(aZG.vsJ, For.BTj)
        ETB.heU(aZG.rqV, For.BTj)
        ETB.heU(aZG.JeD, For.wiZ)
        ETB.heU(aZG.SQj, For.wiZ)
        ETB.heU(aZG.TJE, For.wiZ)
        ETB.heU(aZG.zGr, For.wiZ)
        ETB.heU(aZG.jLU, For.BTj)
        ETB.heU(aZG.Qeq, For.BTj)
        ETB.heU(aZG.opV, For.BTj)
        ETB.heU(aZG.Fxg, For.BTj)
        ETB.heU(aZG.lSg, For.wiZ)
        ETB.heU(aZG.dbx, For.wiZ)
        ETB.heU(aZG.PNz, For.BTj)
        ETB.heU(aZG.VPu, For.wiZ)
        ETB.heU(aZG.ODC, For.wiZ)
        ETB.heU(aZG.CjW, For.BTj)
        ETB.heU(aZG.lfM, For.wiZ)
        ETB.heU(aZG.AlZ, For.wiZ)
        ETB.heU(aZG.sZU, For.wiZ)
        ETB.heU(aZG.Iov, For.BTj)
        ETB.heU(aZG.Oaa, For.wiZ)
        ETB.heU(aZG.gHn, For.wiZ)
        for DKW in range(0, 255):
            ETB.UNE.append(-1)
        ETB.UNE[ETB.EEH] = 0x01;
        ETB.UNE[ETB.tWC] = 0x02;
        ETB.UNE[ETB.Lke] = 0x03;
        ETB.UNE[JHs.PuT] = 0x04;
        ETB.UNE[JHs.pie] = 0x05;
        ETB.UNE[JHs.tIc] = 0x06;
        ETB.UNE[JHs.xGa] = 0x07;
        ETB.UNE[JHs.HVu] = 0x08;
        ETB.UNE[33] = 0x09;
        ETB.UNE[ETB.qvi] = 0x0B;
        for DKW in range(0, 255):
            ETB.qUm.append(-1)
        for JlT in range(0, 128):
            ifQ = ETB.CeD(JlT)
            if ifQ != -1:
                ETB.qUm[ifQ] = JlT
    @staticmethod
    def heU(fYg, hdr_type):
        ETB.eKo[ETB.Rgs(fYg)] = hdr_type
    @staticmethod
    def IkZ(ehY):
        Bhz = ETB.FUT(ehY)
        iaS = 0
        for ZtG in range(0, len(Bhz)):
            UNE = ETB.CeD(Bhz[ZtG])
            if UNE != -1:
                iaS += 1
        if iaS == 0:
            mcf = bytearray()
            mcf.extend(Bhz)
            return mcf
        kPY = []
        for JlT in range(0, len(Bhz) + iaS):
            kPY.append(0)
        ZtG = 0
        RlS = 0
        while ZtG < len(Bhz):
            UNE = ETB.CeD(Bhz[ZtG])
            if UNE != -1:
                kPY[RlS] = ETB.Lke
                kPY[RlS + 1] = UNE
                RlS += 1
            else:
                kPY[RlS] = Bhz[ZtG]
            ZtG += 1
            RlS += 1
        mcf = bytearray()
        mcf.extend(kPY)
        return mcf
    @staticmethod
    def Qkf(Bhz):
        iaS = 0
        for ZtG in range(0, len(Bhz)):
            UNE = ETB.CeD(Bhz[ZtG])
            if UNE != -1:
                iaS += 1
        if iaS == 0:
            return Bhz
        kPY = []
        for JlT in range(0, len(Bhz) + iaS):
            kPY.append(0)
        ZtG = 0
        RlS = 0
        while ZtG < len(Bhz):
            UNE = ETB.CeD(Bhz[ZtG])
            if UNE != -1:
                kPY[RlS] = ETB.Lke
                kPY[RlS + 1] = UNE
                RlS += 1
            else:
                kPY[RlS] = Bhz[ZtG]
            ZtG += 1
            RlS += 1
        mcf = bytearray()
        mcf.extend(kPY)
        return mcf
    @staticmethod
    def Teg(ehY):
        Bhz = list(struct.unpack(len(ehY) * 'B', ehY))
        iaS = 0
        if len(Bhz) == 0:
            return ehY
        for ZtG in range(0, len(Bhz)):
            if Bhz[ZtG] == ETB.Lke:
                iaS += 1
        kPY = []
        for JlT in range(0, len(Bhz) - iaS):
            kPY.append(0)
        ZtG = 0
        RlS = 0
        while ZtG < len(Bhz):
            dnS = Bhz[ZtG]
            if dnS == ETB.Lke:
                if ZtG + 1 < len(Bhz):
                    kPY[RlS] = ETB.WSX(Bhz[ZtG + 1])
                    if kPY[RlS] == -1:
                        raise ValueError()
                    ZtG += 1
                else:
                    raise ValueError()
            else:
                kPY[RlS] = dnS
            ZtG += 1
            RlS += 1
        mcf = bytearray()
        mcf.extend(kPY)
        return mcf
    @staticmethod
    def ZgR(ehY, _headerId, _headerType):
        LGn = None
        tZQ = ehY.find(chr(ETB.Rgs(_headerId)))
        dUz = ehY.find(chr(ETB.tWC), tZQ)
        if tZQ != -1 and dUz != -1:
            WCL = ehY[tZQ + 1:dUz]
            if _headerType == For.gZQ:
                LGn = WCL
            elif _headerType == For.Cph:
                LGn = WCL
            elif _headerType == For.BTj:
                LGn = WCL
            elif _headerType == For.wiZ:
                LGn = ETB.wxD(WCL);
        return LGn
    @staticmethod
    def wxD(_dataString):
        ehY = list(struct.unpack(len(_dataString) * 'B', _dataString))
        kPY = 0
        mKj = -1
        _val = 0
        WQZ = len(ehY)
        fFU = 0
        if WQZ == 1:
            return ehY[0]
        elif WQZ == 2 and ehY[fFU] == ETB.Lke:
            dnS = ETB.WSX(ehY[fFU + 1])
            if dnS != -1:
                return dnS
            else:
                raise ValueError()
        while WQZ > 0:
            dnS = ehY[fFU]
            fFU += 1
            if dnS == ETB.Lke:
                if WQZ - 1 < 0:
                    raise ValueError()
                WQZ -= 1
                dnS = ehY[fFU]
                fFU += 1
                Mkc = ETB.WSX(dnS)
                if Mkc == -1:
                    raise ValueError()
            else:
                Mkc = dnS
            if mKj > 0:
                _val |= Mkc >> mKj
                kPY = kPY << 8 | (_val if _val >= 0   else _val + 256)
                _val = (Mkc << (8 - mKj))
            else:
                _val = (Mkc << - mKj)
            mKj = (mKj + 7) % 8;
            WQZ -= 1
        return kPY
    @staticmethod
    def sKV(_val):
        if (int(_val) & 0xFFFFFF80) == 0:
            JlT = ETB.CeD(_val)
            if JlT == -1:
                return struct.pack('B', _val)
            else:
                return struct.pack('BB', ETB.Lke, JlT)
        DKd = 0
        if (int(_val) & 0xFF000000) != 0:
            DKd = 24
        elif (int(_val) & 0x00FF0000) != 0:
            DKd = 16
        else:
            DKd = 8
        kPY = []
        for JlT in range(0, 10):
            kPY.append(0)
        PmD = 0
        TWc = 0
        while DKd >= 0:
            b = ((int(_val) >> DKd) & 0xFF)
            TWc += 1
            kPY[PmD] |= ((b if b >= 0 else b + 256) >> TWc)
            UNE = ETB.CeD(kPY[PmD])
            if UNE != -1:
                kPY[PmD] = ETB.Lke
                kPY[PmD + 1] = UNE
                PmD += 1
            PmD += 1
            kPY[PmD] |= (b << (7 - TWc)) & 0x7F;
            DKd -= 8
        UNE = ETB.CeD(kPY[PmD])
        if UNE != -1:
            kPY[PmD] = ETB.Lke
            kPY[PmD + 1] = UNE
            PmD += 1
        PmD += 1
        if PmD < len(kPY):
            kPY = kPY[0:PmD]
        mcf = bytearray()
        mcf.extend(kPY)
        return mcf
    @staticmethod
    def WSX(b):
        if b >= 0:
            return ETB.qUm[int(b)]
        else:
            return -1
    @staticmethod
    def CeD(b):
        if b >= 0:
            return ETB.UNE[int(b)]
        else:
            return -1
    @staticmethod
    def Rgs(h):
        return ETB.FRG[int(h)]
    @staticmethod
    def waX(o):
        return ETB.YuP[int(o)]
    @staticmethod
    def YNl(fYg):
        AYz = ETB.Rgs(fYg)
        return ETB.eKo[AYz]
    @staticmethod
    def FUT(str_value):
        dqH = str_value.encode('utf-8')
        return list(struct.unpack(len(dqH) * 'B', dqH))
    @staticmethod
    def Kbv(b):
        if b < 0:
            return None
        return ETB.gNU[b]
class sJO:
    KLK = 0
    vKi = 1
    dQH = 2
    TYb = 3
    blF = 4
    klX = 5
    IzP = 6
    cRR = 7
    KDO = 8
    fqS = 9
    CLIENT_PUBLISH_RESPONSE = 10
    ojR = 11
class aZG:
    SZC = 0
    Zwl = 1
    EME = 2
    BLq = 3
    Xvv = 4
    AAX = 5
    JqS = 6
    frl = 7
    Yof = 8
    ERROR = 9
    RvJ = 10
    hPV = 11
    TXN = 12
    vsJ = 13
    rqV = 14
    JeD = 15
    SQj = 16
    TJE = 17
    zGr = 18
    jLU = 19
    Qeq = 20
    opV = 21
    Fxg = 22
    lSg = 23
    dbx = 24
    PNz = 25
    VPu = 26
    ODC = 27
    CjW = 28
    lfM = 29
    AlZ = 30
    sZU = 31
    Iov = 32
    Oaa = 33
    gHn = 34
class For:
    gZQ = 0
    Cph = 1
    BTj = 2
    wiZ = 3
class JHs:
    PuT = 0x00
    xGa = 0x22
    pie = 0x0A
    tIc = 0x0D
    HVu = 0x5C
class AZa:
    IwM = 1
    jSG = 2
    ycH = 3
    AGA = 4
class uNa:
    kFY = 0
    QEm = 1
    JIG = 2
    AqZ = 3
    qlI = 4
    mQq = 5
    eQo = 6
    MbT = 7
    qSd = 8
class aqF:
    SNAPSHOT = "1"
    UPDATE = "2"
    RECOVERED = "3"
    HISTORICAL = "4"
class pSU:
    ucH = "d"
    iZf = "a"
ETB.xlW()
class FCV(lYT):
    FuV = "POST / HTTP/1.1\r\n"
    tZJ = "Host: "
    iJA = "Content-Length: "
    pOK = "000"
    ekO = "\r\n"
    def __init__(self):
        pass
    def EWQ(self, host):
        MXh = qQA()
        MXh.extend(bytes(FCV.FuV, 'utf-8'))
        MXh.extend(bytes(FCV.tZJ, 'utf-8'))
        MXh.extend(bytes(host, 'utf-8'))
        MXh.extend(bytes(FCV.ekO, 'utf-8'))
        MXh.extend(bytes(FCV.iJA, 'utf-8'))
        MXh.content_length_mark = len(MXh.mcf)
        MXh.extend(bytes(FCV.pOK, 'utf-8'))
        MXh.extend(bytes(FCV.ekO, 'utf-8'))
        MXh.extend(bytes(FCV.ekO, 'utf-8'))
        MXh.payload_mark = len(MXh.mcf)
        return MXh
    def WTN(self, MXh):
        VON = len(MXh.mcf)
        yTA = len(MXh.mcf) - MXh.payload_mark
        NlA = bytes(str(yTA), 'utf-8')
        if len(NlA) <= len(FCV.pOK):
            Jaf = 0
            for JlT in range(len(FCV.pOK) - len(NlA),
                           len(FCV.pOK)):
                MXh.mcf[MXh.content_length_mark + JlT] = NlA[Jaf]
                Jaf = Jaf + 1
        else:
            SUF = MXh.mcf[0:MXh.content_length_mark]
            SUF.extend(NlA)
            SUF.extend(MXh.mcf[(MXh.content_length_mark + len(FCV.pOK)):])
            MXh.mcf = SUF
    def AZx(self, host, encrypted):
        MXh = qQA()
        return MXh
import random
class MeW(lYT):
    fyW = "GET /WebSocketConnection HTTP/1.1\r\n"
    fYA = "GET /WebSocketConnection-Secure HTTP/1.1\r\n"
    QsG = "Host: "
    Kxt = "Origin: "
    UwR = "Upgrade: websocket\r\n"
    vxn = "Sec-WebSocket-Key: 23eds34dfvce4\r\n"
    vUc = "Sec-WebSocket-Version: 13\r\n"
    ktR = "Sec-WebSocket-Protocol: pushv1\r\n"
    Pzy = "Connection: Upgrade\r\n"
    ekO = "\r\n"
    PgD = 2
    aBc = 10
    BRp = 128
    oAR = 128
    def EWQ(self, host):
        MXh = qQA()
        VON = MeW.aBc
        for JlT in range(0, 10):
            MXh.extend(bytes([0]))
        for JlT in range(0, 4):
            VON += 1
            dYQ = random.randint(0, 255)
            MXh.extend([dYQ])
        MXh.GAH(VON)
        MXh.body_start_mark = VON
        return MXh
    def WTN(self, MXh):
        bjx = MeW.oAR
        bjx |= MeW.PgD
        MXh.body_end_mark = len(MXh.mcf)
        ixy = MXh.body_end_mark - MXh.body_start_mark
        ZDV = self.ynF(ixy)
        IMm = self.XKT(ixy, ZDV)
        xYO = 0
        TQY = 0
        if ZDV == 1:
            xYO = 8
            TQY = 8
            MXh.mcf[TQY] = bjx
            MXh.mcf[TQY + 1] = IMm[0] | MeW.BRp
        elif ZDV == 2:
            xYO = 6
            TQY = 6
            MXh.mcf[TQY] = bjx
            MXh.mcf[TQY + 1] = 126 | MeW.BRp
            TQY += 2
            for JlT in range(0, 2):
                MXh.mcf[TQY + JlT] = IMm[JlT]
        else:
            MXh.mcf[TQY] = bjx
            MXh.mcf[TQY + 1] = 127 | MeW.BRp
            TQY += 2
            for JlT in range(0, 8):
                MXh.mcf[TQY + JlT] = IMm[JlT]
        Tth = bytearray()
        Tth.extend([MXh.mcf[MXh.body_start_mark - 4]])
        Tth.extend([MXh.mcf[MXh.body_start_mark - 3]])
        Tth.extend([MXh.mcf[MXh.body_start_mark - 2]])
        Tth.extend([MXh.mcf[MXh.body_start_mark - 1]])
        WDE = 0
        for JlT in range(MXh.body_start_mark, MXh.body_end_mark):
            b = MXh.mcf[JlT] ^ Tth[WDE]
            MXh.mcf[JlT] = b
            if WDE == 3:
                WDE = 0
            else:
                WDE += 1
        MXh.GAH(xYO)
    def AZx(self, host, encrypted):
        MXh = qQA()
        if encrypted is False:
            MXh.extend(bytes(MeW.fyW, 'utf-8'))
        else:
            MXh.extend(bytes(MeW.fYA, 'utf-8'))
        MXh.extend(bytes(MeW.Kxt, 'utf-8'))
        MXh.extend(bytes("http://" + str(host), 'utf-8'))
        MXh.extend(bytes(MeW.ekO, 'utf-8'))
        MXh.extend(bytes(MeW.QsG, 'utf-8'))
        MXh.extend(bytes(str(host), 'utf-8'))
        MXh.extend(bytes(MeW.ekO, 'utf-8'))
        MXh.extend(bytes(MeW.UwR, 'utf-8'))
        MXh.extend(bytes(MeW.Pzy, 'utf-8'))
        MXh.extend(bytes(MeW.vxn, 'utf-8'))
        MXh.extend(bytes(MeW.vUc, 'utf-8'))
        MXh.extend(bytes(MeW.ktR, 'utf-8'))
        MXh.extend(bytes(MeW.ekO, 'utf-8'))
        return MXh
    def ynF(self, size):
        if size <= 125:
            return 1
        elif size <= 65535:
            return 2
        return 8
    def XKT(self, value, ZDV):
        wGc = bytearray()
        EyQ = 8 * ZDV - 8
        for JlT in range(0, ZDV):
            OsQ = self.Uwe(value, EyQ - 8 * JlT)
            rGc = OsQ - (256 * int(OsQ / 256))
            wGc.extend([rGc])
        return wGc
    def Uwe(self, val, n):
        return (val % 0x100000000) >> n
import time
import zlib
import base64
class quY:
    def __init__(self):
        self._encoding = uNa.qSd
    def NRi(self):
        self._encoding = uNa.qlI
    def dWO(self, mcf, entitlement_token, session_type, user_agent, version):
        mcf.extend(bytes(chr(ETB.waX(sJO.ojR)), 'utf-8'))
        if entitlement_token is not None:
            self.tAr(mcf, ETB.Rgs(aZG.vsJ),
                                   ETB.IkZ(entitlement_token))
        if session_type is not None:
            self.tAr(mcf, ETB.Rgs(aZG.lSg),
                                   ETB.sKV(session_type))
        if user_agent is not None:
            self.tAr(mcf, ETB.Rgs(aZG.Fxg),
                                   ETB.IkZ(user_agent))
        self.tAr(mcf, ETB.Rgs(aZG.lfM),
                               ETB.sKV(version))
        self.tAr(mcf, ETB.Rgs(aZG.Xvv),
                               ETB.sKV(self._encoding))
        mcf.extend(bytes(chr(ETB.EEH), 'utf-8'))
    def qZi(self, mcf, guq, session_id):
        mcf.extend(bytes(chr(ETB.waX(sJO.KLK)), 'utf-8'))
        self.tAr(mcf, ETB.Rgs(aZG.SZC),
                               ETB.IkZ(guq.get_subject()))
        if session_id is not None and session_id >= 0:
            self.tAr(mcf, ETB.Rgs(aZG.AAX),
                                   ETB.sKV(session_id))
        nqs = guq.HNj()
        if nqs == fdd.lwB:
            self.tAr(mcf, ETB.Rgs(aZG.ODC),
                                   ETB.sKV(guq.FZC()))
        elif nqs == fdd.jgb:
            self.tAr(mcf, ETB.Rgs(aZG.BLq),
                                   ETB.sKV(guq.jrJ()))
            self.tAr(mcf, ETB.Rgs(aZG.EME),
                                   ETB.sKV((guq.get_seq() + 1)))
        self.tAr(mcf, ETB.Rgs(aZG.Xvv),
                               ETB.sKV(self._encoding))
        mcf.extend(bytes(chr(ETB.EEH), 'utf-8'))
    def Wti(self, mcf, session_id, guq):
        mcf.extend(bytes(chr(ETB.waX(sJO.vKi)), 'utf-8'))
        self.tAr(mcf, ETB.Rgs(aZG.SZC),
                               ETB.IkZ(guq.get_subject()))
        if session_id >= 0:
            self.tAr(mcf, ETB.Rgs(aZG.AAX),
                                   ETB.sKV(session_id))
        self.tAr(mcf, ETB.Rgs(aZG.Xvv),
                               ETB.sKV(self._encoding))
        mcf.extend(bytes(chr(ETB.EEH), 'utf-8'))
    def kCk(self, mcf, message, session_id):
        mcf.extend(bytes(chr(ETB.waX(sJO.fqS)), 'utf-8'))
        self.tAr(mcf, ETB.Rgs(aZG.SZC),
                               ETB.IkZ(message.get_subject()))
        if message.is_compressed():
            LbI = self.Dbf(message.get_content())
            if len(LbI) < len(message.get_content()):
                self.tAr(mcf, ETB.Rgs(aZG.Zwl),
                                       ETB.Qkf(LbI))
            else:
                self.tAr(mcf, ETB.Rgs(aZG.Zwl),
                                       ETB.Qkf(message.get_content()))
                message.set_compressed(False)
        else:
            self.tAr(mcf, ETB.Rgs(aZG.Zwl),
                                   ETB.Qkf(message.get_content()))
        if message.get_reply_to_subject() is not None:
            self.tAr(mcf, ETB.Rgs(aZG.CjW),
                                   ETB.IkZ(message.get_reply_to_subject()))
        if message.get_closure() is not None and len(message.get_content()) > 0:
            self.tAr(mcf, ETB.Rgs(aZG.PNz),
                                   ETB.IkZ(message.get_closure()))
        if session_id >= 0:
            self.tAr(mcf, ETB.Rgs(aZG.AAX),
                                   ETB.sKV(session_id))
        if message.is_retained() is True:
            self.tAr(mcf, ETB.Rgs(aZG.TJE),
                                   ETB.sKV(1))
        else:
            self.tAr(mcf, ETB.Rgs(aZG.TJE),
                                   ETB.sKV(0))
        kNo = message.get_qos()
        if kNo == QoS.GUARANTEED:
            self.tAr(mcf, ETB.Rgs(aZG.zGr),
                                   ETB.sKV(QoS.GUARANTEED))
        elif kNo == QoS.STANDARD:
            self.tAr(mcf, ETB.Rgs(aZG.zGr),
                                   ETB.sKV(QoS.STANDARD))
        if message.is_compressed():
            self.tAr(mcf, ETB.Rgs(aZG.gHn),
                                   ETB.sKV(1))
        self.tAr(mcf, ETB.Rgs(aZG.Xvv),
                               ETB.sKV(self._encoding))
        mcf.extend(bytes(chr(ETB.EEH), 'utf-8'))
    def Fuz(self, mcf, session_id):
        mcf.extend(bytes(chr(ETB.waX(sJO.TYb)), 'utf-8'))
        if session_id >= 0:
            self.tAr(mcf, ETB.Rgs(aZG.AAX),
                                   ETB.sKV(session_id))
        self.tAr(mcf, ETB.Rgs(aZG.Xvv),
                               ETB.sKV(self._encoding))
        mcf.extend(bytes(chr(ETB.EEH), 'utf-8'))
    def hrD(self, mcf, guq, AMA, epoch, session_id):
        mcf.extend(bytes(chr(ETB.waX(sJO.PUBLISH_ACK)), 'utf-8'))
        self.tAr(mcf, ETB.Rgs(aZG.SZC),
                               ETB.IkZ(guq))
        self.tAr(mcf, ETB.Rgs(aZG.EME),
                               ETB.sKV(AMA))
        self.tAr(mcf, ETB.Rgs(aZG.BLq),
                               ETB.sKV(epoch))
        self.tAr(mcf, ETB.Rgs(aZG.AAX),
                               ETB.sKV(session_id))
        self.tAr(mcf, ETB.Rgs(aZG.Xvv),
                               ETB.sKV(self._encoding))
        mcf.extend(bytes(chr(ETB.EEH), 'utf-8'))
    def tAr(self, mcf, TEW, ALH):
        mcf.append(TEW)
        mcf.extend(ALH)
        mcf.append(ETB.tWC)
    def Dbf(self, gYS):
        try:
            vGU = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
            jlY = vGU.compress(gYS)
            jlY += vGU.flush()
            dyA = base64.b64encode(jlY)
        except zlib.error as ex:
            return gYS
        return dyA
    def ioR(self, ALH):
        try:
            mJx = base64.b64decode(ALH)
            if not mJx:
                return ALH
            gNp = zlib.decompress(mJx, -15)
        except base64.binascii.Error as ex:
            return ALH
        except zlib.error as ex:
            return ALH
        return gNp
import socket
import ssl
class naa:
    @staticmethod
    def zxa(host, tig, encryption, socket_timeout_seconds):
        FgL = None
        if encryption is False:
            FgL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            FgL.settimeout(socket_timeout_seconds)
            FgL.connect((host, tig))
        else:
            jsY = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            jsY.settimeout(socket_timeout_seconds)
            try:
                FgL = ssl.wrap_socket(jsY, ssl_version=ssl.PROTOCOL_TLSv1)
            except:
                FgL = ssl.wrap_socket(jsY)
            FgL.connect((host, tig))
        return FgL
class ewp:
    lkF = 80
    glg = 443
    kwj = 100
    def __init__(self, address, encryption):
        self._weight = ewp.kwj
        self._unparsed_address = address
        bwj = address.find(' ')
        if bwj != -1:
            self._weight = int(address[0:bwj])
            if self._weight < 0 or self._weight > 100:
                raise ValueError(
                    "The Weight of a clust Member must be between 0 and 100, Weight: " + str(self._weight))
        JlT = address.find(']')
        WDE = address.rfind(":")
        nZw = None
        tig = None
        if WDE != -1 and WDE + 1 < len(address) and WDE >= JlT:
            nZw = address[0:WDE]
            tig = int(address[WDE + 1:])
        else:
            nZw = address
            if encryption:
                tig = self.glg
            else:
                tig = self.lkF
        if tig < 0 or tig > 65535:
            raise ValueError("Invalid Port number")
        if nZw == "":
            raise ValueError("Clust Member with null address")
        if nZw == "*":
            raise ValueError("Wildcard address (*) cannot be used to define a clust Member")
        self._address = nZw
        self._port = tig
    def iis(self):
        return self._weight
    def Ocs(self):
        return self._port
    def Gsa(self):
        return self._address
    def EIn(self, PNn):
        if (self._address == PNn._address):
            if self._port == PNn._port:
                return True
        return False
    def aLt(self):
        return self._unparsed_address
    def __repr__(self) -> str:
        bIs = "[Host="
        bIs += str(self.Gsa())
        bIs += ", Port="
        bIs += str(self.Ocs())
        bIs += "]"
        return bIs
import random
class eAW:
    def __init__(self, servers, encryption):
        self._members = []
        self._inactive_members = []
        self._current_member = None
        for JlT in range(0, len(servers)):
            self._members.append(ewp(servers[JlT], encryption))
    def Lie(self):
        bBD = self.FSf()
        if len(bBD) == 0:
            self._inactive_members = []
            bBD = list(self._members)
        LLm = self.umE(bBD)
        self._current_member = bBD[LLm]
        return self._current_member
    def FSf(self):
        bBD = list(self._members)
        for hhP in self._members:
            for SnC in self._inactive_members:
                if hhP.EIn(SnC):
                    bBD.remove(hhP)
        return bBD
    def umE(self, bBD):
        LLm = -1
        haR = 0
        for hhP in bBD:
            haR = haR + hhP.iis()
        if haR == 0:
            LLm = int(len(bBD) * random.uniform(0, 1))
        else:
            eyM = int(haR * random.uniform(0, 1))
            haR = 0
            for JlT in range(0 < len(bBD)):
                haR = haR + bBD[JlT].iis()
                if haR > eyM:
                    LLm = JlT
                    break
        return LLm
    def sNv(self):
        return self._current_member
    def AOg(self, PNn):
        self._inactive_members.append(PNn)
import threading
class wsQ:
    klX = 0
    TUX = 1
class Pwp:
    def __init__(self):
        self._state = wsQ.klX
        self._lock = threading.Lock()
    def GQZ(self, state):
        with self._lock:
            self._state = state
    def pXd(self):
        with self._lock:
            return self._state
class xSj:
    @staticmethod
    def search(ALH, dataLength, pattern, patternLength):
        xoF = [0] * patternLength
        WDE = 0
        len = 0
        JlT = 1
        while JlT < patternLength:
            if pattern[JlT] == pattern[len]:
                len += 1
                xoF[JlT] = len
                JlT += 1
            else:
                if len != 0:
                    len = xoF[len - 1]
                else:
                    xoF[JlT] = 0
                    JlT += 1
        JlT = 0
        while JlT < dataLength:
            if pattern[WDE] == ALH[JlT]:
                JlT += 1
                WDE += 1
            if WDE == patternLength:
                return JlT - WDE
            elif JlT < dataLength and pattern[WDE] != ALH[JlT]:
                if WDE != 0:
                    WDE = xoF[WDE - 1]
                else:
                    JlT += 1
        return -1
import abc
class xSS(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Fpg(self, aer):
        pass
import abc
class oMq(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def YFq(self, aer):
        pass
    @abc.abstractmethod
    def yIb(self):
        pass
import abc
class Lge(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Ntf(self, status, info):
        pass
    @abc.abstractmethod
    def OUt(self, message):
        pass
import abc
class iCr(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gvX(self, Itu, connection, keep_alive):
        pass
    @abc.abstractmethod
    def ArA(self, Itu, connection, disconnect_info):
        pass
    @abc.abstractmethod
    def llM(self, connection):
        pass
    @abc.abstractmethod
    def cancel(self):
        pass
    @abc.abstractmethod
    def urp(self, value):
        pass
class nbw(MigratoryDataMessage):
    def __init__(self, _subject, _content, closure, retained, _message_type, qos_, _reply_subject, _compression):
        super().__init__(_subject, _content, closure)
        self._retained = retained
        self._message_type = _message_type
        self.HQg = qos_
        self._reply_to_subject = _reply_subject
        self._compression = _compression
    def Wmn(self, AMA):
        self._seq = AMA
    def EZA(self, epoch):
        self._epoch = epoch
class uCm:
    def __init__(self, ioi, status, info, migratory_data_message):
        self.ioi = ioi
        self.status = status
        self.info = info
        self.migratory_data_message = migratory_data_message
class AEe:
    VhZ = 0
    OUB = 1
class uTI:
    ojR = 1,
    Bwc = 2,
    nvP = 3,
    OrY = 4,
    KLK = 5,
    vKi = 6,
    klX = 7,
    aQV = 8,
    zod = 9,
    esg = 10,
    dQH = 11,
    hCP = 12
class gby:
    def __init__(self, operation):
        self.operation = operation
        self.connection_uuid = None
        self.disconnect_reason = None
        self.Pnj = None
        self.history = None
        self.md_message = None
        self.message = None
        self.info = None
    @staticmethod
    def kUm():
        return gby(uTI.ojR)
    @staticmethod
    def JDj(Pnj, history):
        aer = gby(uTI.KLK)
        aer.Pnj = Pnj
        aer.history = history
        return aer
    @staticmethod
    def cjl(Pnj):
        aer = gby(uTI.vKi)
        aer.Pnj = Pnj
        return aer
    @staticmethod
    def WNa(message):
        aer = gby(uTI.dQH)
        aer.md_message = message
        return aer
    @staticmethod
    def iPq(message):
        aer = gby(uTI.esg)
        aer.message = message
        return aer
    @staticmethod
    def TNU(uuid, disconnect_reason):
        aer = gby(uTI.klX)
        aer.connection_uuid = uuid
        aer.disconnect_reason = disconnect_reason
        return aer
    @staticmethod
    def Erm(disconnect_info):
        aer = gby(uTI.zod)
        aer.info = disconnect_info
        return aer
    @staticmethod
    def JsS():
        aer = gby(uTI.aQV)
        return aer
    @staticmethod
    def Plt():
        aer = gby(uTI.Bwc)
        return aer
    @staticmethod
    def Tbv():
        aer = gby(uTI.OrY)
        return aer
    @staticmethod
    def szz():
        aer = gby(uTI.nvP)
        return aer
    @staticmethod
    def nck():
        aer = gby(uTI.hCP)
        return aer
import re
class jQt:
    hlF = 0
    Iww = 1
    ZmJ = 2
class gHQ:
    nTx = "OK"
    kuu = "DENY"
    SZc = "connection_active_close_keep_alive"
    BBf = "connection_active_close_seq_higher"
    XHM = "connection_passive_close"
    sMx = "connection_error"
    eWz = "cache_ok"
    OXT = "cache_ok_no_new_message"
    ctf = "cache_ok_new_epoch"
    SLM = "end"
    AVo = "^\/([^\/]+\/)*([^\/]+|\*)$"
    @staticmethod
    def qin(WCL):
        if not isinstance(WCL, str):
            return False
        fhT = re.compile(gHQ.AVo)
        if fhT.search(WCL) is not None:
            return True
        return False
    @staticmethod
    def XvP(Pnj):
        bGe = []
        for guq in Pnj:
            if guq is not None and gHQ.qin(guq):
                bGe.append(guq)
        return bGe
    @staticmethod
    def ubI(Wex, recv_seq, recv_seq_id, listener_notifier, logger):
        if Wex.jrJ() != recv_seq_id:
            Wex.Wmn(recv_seq)
            Wex.jBO(recv_seq_id)
            return jQt.hlF
        if recv_seq <= Wex.get_seq():
            return jQt.Iww
        if recv_seq == Wex.get_seq() + 1:
            if Wex.ucU() == fdd.jgb:
                Wex.emd()
                listener_notifier.Ntf(MigratoryDataClient.NOTIFY_DATA_SYNC, Wex.get_subject())
                logger.debug(str(fqD.SgG) + str(
                    MigratoryDataClient.NOTIFY_DATA_SYNC) + str(Wex))
            Wex.Wmn(Wex.get_seq() + 1)
            return jQt.hlF
        if Wex.IbH() > 0:
            logger.info("Missing Messages: expected message with sequence number: " + str(
                Wex.get_seq() + 1) + ", received instead message with sequence number:  " + str(recv_seq) + " !")
            return jQt.ZmJ
        logger.info("Reset sequence: '" + str(Wex.get_seq() + 1) + "'. The new sequence is: '" + str(recv_seq) + "' !")
        Wex.Wmn(recv_seq)
        listener_notifier.Ntf(MigratoryDataClient.NOTIFY_DATA_RESYNC, Wex.get_subject())
        logger.debug(
            fqD.SgG + MigratoryDataClient.NOTIFY_DATA_RESYNC + str(Wex))
        return jQt.hlF
    @staticmethod
    def jxf(Wex, recv_seq, recv_seq_id, listener_notifier, logger):
        if Wex.jrJ() != recv_seq_id:
            Wex.Wmn(recv_seq)
            Wex.jBO(recv_seq_id)
            return jQt.hlF
        if recv_seq <= Wex.get_seq():
            return jQt.Iww
        if Wex.ucU() == fdd.jgb:
            Wex.emd()
        Wex.Wmn(recv_seq)
        return jQt.hlF
import threading
class inR:
    def __init__(self):
        self._subject_table = {}
        self._empty_subject = TOP("", 0)
        self._lock = threading.Lock()
    def jbq(self, Pnj, history):
        with self._lock:
            for guq in Pnj:
                YRz = self._subject_table.get(guq)
                if YRz is None:
                    self._subject_table[guq] = TOP(guq, history)
    def NOL(self, Pnj):
        with self._lock:
            amm = []
            for guq in Pnj:
                YRz = self._subject_table.get(guq)
                if YRz is not None:
                    try:
                        del self._subject_table[guq]
                        amm.append(YRz)
                    except KeyError:
                        pass
            return amm
    def SRq(self):
        with self._lock:
            return self._subject_table.keys()
    def get_subject(self, guq):
        with self._lock:
            return self._subject_table.get(guq)
    def EVF(self, guq):
        with self._lock:
            qZw = self._subject_table.get(guq)
            if qZw is None:
                return False
            else:
                return True
    def viu(self):
        with self._lock:
            return self._empty_subject
    def tpi(self):
        with self._lock:
            for WLq in self._subject_table:
                self._subject_table[WLq].wan()
import threading
import queue
import time
class mzr(oMq, threading.Thread):
    def __init__(self, knm, logger):
        threading.Thread.__init__(self)
        self._logger = logger
        self._event_handler = knm
        self._control_queue = queue.Queue()
        self._running = UsT(True)
    def run(self):
        while self._running.UHJ():
            self.Abs()
        self._event_handler.Fpg(gby.Plt())
        self._logger.debug("Exit single_thread_event_loop thread")
    def YFq(self, aer):
        if self._running.UHJ():
            self._control_queue.put(aer)
    def Abs(self):
        try:
            BQU = self._control_queue.get(True, 0.1)
            if BQU is not None:
                self._event_handler.Fpg(BQU)
        except queue.Empty:
            pass
    def yIb(self):
        self._running.NuT(False)
class DkP:
    @staticmethod
    def xas(MXh, GAH):
        eCX = rWc(-1, -1)
        if GAH == len(MXh.mcf):
            return eCX
        VON = GAH
        DLB = 2
        hFx = 0
        kwp = 0
        SeO = len(MXh.mcf) - VON
        if SeO < DLB:
            return eCX
        b = MXh.mcf[VON]
        bjx = (b >> 7) & 0x01
        uhj = b & 0x40
        cGj = b & 0x20
        wiI = b & 0x10
        if bjx != 1 or uhj != 0 or cGj != 0 or wiI != 0:
            return eCX
        VON += 1
        b = MXh.mcf[VON]
        zMn = b & 0x7F
        if zMn < 126:
            kwp = 0
            hFx = zMn
        elif zMn == 126:
            kwp = 2
            if SeO < DLB + kwp:
                return eCX
            qLt = bytearray()
            for JlT in range(VON + 1, VON + 1 + kwp):
                qLt.extend([MXh.mcf[JlT]])
            hFx = DkP.eoF(qLt)
            VON += kwp
        elif zMn == 127:
            kwp = 8
            if SeO < DLB + kwp:
                return eCX
            qLt = bytearray()
            for JlT in range(VON + 1, VON + 1 + kwp):
                qLt.extend([MXh.mcf[JlT]])
            hFx = DkP.eoF(qLt)
            VON += kwp
        if SeO < (DLB + kwp + hFx):
            return eCX
        VON += 1
        return rWc(VON, VON + hFx)
    @staticmethod
    def eoF(ALH):
        if len(ALH) == 2:
            return ((ALH[0] & 0xFF) << 8) | (ALH[1] & 0xFF)
        else:
            return ((ALH[4] & 0x7F) << 24) | ((ALH[5] & 0xFF) << 16) | ((ALH[6] & 0xFF) << 8) | (ALH[7] & 0xFF)
import re
class Qfc:
    @staticmethod
    def GbG(MXh, logger):
        MMW = MXh.VON
        if MXh.mcf[MMW] == 72:
            MMW = Qfc.ugR(MXh)
        if MMW == -1:
            return []
        MXh.GAH(MMW)
        BZl = []
        while True:
            if MMW >= len(MXh.mcf):
                return BZl
            if MXh.mcf[MMW] == ETB.qvi:
                MMW += 1
            else:
                try:
                    Zzp = DkP.xas(MXh, MMW)
                except IndexError:
                    Zzp = rWc(-1, -1)
                brl = Zzp.MSp()
                eVf = Zzp.xIf()
                if brl == -1:
                    return BZl
                while True:
                    JlT = Qfc.ZAJ(MXh, brl, eVf, ETB.EEH)
                    if JlT == -1:
                        break
                    gNU = Qfc.VUj(MXh, brl + 1, JlT, logger)
                    if gNU is not None:
                        message = joo(ETB.kLV[MXh.mcf[brl]], gNU)
                        BZl.append(message)
                    brl = JlT + 1
                    MXh.GAH(brl)
                MMW = MXh.VON
    @staticmethod
    def uou(MXh, logger):
        VON = Qfc.Ois(MXh)
        if VON == -1:
            return []
        MXh.GAH(VON)
        BZl = []
        while True:
            JlT = Qfc.ZAJ(MXh, VON, len(MXh.mcf), ETB.EEH)
            if JlT == -1:
                break
            if MXh.mcf[VON] == 72:
                BZl.extend(Qfc.uou(MXh, logger))
                break
            gNU = Qfc.VUj(MXh, VON + 1, JlT, logger)
            if gNU is not None:
                message = joo(ETB.kLV[MXh.mcf[VON]], gNU)
                BZl.append(message)
            VON = JlT + 1
            MXh.GAH(VON)
        return BZl
    @staticmethod
    def Ois(MXh):
        VON = MXh.VON
        if MXh.mcf[VON] == 72:
            Skg = "\r\n\r\n".encode("utf-8")
            TyL = xSj.search(MXh.mcf[VON:], len(MXh.mcf), Skg,
                                                   len(Skg))
            if TyL != -1:
                VON += TyL + len(Skg)
                MXh.GAH(VON)
            else:
                return -1
        return VON
    @staticmethod
    def ugR(MXh):
        Skg = "\r\n\r\n".encode("utf-8")
        VON = MXh.VON
        JlT = xSj.search(MXh.mcf[VON:], len(MXh.mcf), Skg,
                             len(Skg))
        if JlT == -1:
            return -1
        VON = JlT + len(Skg)
        return VON
    @staticmethod
    def ZAJ(MXh, start, end, value):
        for JlT in range(start, end):
            if MXh.mcf[JlT] == value:
                return JlT
        return -1
    @staticmethod
    def VUj(MXh, start, end, logger):
        gNU = None
        while True:
            if start >= end:
                break
            fYg = MXh.mcf[start]
            jgI = Qfc.ZAJ(MXh, start + 1, end, ETB.tWC)
            if jgI == -1:
                logger.trace(
                    "Received an invalid msg: Hdr end missing - msg ignored, Hdr Position: " + str(
                        start) + ", " + str(MXh.mcf[start:end]))
                return None
            TEW = ETB.Kbv(fYg)
            if TEW is None:
                logger.trace("Received an unknown Hdr - Hdr ignored, Hdr Position: " + str(MXh.mcf))
                start = jgI + 1
            start = start + 1
            if gNU is None:
                gNU = {}
            value = None
            LNZ = ETB.YNl(TEW)
            JZF = MXh.mcf[start:jgI]
            if LNZ == For.wiZ:
                value = ETB.wxD(JZF)
            elif LNZ == For.BTj:
                dqH = ETB.Teg(JZF)
                value = dqH.decode('utf-8')
            elif LNZ == For.Cph:
                value = ETB.Teg(JZF)
            elif LNZ == For.gZQ:
                value = JZF
            hgc = gNU.get(TEW)
            if hgc is None:
                gNU[TEW] = value
            else:
                values = [hgc, value]
                gNU[TEW] = values
            start = jgI + 1
        return gNU
import threading
import queue
class OsY(Lge, threading.Thread):
    def __init__(self, listener):
        super().__init__()
        self._queue = queue.Queue()
        self._run = True
        self._migratory_data_listener = listener
    def Ntf(self, status, info):
        self._queue.put(uCm(AEe.VhZ, status, info, None))
    def OUt(self, message):
        self._queue.put(uCm(AEe.OUB, None, None, message))
    def run(self):
        while self._run:
            try:
                hZQ = self._queue.get(True, 0.1)
                if self._migratory_data_listener is not None:
                    if hZQ.ioi == AEe.VhZ:
                        self._migratory_data_listener.on_status(hZQ.status, hZQ.info)
                    elif hZQ.ioi == AEe.OUB:
                        self._migratory_data_listener.on_message(hZQ.migratory_data_message)
            except queue.Empty:
                pass
    def oBS(self):
        self._run = False
import socket
import uuid
import threading
class lgT:
    ojR = 0
    CcI = 1
class IVo:
    TQh = 0
    OrY = 1
    Quq = 2
class eZN:
    WBN = 0
    onf = 1
    fca = 2
class Connection:
    def __init__(self, configuration, listener_notifier, Yxr, ROp, client_state, logger):
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
        self._app_state = IVo.Quq
        self._node_type = eZN.WBN
        self._subject_manager = inR()
        self._logger = logger
        self._configuration = configuration
        self._listener_notifier = listener_notifier
        self._cluster = Yxr
        self._scheduler = ROp
        self._client_state = client_state
        self._push_encoder = quY()
        self._transport_type = self._configuration.trans_type
        if self._transport_type == yhd.HTTP:
            self._transport_encoder = FCV()
            self._push_encoder.NRi()
        else:
            self._transport_encoder = MeW()
        self._message_listener = liM()
        self._message_listener.ceV(self)
        self._cluster_token = None
    def axH(self):
        return self._message_listener
    def Tpi(self, MXh):
        BZl = None
        if self._transport_type == yhd.Dom:
            BZl = Qfc.GbG(MXh, self._logger)
        else:
            BZl = Qfc.uou(MXh, self._logger)
        if len(BZl) > 0:
            self.uRm(BZl)
        else:
            self._loop.YFq(gby.nck())
            self._logger.debug(str(fqD.tPH))
    def uRm(self, BZl):
        for JlT in range(0, len(BZl)):
            message = BZl[JlT]
            if message.operation == sJO.CLIENT_PUBLISH_RESPONSE or message.operation == sJO.dQH or message.operation == sJO.cRR or message.operation == sJO.IzP \
                    or message.operation == sJO.KLK or message.operation == sJO.vKi or message.operation == sJO.ojR:
                self._loop.YFq(gby.iPq(message))
                self._logger.debug(fqD.yRC + str(message))
            elif message.operation == sJO.TYb:
                self._loop.YFq(gby.nck())
                self._logger.debug(str(fqD.tPH))
            elif message.operation == sJO.fqS:
                break
            else:
                self._logger.warn("No existing operation for msg: " + str(message))
    def connect(self):
        Itu = uuid.uuid4()
        self.sae(Itu)
        if self._socket is not None:
            self.disconnect()
        try:
            PNn = self._cluster.Lie()
            self._logger.info("Connecting to the clust Member: " + str(self._cluster.sNv()))
            self._socket = naa.zxa(PNn.Gsa(), PNn.Ocs(),
                                                    self._configuration.encryption,
                                                    self._configuration.socket_timeout_seconds)
            self._writer = XBk(self._socket)
            self._writer.start()
            self._reader = ZrB(self._socket, self, Itu)
            self._reader.start()
            MXh = self._transport_encoder.AZx(self._cluster.sNv().Gsa(),
                                                                  self._configuration.encryption)
            if len(MXh.mcf) > 0:
                self._writer.RUH(MXh.mcf)
        except:
            self._logger.info("Failed to Connect: " + str(self._cluster.sNv()))
            self._scheduler.ArA(Itu, self, gHQ.sMx)
            return
        self._scheduler.gvX(Itu, self, lgT.ojR)
        self._scheduler.llM(self)
        self.jsZ()
    def jsZ(self):
        MXh = self._transport_encoder.EWQ(self._cluster.sNv().Gsa())
        Jaf = self._configuration
        self._push_encoder.dWO(MXh.mcf, Jaf.entitlement_token, Jaf.session_type, Jaf.user_agent, Jaf.lfM)
        self._transport_encoder.WTN(MXh)
        self._write(MXh.INS())
    def xYl(self):
        self.disconnect()
        if self._app_state == IVo.TQh:
            return
        self._cluster.AOg(self._cluster.sNv())
        self._reconnected = True
        self.connect()
    def disconnect(self):
        if self._socket is not None:
            self._socket.close()
        if self._writer is not None:
            self._writer.oBS()
        if self._reader is not None:
            self._reader.oBS()
        self._socket = None
        self._writer = None
        self._reader = None
        self._scheduler.cancel()
        self.hXA()
    def uyx(self):
        self._app_state = IVo.TQh
        self.disconnect()
    def hXA(self):
        self._client_state.GQZ(wsQ.klX)
        self._session = -1
        self._session_received = False
    def FjH(self):
        if self._app_state != IVo.Quq:
            return
        self._logger.info("Call pause")
        self._app_state = IVo.OrY
        self.disconnect()
    def resume(self):
        if self._app_state != IVo.OrY:
            return
        self._logger.info("Call resume")
        self._app_state = IVo.Quq
        self.REH()
        self.xYl()
    def subscribe(self, Pnj, history):
        if Pnj is None or len(Pnj) == 0:
            return
        Pnj = gHQ.XvP(Pnj)
        IrJ = list(set(Pnj) - set(self._subject_manager.SRq()))
        if len(IrJ) == 0:
            return
        self._subject_manager.jbq(IrJ, history)
        if self._client_state.pXd() == wsQ.TUX:
            self.jph(IrJ)
    def jph(self, subjects_string):
        MXh = self._transport_encoder.EWQ(self._cluster.sNv().Gsa())
        for guq in subjects_string:
            self.NlV(MXh, self._subject_manager.get_subject(guq))
        self._transport_encoder.WTN(MXh)
        self._write(MXh.INS())
    def _write(self, message):
        if self._writer is not None:
            self._writer.RUH(message)
            try:
                self._logger.debug(fqD.lLA + message.decode('utf-8'))
            except UnicodeDecodeError:
                self._logger.debug(fqD.lLA + str(message))
    def NlV(self, MXh, guq):
        self._push_encoder.qZi(MXh.mcf, guq, self._session)
    def unsubscribe(self, subjects_string):
        if subjects_string is None or len(subjects_string) == 0:
            return
        JDA = list(set(subjects_string) & set(self._subject_manager.SRq()))
        if len(JDA) == 0:
            return
        amm = self._subject_manager.NOL(JDA)
        if self._client_state.pXd() == wsQ.TUX:
            self.zww(amm)
    def zww(self, Pnj):
        MXh = self._transport_encoder.EWQ(self._cluster.sNv().Gsa())
        for guq in Pnj:
            self._push_encoder.Wti(MXh.mcf, self._session, guq)
        self._transport_encoder.WTN(MXh)
        self._write(MXh.INS())
    def publish(self, message):
        if self._client_state.pXd() != wsQ.TUX:
            self.lFO(MigratoryDataClient.NOTIFY_PUBLISH_FAILED, message)
        self.Ute(message)
    def Ute(self, message):
        jtY = message.get_reply_to_subject()
        if jtY is not None and gHQ.qin(
                jtY) is True and self._subject_manager.EVF(jtY) is False:
            self.subscribe([jtY], 0)
        MXh = self._transport_encoder.EWQ(self._cluster.sNv().Gsa())
        self._push_encoder.kCk(MXh.mcf, message, self._session)
        self._transport_encoder.WTN(MXh)
        if self._max_message_size is not None and (len(MXh.mcf) - MXh.VON) > self._max_message_size:
            self.lFO(MigratoryDataClient.NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED, message)
            return
        closure = message.get_closure()
        if closure is not None and len(closure) > 0:
            self._publish_closures.append(closure)
        self._write(MXh.INS())
    def jno(self):
        for closure in self._publish_closures:
            self._listener_notifier.Ntf(
                fqD.Vpe + " " + closure)
        self._publish_closures = []
    def lFO(self, notification, message):
        if message is not None and message.get_closure() is not None:
            self._listener_notifier.Ntf(notification, message.get_closure())
    def fDB(self):
        MXh = self._transport_encoder.EWQ(self._cluster.sNv().Gsa())
        self._push_encoder.Fuz(MXh.mcf, self._session)
        self._transport_encoder.WTN(MXh)
        if self._writer is not None:
            self._write(MXh.INS())
    def ArA(self, uuid, disconnect_reason, from_):
        if uuid == self.cHD():
            self._client_state.GQZ(wsQ.klX)
            self._loop.YFq(gby.TNU(uuid, disconnect_reason))
            self._logger.debug(
                fqD.SCB + str(self._current_connection_id) + str(from_))
    def bws(self, disconnect_info):
        self._logger.error("[" + str(disconnect_info) + "] [" + str(self._cluster.sNv()) + "]")
        self._logger.info("Lost connection with the clust Member: " + str(self._cluster.sNv()))
        if self._session_received is False:
            self._servers_down_count += 1
            if self._is_server_down is False:
                if self._servers_down_count >= self._configuration.servers_down_before_notify:
                    self._is_server_down = True
                    self._listener_notifier.Ntf(MigratoryDataClient.NOTIFY_SERVER_DOWN,
                                                         self._cluster.sNv().aLt())
                    self._logger.debug(fqD.raC + str(disconnect_info))
    def REH(self):
        self._is_server_down = False
        self._servers_down_count = 0
    def kzM(self):
        self._logger.info("Connected to the clust Member: " + str(self._cluster.sNv()))
        self.REH()
        self._listener_notifier.Ntf(MigratoryDataClient.NOTIFY_SERVER_UP,
                                             self._cluster.sNv().aLt())
        self._logger.debug(fqD.iMT + MigratoryDataClient.NOTIFY_SERVER_UP + str(
            self.cHD()))
    def JUz(self):
        return self._reconnect_retries
    def sWW(self):
        self._reconnect_retries += 1
        return self._reconnect_retries
    def sae(self, Itu):
        with self._lock:
            self._current_connection_id = Itu
    def cHD(self):
        with self._lock:
            return self._current_connection_id
    def HQc(self, loop):
        self._loop = loop
    def VcU(self):
        return self._loop
    def Umj(self):
        return self._app_state
class liM:
    def __init__(self):
        self._connection = None
    def ceV(self, connection):
        self._connection = connection
    def on_message(self, message):
        self._connection._scheduler.gvX(self._connection.cHD(),
                                                                   self._connection, lgT.CcI)
        gNU = message.gNU
        if message.operation == sJO.KLK:
            self.VcJ(gNU)
        elif message.operation == sJO.dQH:
            self.Vdd(gNU, message)
        elif message.operation == sJO.ojR:
            self.Qad(gNU)
        elif message.operation == sJO.CLIENT_PUBLISH_RESPONSE:
            self.EdC(gNU)
        elif message.operation == sJO.vKi:
            self.sXE()
        elif message.operation == sJO.cRR:
            self.DFp(gNU)
        elif message.operation == sJO.IzP:
            self.bvC(gNU)
        else:
            self._connection._logger.warn("No existing operation for msg: " + str(message))
    def Qad(self, gNU):
        qoi = gNU.get(aZG.AAX)
        if qoi is not None:
            self._connection.kzM()
            self._connection._session = qoi
            self._connection._session_received = True
            self._connection._reconnect_retries = 0
            jsx = gNU.get(aZG.VPu)
            if jsx is not None and jsx == 1:
                self._connection._node_type = eZN.onf
            if jsx is not None and jsx == 2:
                self._connection._node_type = eZN.fca
            yjp = gNU.get(aZG.dbx)
            if yjp is not None:
                self._connection._scheduler.urp(yjp)
                self._connection._scheduler.gvX(
                    self._connection.cHD(), self._connection, lgT.CcI)
            self._connection._client_state.GQZ(wsQ.TUX)
            CnI = gNU.get(aZG.Iov)
            self.kAN(CnI)
            Pvl = gNU.get(aZG.Oaa)
            if Pvl is not None:
                self._connection._max_message_size = Pvl
            Pnj = self._connection._subject_manager.SRq()
            if len(Pnj) > 0:
                self._connection.jph(Pnj)
    def VcJ(self, gNU):
        pass
    def sXE(self):
        pass
    def Vdd(self, gNU, msg):
        guq = gNU.get(aZG.SZC)
        Wex = self._connection._subject_manager.get_subject(guq)
        if Wex is None:
            return
        CnI = gNU.get(aZG.Iov)
        self.kAN(CnI)
        ALH = gNU.get(aZG.Zwl)
        closure = gNU.get(aZG.PNz)
        retained = False
        gQh = gNU.get(aZG.TJE)
        if gQh is not None and gQh == 1:
            retained = True
        ryL = False
        SjK = gNU.get(aZG.gHn)
        if SjK is not None and SjK == 1:
            ryL = True
        if ryL == True:
            ALH = self._connection._push_encoder.ioR(ALH)
        LND = MessageType.UPDATE
        ioi = gNU.get(aZG.opV)
        if ioi is not None:
            if ioi == aqF.SNAPSHOT:
                LND = MessageType.SNAPSHOT
            elif ioi == aqF.RECOVERED:
                LND = MessageType.RECOVERED
            elif ioi == aqF.HISTORICAL:
                LND = MessageType.HISTORICAL
        HQg = QoS.GUARANTEED
        Isr = gNU.get(aZG.zGr)
        if Isr is not None and Isr == QoS.STANDARD:
            HQg = QoS.STANDARD
        if self._connection._node_type == eZN.onf and HQg == QoS.GUARANTEED:
            message = nbw(guq, ALH, closure, retained, LND, QoS.GUARANTEED,
                                                   gNU.get(aZG.CjW), ryL)
            AMA = gNU.get(aZG.EME)
            lbh = gNU.get(aZG.BLq)
            message.Wmn(AMA)
            message.EZA(lbh)
            kcH = gHQ.ubI(Wex, AMA, lbh, self._connection._listener_notifier,
                                             self._connection._logger)
            if kcH == jQt.hlF:
                self._connection._listener_notifier.OUt(message)
                self._connection._logger.debug(fqD.SgG + str(message))
            elif kcH == jQt.ZmJ:
                self._connection.ArA(self._connection.cHD(),
                                           gHQ.BBf, "seq_higher")
        elif self._connection._node_type == eZN.fca and HQg == QoS.GUARANTEED:
            message = nbw(guq, ALH, closure, retained, LND, QoS.GUARANTEED,
                                                   gNU.get(aZG.CjW), ryL)
            AMA = gNU.get(aZG.EME)
            lbh = gNU.get(aZG.BLq)
            message.Wmn(AMA)
            message.EZA(lbh)
            kcH = gHQ.jxf(Wex, AMA, lbh, self._connection._listener_notifier,
                                             self._connection._logger)
            if kcH == jQt.hlF:
                self._connection._listener_notifier.OUt(message)
                self._connection._logger.debug(fqD.SgG + str(message))
        else:
            message = nbw(guq, ALH, closure, retained, LND, QoS.STANDARD,
                                                   gNU.get(aZG.CjW), ryL)
            self._connection._listener_notifier.OUt(message)
            self._connection._logger.debug(fqD.SgG + str(message))
    def EdC(self, gNU):
        if gNU is None:
            return
        closure = gNU.get(aZG.PNz)
        siS = gNU.get(aZG.rqV)
        if closure is not None and siS is not None:
            status = MigratoryDataClient.NOTIFY_PUBLISH_FAILED
            if siS == gHQ.kuu:
                status = MigratoryDataClient.NOTIFY_PUBLISH_DENIED
            elif siS == gHQ.nTx:
                status = MigratoryDataClient.NOTIFY_PUBLISH_OK
            self._connection._listener_notifier.Ntf(status, closure)
            self._connection._logger.debug(
                fqD.tRt + str(status) + str(closure))
            if self._connection._publish_closures.__contains__(closure):
                self._connection._publish_closures.remove(closure)
    def DFp(self, gNU):
        JiC = gNU.get(aZG.rqV)
        guq = gNU.get(aZG.SZC)
        if JiC is not None and guq is not None:
            blB = True
            UPH = MigratoryDataClient.NOTIFY_SUBSCRIBE_DENY
            if JiC == pSU.iZf:
                UPH = MigratoryDataClient.NOTIFY_SUBSCRIBE_ALLOW
                blB = False
            elif JiC == pSU.ucH:
                UPH = MigratoryDataClient.NOTIFY_SUBSCRIBE_DENY
            if blB is True:
                self._connection._subject_manager.NOL([guq])
            self._connection._listener_notifier.Ntf(UPH, guq)
            self._connection._logger.debug(fqD.KtW + str(
                guq + str(JiC) + str(UPH)))
    def bvC(self, gNU):
        guq = gNU.get(aZG.SZC)
        status = gNU.get(aZG.opV)
        self._connection._logger.info("Recovery Status for subj: " + str(guq) + " is:" + str(status))
        if gHQ.SLM == status:
            Pnj = self._connection._subject_manager.SRq()
            for s in Pnj:
                Wex = self._connection._subject_manager.get_subject(s)
                Bzd = Wex.SvO()
                if gHQ.eWz == Bzd or gHQ.ctf == Bzd or gHQ.OXT == Bzd:
                    Wex.GgL()
                else:
                    Wex.iwQ()
        else:
            Wex = self._connection._subject_manager.get_subject(guq)
            if Wex is not None:
                Wex.zIF(status)
    def kAN(self, _received_cluster_token):
        if _received_cluster_token is not None:
            if self._connection._cluster_token is None:
                self._connection._cluster_token = _received_cluster_token
            else:
                if _received_cluster_token != self._connection._cluster_token:
                    self._connection._cluster_token = _received_cluster_token
                    self._connection._subject_manager.tpi()
import uuid
class yhd:
    HTTP = 0
    Dom = 1
class XDE:
    def __init__(self, session_type, user_agent):
        self.lfM = 6
        self.id = str(uuid.uuid4())
        self.session_type = session_type
        self.user_agent = user_agent + ", version:" + str(self.lfM)
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
        self.trans_type = yhd.Dom
    def jbq(self, Pnj, history):
        for guq in Pnj:
            self._subjects[guq] = history
    def rMp(self, Pnj):
        for guq in Pnj:
            try:
                del self._subjects[guq]
            except KeyError:
                pass
    def get_subjects(self):
        return self._subjects
class Mnt(xSS):
    def __init__(self, connection, ROp):
        self._connection = connection
        self._scheduler = ROp
    def Fpg(self, aer):
        if aer.operation == uTI.ojR:
            self._connection.connect()
        elif aer.operation == uTI.KLK:
            self._connection.subscribe(aer.Pnj, aer.history)
        elif aer.operation == uTI.vKi:
            self._connection.unsubscribe(aer.Pnj)
        elif aer.operation == uTI.dQH:
            self._connection.publish(aer.md_message)
        elif aer.operation == uTI.esg:
            self._connection.axH().on_message(aer.message)
        elif aer.operation == uTI.klX:
            if aer.connection_uuid == self._connection.cHD():
                self._connection.disconnect()
                self._connection.jno()
                self._scheduler.ArA(aer.connection_uuid, self._connection,
                                          aer.disconnect_reason)
        elif aer.operation == uTI.aQV:
            self._connection.fDB()
            self._scheduler.llM(self._connection)
        elif aer.operation == uTI.zod:
            self._connection.xYl()
        elif aer.operation == uTI.Bwc:
            self._connection.uyx()
        elif aer.operation == uTI.OrY:
            self._connection.FjH()
        elif aer.operation == uTI.nvP:
            self._connection.resume()
        elif aer.operation == uTI.hCP:
            self._scheduler.gvX(self._connection.cHD(),
                                                           self._connection, lgT.CcI)
import threading
import random
import time
class IMc(iCr):
    def __init__(self, configuration, client_state):
        self._keep_alive_timer_task = None
        self._reconnect_timer_task = None
        self._ping_operation_timer_task = None
        self._configuration = configuration
        self._client_state = client_state
        self._keep_alive_timeout = self._configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
    def ArA(self, Itu, connection, disconnect_info):
        if connection.Umj() != IVo.Quq:
            return
        dfD = connection.cHD()
        if dfD is None or dfD != Itu:
            return
        connection.sae(None)
        connection.bws(disconnect_info)
        Wuf = connection.sWW()
        gfv = self.TUm(Wuf, False)
        if self._reconnect_timer_task is not None:
            self._reconnect_timer_task.cancel()
        self._reconnect_timer_task = threading.Timer(gfv, self.Fub, [connection, disconnect_info])
        self._reconnect_timer_task.start()
    def Fub(self, connection, disconnect_info):
        connection.VcU().YFq(gby.Erm(disconnect_info))
    def llM(self, connection):
        if self._ping_operation_timer_task is not None:
            self._ping_operation_timer_task.cancel()
        self._ping_operation_timer_task = threading.Timer(self._configuration.PING_INTERVAL,
                                                          self.ayB, [connection])
        self._ping_operation_timer_task.start()
    def ayB(self, connection):
        connection.VcU().YFq(gby.JsS())
    def cancel(self):
        if self._keep_alive_timer_task is not None:
            self._keep_alive_timer_task.cancel()
        if self._ping_operation_timer_task is not None:
            self._ping_operation_timer_task.cancel()
        if self._reconnect_timer_task is not None:
            self._reconnect_timer_task.cancel()
    def gvX(self, Itu, connection, keep_alive):
        if self._keep_alive_timer_task is not None:
            self._keep_alive_timer_task.cancel()
        gfv = self._keep_alive_timeout
        if keep_alive == lgT.ojR:
            Wuf = connection.JUz()
            gfv = self.TUm(Wuf, True)
        if gfv > 0:
            self._keep_alive_timer_task = threading.Timer(gfv,
                                                          self.gUp, [Itu, connection])
            self._keep_alive_timer_task.start()
    def gUp(self, uuid, connection):
        dfD = connection.cHD()
        if dfD is None or dfD != uuid:
            return
        self._client_state.GQZ(wsQ.klX)
        connection.VcU().YFq(
            gby.TNU(uuid, gHQ.SZc))
    def urp(self, value):
        self._keep_alive_timeout = value * 1.4
    def TUm(self, Wuf, verify_timeout):
        gfv = self._configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
        if Wuf > 0:
            if Wuf <= self._configuration.quick_reconnect_max_retries:
                gfv = (Wuf * self._configuration.quick_reconnect_initial_delay) - int(
                    random.uniform(0, 1) * self._configuration.quick_reconnect_initial_delay)
            else:
                if self._configuration.reconnect_policy == MigratoryDataClient.TRUNCATED_EXPONENTIAL_BACKOFF:
                    count = Wuf - self._configuration.quick_reconnect_max_retries
                    gfv = int(min(self._configuration.reconnect_time_interval * pow(2, count) - int(
                        random.uniform(0, 1) * self._configuration.reconnect_time_interval * count),
                                      self._configuration.reconnect_max_delay))
                else:
                    gfv = self._configuration.reconnect_time_interval
            if verify_timeout and gfv < self._configuration.OPERATION_TIMEOUT_INTERVAL:
                gfv = self._configuration.OPERATION_TIMEOUT_INTERVAL
        return gfv
import sys
import threading
class njo:
    def __init__(self):
        self._lock = threading.Lock()
        self._running = False
        self._configuration = None
        self._connection = None
        self._single_thread_event_loop = None
        self._listener_notifier = None
        self._servers = None
        self._migratory_data_listener = None
        self._client_state = Pwp()
        self.lSg = AZa.ycH
        self.Fxg = "MigratoryDataClient/v6.0 Python/" + str(sys.version)
        self._logger = osA()
        self._configuration = XDE(self.lSg, self.Fxg)
    def ImB(self):
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
            Yxr = eAW(self._servers, self._configuration.encryption)
            self._listener_notifier = OsY(self._migratory_data_listener)
            self._listener_notifier.start()
            ROp = IMc(self._configuration, self._client_state)
            self._connection = Connection(self._configuration, self._listener_notifier, Yxr, ROp,
                                          self._client_state, self._logger)
            knm = Mnt(self._connection, ROp)
            self._single_thread_event_loop = mzr(knm, self._logger)
            self._connection.HQc(self._single_thread_event_loop)
            self._single_thread_event_loop.YFq(gby.kUm())
            Pnj = self._configuration.get_subjects()
            for WLq in Pnj:
                self._single_thread_event_loop.YFq(
                    gby.JDj([WLq], Pnj[WLq]))
                self._logger.debug(fqD.dsq + str([WLq]))
            self._single_thread_event_loop.start()
        finally:
            self._lock.release()
    def KSn(self, _servers):
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
    def PLT(self):
        self._lock.acquire()
        try:
            listener = self._migratory_data_listener
        finally:
            self._lock.release()
        return listener
    def TjW(self, _listener):
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
    def PXX(self, _log_listener, _log_level):
        self._lock.acquire()
        try:
            if self._running is False:
                self._logger.wsC(_log_listener, _log_level)
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def uyx(self):
        self._lock.acquire()
        try:
            self._logger.info("Disposing")
            if self._running is False:
                return
            self._running = False
            if self._single_thread_event_loop is not None:
                self._single_thread_event_loop.YFq(gby.Plt())
                self._logger.debug(fqD.hZv)
                self._single_thread_event_loop.yIb()
                self._single_thread_event_loop = None
            if self._listener_notifier is not None:
                self._listener_notifier.oBS()
                self._listener_notifier = None
        finally:
            self._lock.release()
    def JfO(self, token):
        self._lock.acquire()
        try:
            if self._running is False:
                self._configuration.entitlement_token = token
                self._logger.info("Configuring Entitlement token: " + token)
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def zjj(self, _subjects, history):
        self._lock.acquire()
        try:
            if _subjects is None or len(_subjects) == 0:
                raise ValueError("Error: subscribe() - invalid argument; expected a list of valid topics")
            for guq in _subjects:
                if guq is None or len(guq) == 0 or gHQ.qin(guq) is False:
                    raise TypeError("Subscribe with invalid guq: " + str(guq))
            if history < 0:
                raise ValueError(
                    "Error: subscribeWithHistory() - the argument numberOfHistoricalMessages should be a positive number or zero!")
            self._logger.info("Subscribing to: " + str(_subjects))
            self._configuration.jbq(_subjects, history)
            if self._running is True:
                self._single_thread_event_loop.YFq(
                    gby.JDj(_subjects, history))
                self._logger.debug(fqD.dsq + str(_subjects))
        finally:
            self._lock.release()
    def UPj(self, _subjects):
        self._lock.acquire()
        try:
            if _subjects is None or len(_subjects) == 0:
                raise ValueError("Error: subscribe() - invalid argument; expected a list of valid topics")
            for guq in _subjects:
                if guq is None or len(guq) == 0 or gHQ.qin(guq) is False:
                    raise TypeError("Unsubscribe with invalid guq: " + str(guq))
            self._logger.info("Unsubscribing from: " + str(_subjects))
            self._configuration.rMp(_subjects)
            if self._running is True:
                self._single_thread_event_loop.YFq(gby.cjl(_subjects))
                self._logger.debug(fqD.fXo + str(_subjects))
        finally:
            self._lock.release()
    def wkJ(self, _message):
        self._lock.acquire()
        try:
            if self._running is True:
                guq = _message.get_subject()
                gYS = _message.get_content()
                if guq is None or len(guq) == 0 or gHQ.qin(guq) is False:
                    raise TypeError("Msg with invalid subj: " + str(guq))
                if gYS is None:
                    raise TypeError("Msg with null content")
                self._single_thread_event_loop.YFq(gby.WNa(_message))
                self._logger.debug(fqD.jid + str(_message))
            else:
                raise RuntimeError("Error: publish() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def hMJ(self, _encryption_bool):
        self._lock.acquire()
        try:
            if self._running is False:
                self._logger.info("Configuring encryption to: " + str(_encryption_bool))
                self._configuration.encryption = _encryption_bool
            else:
                raise RuntimeError("Client is already running, Disconnect first")
        finally:
            self._lock.release()
    def KDM(self, nr):
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
    def pLE(self):
        self._lock.acquire()
        try:
            return list(self._configuration.get_subjects().keys())
        finally:
            self._lock.release()
    def FjH(self):
        self._lock.acquire()
        try:
            if self._running is True:
                self._logger.info("Migratorydata client calls pause")
                self._logger.debug(fqD.wso)
                self._single_thread_event_loop.YFq(gby.Tbv())
            else:
                raise RuntimeError("Error: pause() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def FAB(self):
        self._lock.acquire()
        try:
            if self._running is True:
                self._logger.info("Migratorydata client calls resume")
                self._logger.debug(fqD.aTg)
                self._single_thread_event_loop.YFq(gby.szz())
            else:
                raise RuntimeError("Error: resume() - not connected; use this method after connect()")
        finally:
            self._lock.release()
    def bvI(self, nr):
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
    def mEA(self, interval):
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
    def pVT(self, _policy):
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
    def NGB(self, interval):
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
    def MKA(self, delay):
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
    def QwM(self, type):
        self._lock.acquire()
        try:
            if self._running is True:
                raise RuntimeError(
                    "Error: Set_transport() - already connected; use this method before connect")
            if type == MigratoryDataClient.TRANSPORT_HTTP:
                self._configuration.trans_type = yhd.HTTP
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
    CONSTANT_WINDOW_BACKOFF = "CONSTANT_WINDOW_BACKOFF"
    TRUNCATED_EXPONENTIAL_BACKOFF = "TRUNCATED_EXPONENTIAL_BACKOFF"
    TRANSPORT_HTTP = "TRANSPORT_HTTP"
    TRANSPORT_WEBSOCKET = "TRANSPORT_WEBSOCKET"
    def __init__(self):
        self._client_impl = njo()
    def connect(self):
        self._client_impl.ImB()
    def disconnect(self):
        self._client_impl.uyx()
    def set_listener(self, listener):
        if issubclass(type(listener), MigratoryDataListener) is False:
            raise TypeError("Argument for set_listener must be a subclass MigratoryDataListener")
        self._client_impl.TjW(listener)
    def get_listener(self):
        return self._client_impl.PLT()
    def set_log_listener(self, log_listener, log_level):
        if issubclass(type(log_listener), MigratoryDataLogListener) is False:
            raise TypeError("First argument for set_log_listener must be a subclass MigratoryDataLogListener")
        if type(log_level) is not int:
            raise TypeError("Second argument for set_log_level must be a MigratoryDataLogLevel")
        if log_level < 0 or log_level > 4:
            raise TypeError("Second argument for set_log_level must be a MigratoryDataLogLevel")
        self._client_impl.PXX(log_listener, log_level)
    def set_entitlement_token(self, entitlement_token):
        if type(entitlement_token) is not str:
            raise TypeError("Argument for set_entitlement_token must be of type string")
        self._client_impl.JfO(entitlement_token)
    def set_servers(self, servers):
        self._check_if_is_string_list(servers, "set_servers")
        self._client_impl.KSn(servers)
    def _check_if_is_string_list(self, string_list, method_name):
        if type(string_list) is not list:
            raise TypeError("First argument for " + method_name + " must be a list of strings")
        for gFa in string_list:
            if type(gFa) is not str:
                raise TypeError("First argument for " + method_name + " must be a list of strings")
    def subscribe(self, subject_list):
        self._check_if_is_string_list(subject_list, "subscribe")
        self._client_impl.zjj(subject_list, 0)
    def subscribe_with_history(self, subject_list, number_of_historical_messages):
        self._check_if_is_string_list(subject_list, "subscribe_with_history")
        if type(number_of_historical_messages) is not int:
            raise TypeError("Second argument for subscribe_with_history must be of type int")
        self._client_impl.zjj(subject_list, number_of_historical_messages)
    def unsubscribe(self, subject_list):
        self._check_if_is_string_list(subject_list, "unsubscribe")
        self._client_impl.UPj(subject_list)
    def publish(self, message):
        if type(message) is not MigratoryDataMessage:
            raise TypeError("Argument for publish must be of type MigratoryDataMessage")
        self._client_impl.wkJ(message)
    def set_encryption(self, encryption_bool):
        if type(encryption_bool) is not bool:
            raise TypeError("Argument for set_encryption must be of type bool")
        self._client_impl.hMJ(encryption_bool)
    def get_subjects(self):
        return self._client_impl.pLE()
    def pause(self):
        self._client_impl.FjH()
    def resume(self):
        self._client_impl.FAB()
    def notify_after_failed_connection_attempts(self, retries_number):
        if type(retries_number) is not int:
            raise TypeError("Argument for notify_after_failed_connection_attempts must be of type int")
        self._client_impl.KDM(retries_number)
    def set_quick_reconnect_max_retries(self, retries_number):
        if type(retries_number) is not int:
            raise TypeError("Argument for set_quick_reconnect_max_retries must be of type int")
        self._client_impl.bvI(retries_number)
    def set_quick_reconnect_initial_delay(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_quick_reconnect_initial_delay must be of type int")
        self._client_impl.mEA(seconds)
    def set_reconnect_policy(self, policy):
        if type(policy) is not str:
            raise TypeError("Argument for set_reconnect_policy must be of type string")
        self._client_impl.pVT(policy)
    def set_reconnect_time_interval(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_reconnect_time_interval must be of type int")
        self._client_impl.NGB(seconds)
    def set_reconnect_max_delay(self, seconds):
        if type(seconds) is not int:
            raise TypeError("Argument for set_reconnect_max_delay must be of type int")
        self._client_impl.MKA(seconds)
    def set_transport(self, transport_type):
        if transport_type != MigratoryDataClient.TRANSPORT_HTTP and transport_type != MigratoryDataClient.TRANSPORT_WEBSOCKET:
            raise TypeError(
                "Argument for set_transport must be MigratoryDataClient.TRANSPORT_WEBSOCKET or MigratoryDataClient.TRANSPORT_HTTP")
        self._client_impl.QwM(transport_type)
