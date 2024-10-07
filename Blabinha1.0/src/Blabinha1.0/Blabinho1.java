//Teste para verificar que o repositorio git local está funcionando
package Blabinho1;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.*;

import com.google.gson.Gson;

import ai.humanrobotics.messaging.types.AlertDialog;
import ai.humanrobotics.messaging.types.AlertDialogOption;
import ai.humanrobotics.messaging.types.AlertDialogResult;
import ai.humanrobotics.messaging.types.FaceDisplaySettings;
import com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory;
import io.humanrobotics.api.Robios;
import io.humanrobotics.api.RobiosApi;
import io.humanrobotics.api.RobiosConfig;
import io.humanrobotics.api.exception.RobiosException;
import io.humanrobotics.api.listeners.AlertDialogListener;
import io.humanrobotics.api.listeners.VoiceRecognitionListener;
import io.humanrobotics.api.models.constants.Expression;

public class Blabinho1 {
    static int falas = 0; // falas != 0 quer dizer que vai sair no prompt/cmd ao inves da voz do robo
    static int tab2 = 0;
    static String[] opII1 = { "Importância da Amazônia Azul", "Animais, plantas e outros bichinhos da Amazônia Azul",
            "Os mundos que existem na Amazônia Azul", "Amazônia Azul em perigo", "Quem cuida da Amazônia Azul",
            "Meu herói está pronto", "Sair da brincadeira" };
    // ("II2","II3","II3D","II5","II6","Sair","Terminar")

    static String[] opII2 = { "Geração de energia no mar", "Transporte e navegação na Amazônia Azul",
            "Como é a pesca na Amazônia Azul?", "O que é aquicultura?", "Turismo: para onde viajar.",
            "Esporte: que legal!", "Voltar", "Meu herói está pronto" };
    // "II8","II9","II10A","II10B","II10B","II4A","II4B","Sair","Terminar"

    static String[] opII3D = { "II3D2", "II3D3", "II3D4", "II3D5", "II3D6", "II3D7 ", "Sair", "Terminar" };
    // "II3D2","II3D3","II3D4","II3D5","II3D6","II3D7 ","Sair","Terminar"

    static int[] bonus = { 0, 0, 0 };
    // [0]-> Radar(II6A) [1]-> Câmera/Sapato (II3D4/II3D2) [2]-> Mapa(II4B)
    static int[] escolhas = { 0, 0, 0 };
    static String mediaP = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/895c1dc3-6db2-4cda-ba4c-36ab8c5f2e1a_The Ocean.png";
    static float completude = 6;
    public static String userInput = "";
    private static final long delayFalas = 7000;

    private static final String errorMsg = "Desculpe, não entendi o que você disse.";

    public static final String apiKey = "Insira sua chave aqui";

    public static final String robotId = "Insira sua chave aqui";


    public static Robios robios;
    static {
        try {
            robios = RobiosApi.get(apiKey, RobiosConfig.forCloud(robotId));
        } catch (RobiosException e) {
            throw new RuntimeException(e);
        }
    }

    /*
     * private static final String ROBOT_ADDRESS = "Insira sua chave aqui";
     * public static Robios robios;
     * 
     * static {
     * try {
     * RobiosConfig config = new RobiosConfig();
     * config.setRobotAddress(ROBOT_ADDRESS);
     * config.setRobotId(robotId);
     * robios = RobiosApi.get(apiKey, config);
     * } catch (RobiosException e) {
     * throw new RuntimeException(e);
     * }
     * }
     */

    public static void fa2(String tex) throws Exception {
        String[] ar = tex.split("/", 0);
        if (falas == 0) {
            for (String s : ar) {
                if (!ar[0].equals("")) {
                    robios.say(s);
                }
            }
        } else {
            System.out.println("##### FALA #####");
            for (String s : ar) {
                if (!ar[0].equals("")) {
                    System.out.println(s);
                }
            }
        }
    }

    public static void fa(String tex) throws Exception {
        String[] ar = tex.split("/", 0);
        if (falas == 0) {
            for (String s : ar) {
                if (!ar[0].equals("")) {
                    if (s.contains("RAIVA")) {
                        robios.setExpression("hangry");
                        s = s.replaceAll("RAIVA", "");
                        robios.say(s);
                    } else if (s.contains("FELIZ")) {
                        robios.setExpression("happy");
                        s = s.replaceAll("FELIZ", "");
                        robios.say(s);
                    } else if (s.contains("TRISTE")) {
                        robios.setExpression("sad");
                        s = s.replaceAll("TRISTE", "");
                        robios.say(s);
                    } else if (s.contains("MEDO")) {
                        robios.setExpression("afraid");
                        s = s.replaceAll("MEDO", "");
                        robios.say(s);
                    } else if (s.contains("SUSTO")) {
                        robios.setExpression("scared");
                        s = s.replaceAll("SUSTO", "");
                        robios.say(s);
                    } else if (s.contains("NORMAL")) {
                        robios.setExpression("normal");
                        s = s.replaceAll("NORMAL", "");
                        robios.say(s);
                    } else {
                        robios.setExpression("normal");
                        robios.say(s);
                    }
                    robios.setExpression("normal");
                }
            }
        } else {
            System.out.println("##### FALA #####");
            for (String s : ar) {
                if (!ar[0].equals("")) {
                    System.out.println(s);
                }
            }
        }
    }

    public static void bonusImage() throws Exception {
        String[] btn = { "Ver o que é" };
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/6e34f045-55c9-4ccf-a18b-9d6dfbfebc66_Star.png";
        Thread.sleep(1750);
        robios.setExpression("scared");
        Thread.sleep(1500);
        fa("Alguma coisa está acontecendo!");
        robios.setExpression("happy");
        fa("O que será?");
        displayImage(robios, btn, media, "");
    }

    public static String recebeNome(String tex) {
        String[] retira = { "\\bmeu\\b", "\\bnome\\b", "\\bé\\b", "\\bme\\b", "\\bchamo\\b", "\\bsou\\b",
                "\\bconhecido\\b", "\\bcomo\\b", "\\boi\\b", "\\bola\\b", "\\bolá\\b", "é" };
        String textoCortado = tex;
        for (String retirar : retira) {
            textoCortado = textoCortado.replaceAll(retirar, "");
        }
        return textoCortado;
    }

    // **************************************************************************************************************
    // ************************** RESPOSTAS para perguntas do tipo SIM ou NÃO
    // ***************************************
    public static String recebeConfirmacao(String tex) throws Exception {
        String resp = "";

        if (tex.contains("nao") || tex.contains("negativo") || tex.contains("não")) {
            resp = "nao";
        } else if (tex.contains("sim") || tex.contains("Claro") || tex.contains("claro") || tex.contains("vamos")
                || tex.contains("gostaria") || tex.contains("sei") || tex.contains("quero") || tex.contains("ok")
                || tex.contains("ta") || tex.contains("tá") || tex.contains("bom") || tex.contains("bora")) {
            resp = "sim";
        } else {
            fa("Ops, não entendi o que você disse!/ Vou repetir a pergunta.");
        }

        return resp;
    }

    public static void recebeConfirmacaoVTC(String tex) throws Exception {
        String resp = "";
        if (tex.contains("nao") || tex.contains("negativo") || tex.contains("não")) {
            resp = "nao";
        } else if (tex.contains("sim") || tex.contains("Claro") || tex.contains("claro") || tex.contains("vamos")
                || tex.contains("gostaria") || tex.contains("sei") || tex.contains("quero") || tex.contains("ok")
                || tex.contains("ta") || tex.contains("tá") || tex.contains("bom") || tex.contains("bora")) {
            resp = "sim";
        } else {
            fa("Ops, não entendi o que você disse!/ Vou repetir a pergunta.");
        }
    }

    public static String recebeConfirmacao2(String tex) throws Exception {
        String resp;
        tex = tex.toLowerCase();
        if (((tex.contains("que") || tex.contains("qual")) && (tex.contains("desafio"))) || tex.contains("explica")
                || (tex.contains("não") && (tex.contains("entendi") || tex.contains("sei")))
                || (tex.contains("conte") && tex.contains("mais"))) {
            resp = ask("É um desafio muito legal, sobre super-heróis. Me diga se você quer participar.");
            resp = recebeConfirmacao(resp);
            if (resp.contains("sim")) {
                return "sim";
            } else if (resp.contains("nao")) {
                return "nao";
            }
            return resp;
        } else {
            resp = recebeConfirmacao(tex);
            return resp;
        }
    }

    public static void retiraVetor(String retira, int caso) {
        String[] temp;
        int inserir = 0;
        if (caso == 1) {
            temp = new String[opII1.length - 1];
            for (String s : opII1) {
                if (!retira.equals(s)) {
                    temp[inserir] = s;
                    inserir++;
                }
            }
            opII1 = temp;
        } else if (caso == 2) {
            temp = new String[opII2.length - 1];
            for (String s : opII2) {
                if (!retira.equals(s)) {
                    temp[inserir] = s;
                    inserir++;
                }
            }
            opII2 = temp;
        } else if (caso == 3) {
            temp = new String[opII3D.length - 1];
            for (int i = 0; i < opII3D.length - 1; i++) {
                if (retira.equals(opII2[i])) {
                    temp[inserir] = opII3D[i];
                    inserir++;
                }
            }
            opII3D = temp;
        }
    }

    public static String assuntos() {
        Random gerador = new Random();
        int x = gerador.nextInt(4);

        switch (x) {
            case 0 -> {
                return "Você quer deixar seu herói mais forte? Escolha outro assunto.";
            }
            case 1 -> {
                return "Se você ainda tiver fôlego, escolha outro assunto.";
            }
            case 2 -> {
                return "Escolha um assunto para conhecer um pouco mais:";
            }
            case 3 -> {
                return "Ainda não cansou? Então escolha outro assunto.";
            }
            default -> {
                return "Você quer deixar seu herói mais forte? Escolha outro assunto.";
            }
        }
    }

    public static void log() {
        System.out.println("#################### LOG ###############");
        System.out.println("Quantidade vista:" + completude + "/19\n");

    }

    public static void completude() {
        completude++;
        log();
    }

    // ******************************************************************************************************
    // ******************************************* FASE 1
    // ***************************************************

    public static void tabelaI1() throws Exception { // fase 1 da aplicação
        String resp;
        String nome;
        int cond = 0;
        resp = ask("Olá!/Que bom que você está aqui./Como é seu nome?");
        nome = recebeNome(resp);
        fa("Olá " + nome + "./O meu nome é Blabinha.");
        do {
            resp = ask("Será que você gostaria de participar de um desafio comigo?");
            resp = recebeConfirmacao2(resp);
            if (Objects.equals(resp, "sim")) {
                tabelaI2();
                cond = 1;
            } else if (Objects.equals(resp, "nao")) {
                robios.setExpression("sad");
                tabelaI3();
                cond = 1;
            }
        } while (cond == 0);

    }

    public static void tabelaI2() throws Exception { // fase 1 da aplicação
        String resp;
        int cond = 0;
        robios.setExpression("happy");
        fa("Oba, que bom!!");
        robios.setExpression("normal");
        fa("Eu faço parte de um grupo que cuida da Amazônia Azul./Estamos precisando de um super herói para nos ajudar!"
                +
                "/O nosso desafio é construí-lo./Mas antes, eu preciso lhe explicar o que é a Amazônia Azul.");
        do {
            resp = ask("Será que você sabe o que é a Amazônia Azul?");
            resp = recebeConfirmacao(resp);
            if (Objects.equals(resp, "sim")) {
                tabelaI4();
                cond = 1;
            } else if (Objects.equals(resp, "nao")) {
                tabelaI5();
                cond = 1;
            }
        } while (cond == 0);

    }

    public static void tabelaI3() throws Exception { // fase 1 da aplicação
        robios.setExpression("sad");
        fa("Poxa, que pena!");
        robios.setExpression("normal");
        fa("Mas não tem problema, se você quiser participar do desafio outro dia, você pode voltar." +
                "/Até mais!");
    }

    public static void tabelaI4a() throws Exception { // fase 1 da aplicação
        String resp;
        int cond = 0;

        fa("Que bacana!!!");
        fa("Nem todo mundo sabe o que é a Amazônia Azul." +
                "/Esse mar azul que banha o nosso país precisa muito da nossa atenção!");
        do {
            resp = ask("Vamos ao desafio então?");
            resp = recebeConfirmacao(resp);
            if (Objects.equals(resp, "sim")) {
                tabelaI6();
                cond = 1;
            } else if (Objects.equals(resp, "nao")) {
                tabelaI3();
                cond = 1;
            }

        } while (cond == 0);
    }

    public static void tabelaI4() throws Exception { // fase 1 da aplicação
        String resp;
        int cond = 0;
        robios.setExpression("happy");
        fa("Que bacana!!!");
        robios.setExpression("normal");
        fa("Nem todo mundo sabe o que é a Amazônia Azul." +
                "/Esse mar azul que banha o nosso país precisa muito da nossa atenção!");

        do {
            resp = ask("Vamos ao desafio então?");
            resp = recebeConfirmacao(resp);
            if (Objects.equals(resp, "sim")) {
                tabelaI6();
                cond = 1;
            } else if (Objects.equals(resp, "nao")) {
                tabelaI3();
                cond = 1;
            }
        } while (cond == 0);
    }

    public static void tabelaI5() throws Exception { // fase 1 da aplicação
        String resp;
        int cond = 0;
        fa("A Amazônia Azul é o nome que a Marinha do Brasil deu para o mar do nosso lindo oceano. " +
                "/Todo nosso litoral, suas praias, ilhas e animais, fazem parte dela." +
                "/É uma região muito linda, mas que corre perigo. Por isso precisamos de um super herói." +
                "/O super herói vai proteger a Amazônia Azul! " +
                "/Legal, né?!");
        do {
            resp = ask(" Você quer partir para o desafio de criar um super herói para a Amazônia Azul comigo?");
            resp = recebeConfirmacao(resp);

            if (Objects.equals(resp, "sim")) {
                tabelaI6();
                cond = 1;
            } else if (Objects.equals(resp, "nao")) {
                tabelaI3();
                cond = 1;
            }
        } while (cond == 0);

    }

    public static void tabelaI6() throws Exception { // fase 1 da aplicação
        robios.setExpression("happy");
        fa("Bora lá então!!");
        robios.setExpression("normal");
        fa("Para criar um super herói, você precisa primeiro aprender sobre a Amazônia Azul." +
                " Quanto mais você souber sobre a Amazônia Azul, mais forte ficará seu herói!/" +
                " Vamos começar");

        tabelaII1();
    }

    // ******************************************************************************************************
    // ******************************************************************************************************

    public static void menu(String tabela) throws Exception {
        switch (tabela) {
            case "Sair da brincadeira" -> tabelaII7();
            case "Sair", "Voltar" -> tabelaII1();
            case "Meu herói está pronto" -> tabelaIII();
            case "Importância da Amazônia Azul" -> tabelaII2();
            case "Animais, plantas e outros bichinhos da Amazônia Azul" -> tabelaII3();
            case "Os mundos que existem na Amazônia Azul" -> tabelaII3D();
            case "Amazônia Azul em perigo" -> tabelaII5();
            case "Quem cuida da Amazônia Azul" -> tabelaII6();
            case "Geração de energia no mar" -> tabelaII8();
            case "Transporte e navegação na Amazônia Azul" -> tabelaII9();
            case "Como é a pesca na Amazônia Azul?" -> tabelaII10A();
            case "O que é aquicultura?" -> tabelaII10B();
            case "Turismo: para onde viajar." -> tabelaII4A();
            case "Esporte: que legal!" -> tabelaII4B();
            case "Costões rochosos" -> tabelaII3D2();
            case "Lagunas costeiras" -> tabelaII3D3();
            case "Recifes de corais" -> tabelaII3D4();
            case "Manguezais" -> tabelaII3D5();
            case "Marismas" -> tabelaII3D6();
            case "Praias arenosas" -> tabelaII3D7();
            default -> {
                fa("Opa!/ Aconteceu algum problema! ");
                System.out.println("Sem opção no menu para -> " + tabela);
            }
        }
    }

    public static void tabelaII1() throws Exception {
        if (opII1.length == 0) {
            tabelaIII();
        }
        String assunto = assuntos();
        String nome = displayImage(robios, opII1, mediaP, assunto);
        menu(nome);

    }

    public static void opcoesII2() throws Exception {
        String assunto = assuntos();
        String resp = displayImage(robios, opII2, mediaP, assunto);
        menu(resp);

    }

    // ************************************ Fase 2
    // **********************************************************
    // ******************************************************************************************************
    public static void tabelaII2() throws Exception { // fase 2 da aplicação - MENU 1: Importância da Amazônia Azul
        if (opII2.length > 2) {
            if (tab2 == 0) {
                fa("Ok, então vamos conversar um pouco sobre a importância da Amazônia Azul./" +
                        "A Amazônia Azul é um lugar cheio de coisas importantes que precisamos para viver./" +
                        "Ela ajuda a limpar o ar que respiramos, consegue produzir energia para acender a luz,/" +
                        " serve como caminhos para irmos de um lugar para outro, nos dá comida e muita diversão." +
                        "/Tem muitas coisas importantes na Amazônia Azul.");
                tab2 = 1;
                opcoesII2();
            } else {
                opcoesII2();
            }
        } else {
            retiraVetor("Importância da Amazônia Azul", 1);
            fa("Você já sabe muito sobre a importância da Amazônia Azul, agora você pode voltar para saber sobre outros assuntos.");
            tabelaII1();
        }
    }

    public static void tabelaII3() throws Exception { // fase 2 da aplicação - - MENU 1: Animais, plantas e outros
                                                      // bichinhos da Amazônia Azul

        String[] getOpII3 = { "Fauna", "Flora", "Microorganismos" };
        // ("II3A","II3B","II3C","Sair","Terminar")

        fa("A biodiversidade marinha inclui a fauna, que são os animais marinhos,/ a flora," +
                " que são as plantas que vivem na água ou perto do mar,/" +
                " e os microorganismos, que incluem os seres vivos muito pequenos que não podemos enxergar só com nossos olhos."
                +
                "/Tudo isso está dentro dos ecossistemas, que são como grandes casas com diferentes seres vivos que vivem juntos./"
                +
                "Seu super herói vai dar mais atenção para o que: fauna, flora ou microorganismos?");

        String resp = displayImage(robios, getOpII3, mediaP, "");
        retiraVetor("Animais, plantas e outros bichinhos da Amazônia Azul", 1);
        if (Objects.equals(resp, "Fauna")) {
            tabelaII3A();
        } else if (Objects.equals(resp, "Flora")) {
            tabelaII3B();
        } else if (Objects.equals(resp, "Microorganismos")) {
            tabelaII3C();
        }
    }

    // Fiz uma imagem para colocar aqui enquanto o robô fala toda essa fala.
    // Não sei se isso fica bom, porque vai ficar uma imagem grande lá enquanto o
    // robô fala. Talvez deixar o rosto dele maior e centralizado.
    // Imagem com o nome da tabela no diretório de imagens.
    public static void tabelaII3A() throws Exception { // fase 2 da aplicação - ESCOLHA DE FAUNA
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/fc4e8268-4af6-43d3-841d-260a7525b927_tabelaII3A.png";
        String fala = ("No mar e nas praias do Brasil, existem muitos animais incríveis! " +
                "/Podemos encontrar golfinhos, tartarugas marinhas, peixes, caranguejos, estrelas-do-mar e até baleias!"
                +
                "/As tartarugas marinhas vivem tanto na água quanto na areia. Elas colocam seus ovos na praia e depois voltam para o mar."
                +
                "/Os peixes são variados e têm cores lindas! Já as estrelas-do-mar têm braços longos e pontudos." +
                "/SUSTOElas se grudam nas pedras e se alimentam de pequenos animais. " +
                "/Em certas épocas do ano, baleias enormes passam pela costa do Brasil." +
                "/Elas são gigantes e impressionantes!/Já deu para perceber que a fauna do Brasil é muito rica, né?");
        displayImageFala(robios, media, fala);
        tabelaII1();

    }

    // Fiz uma imagem para colocar aqui enquanto o robô fala toda essa fala.
    // Não sei se isso fica bom, porque vai ficar uma imagem grande lá enquanto o
    // robô fala. Talvez deixar o rosto dele maior e centralizado.
    // Imagem com o nome da tabela no diretório de imagens.
    public static void tabelaII3B() throws Exception { // fase 2 da aplicação - ESCOLHA DE FLORA
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/a7ab0f44-75a4-4294-ac43-bf5f3172feaf_tabelaII3B.png";
        String fala = ("A flora é o conjunto de plantas de um ambiente. No Brasil, existem muitas plantas super diferentes."
                +
                "/Podemos encontrar as algas marinhas, que vivem debaixo da água salgada." +
                "/Nas dunas há plantas resistentes, como a restinga. Elas crescem mesmo com tanta a areia e tanto vento."
                +
                "/Também são muito importantes para segurar a areia e proteger a praia." +
                "/Ainda podemos encontrar lindos coqueiros e palmeiras nas praias arenosas!");
        displayImageFala(robios, media, fala);
        tabelaII1();

    }

    // Fiz uma imagem para colocar aqui enquanto o robô fala toda essa fala.
    // Não sei se isso fica bom, porque vai ficar uma imagem grande lá enquanto o
    // robô fala. Talvez deixar o rosto dele maior e centralizado.
    // Imagem com o nome da tabela no diretório de imagens.
    public static void tabelaII3C() throws Exception { // fase 2 da aplicação - ESCOLHA DE MICROORGANISMOS
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/4c71a856-ebc8-4f42-90f1-75ddc077030a_tabelaII3C.png";
        String fala = ("Um exemplo de microorganismo é o fitoplâncton." +
                "/O fitoplâncton é um grupo de seres vivos muito muito muito pequenininhos que vivem no mar." +
                "/Eles são unicelulares. Isso quer dizer que cada um deles vive e faz todas as coisas importantes para a sua vida usando apenas uma célula."
                +
                "Eles conseguem produzir seu próprio alimento por meio da fotossíntese. " +
                "/O fitoplâncton é composto por algas e é a base da cadeia alimentar marinha." +
                "/Ou seja, esses seres são o alimento de muitos animais marinhos, dos menores, como os peixes-lanterna, aos maiores, como as baleias."
                +
                "/FELIZAlgumas bactérias e algas azuis também fazem parte deste grupo." +
                "/Esses caras são os maiores produtores de oxigênio do mundo, ganhando até da Floresta Amazônica! Incrível, né?");
        displayImageFala(robios, media, fala);
        tabelaII1();

    }

    public static void opcoesII3D() throws Exception { // fase 2 da aplicação -
        String[] opII3D = { "Costões rochosos", "Lagunas costeiras", "Recifes de corais", "Manguezais", "Marismas",
                "Praias arenosas" };
        // "II3D2","II3D3","II3D4","II3D5","II3D6","II3D7 ","Sair","Terminar"
        String resp = displayImage(robios, opII3D, mediaP, "");
        menu(resp);

    }

    public static void tabelaII3D() throws Exception { // fase 2 da aplicação - - MENU 1: Os mundos que existem na
                                                       // Amazônia Azul"
        completude();
        fa("O Oceano Atlântico banha o leste do Brasil." +
                " Nele existem vários tipos de vida./ Existem muitos ambientes diferentes nesse mar, chamados de ecossistemas."
                +
                " /Eles podem ser: montinhos de rochas, lagoas, rios que encontram o mar, " +
                "/lugares com plantas especiais que crescem na água," +
                " praias de areia, e conjuntos de corais bem coloridos, que são os recifes." +
                "/Escolha um desses ecossistemas para conhecer mais sobre a Amazônia Azul e para que seu super-herói desenvolva novas habilidades!");
        retiraVetor("Os mundos que existem na Amazônia Azul", 1);
        opcoesII3D();
    }

    public static void tabelaII3D2() throws Exception { // fase 2 da aplicação - MENU 3: Costões rochosos.
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/32c0219a-f452-4ddc-a4c4-e8d6fb3964f2_sola da bota palma da mão.png";
        String[] btn = { "Pegar seu sapato especial!" };
        fa("O costão rochoso é como se fosse um monte de paredes de pedra bem na beira do mar. " +
                "/Às vezes essas paredes são muito altas e lisas, e é ali que as ondas batem quando se quebram." +
                " /Muitos animais e plantas também vivem nesse lugar!" +
                " /Eles são bem diferentes dos que vivem na areia da praia, porque são animais e plantas que vivem grudados nas pedras.");
        bonusImage();
        fa("Você recebeu uma estrela e seu super-herói ganhou um presente. " +
                "/Agora ele tem um sapato especial para caminhar sobre os costões rochosos. " +
                "/Assim, ele não vai se machucar e vai poder proteger as pessoas e os animais da Amazônia Azul.");
        displayImage(robios, btn, media, "");
        bonus[1] = 1;
        log();
        tabelaII1();
    }

    public static void tabelaII3D3() throws Exception { // fase 2 da aplicação - MENU 3: Lagunas costeiras
        String resp;
        String[] btn = { "Máscara de mergulho", "Protetor solar", "Cordas", "Boné", "Martelo" };
        fa("Lagunas costeiras são como piscinas naturais formadas perto da praia." +
                "/Nelas, a água é mais calma e tranquila. ");
        robios.setExpression("happy");
        fa("Por isso, muitos animais como peixes e aves passam por lá para descansar e se alimentar.");
        robios.setExpression("normal");
        fa("Além disso, elas protegem a costa de tempestades e podem ser usadas para pescar alimentos para os seres humanos!");
        fa("Escolha um equipamento para ajudar seu super-herói a explorar as lagunas para verificar se está tudo bem com os animais que vivem nelas.");
        resp = displayImage(robios, btn, mediaP, "");
        switch (resp) {
            case "Máscara de mergulho" -> escolhas[2] = 1;
            case "Protetor solar" -> escolhas[2] = 2;
            case "Cordas" -> escolhas[2] = 3;
            case "Boné" -> escolhas[2] = 4;
            case "Martelo" -> escolhas[2] = 5;
        }
        fa("Ótimo, seu herói está ganhando habilidades!"); // tratar essa opção na parte 3
        log();
        tabelaII1();
    }

    public static void tabelaII3D4() throws Exception { // fase 2 da aplicação - MENU 3: Recifes de corais
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/9836315a-ceac-4ef3-900c-cd1d5d7b7fdc_camerinha.png";
        String[] btn = { "Pegue sua câmera!" };
        fa("Os recifes de corais são ambientes bem coloridos que abrigam corais, peixes, caranguejos, moluscos e outros animais e plantas incríveis."
                +
                "/Além disso, os recifes de corais ajudam a proteger a praia e tudo que está na beira do mar. " +
                "/Eles são como uma barreira natural que evita que as ondas e o vento levem a areia da praia, causando a chamada \"erosão\"."
                +
                "/Muitas pessoas gostam de mergulhar e explorar a beleza dos recifes, além de pescar peixes e mariscos que vivem por lá."
                +
                "/No Brasil, os recifes de corais estão principalmente na costa da Bahia, de Pernambuco, de Alagoas e do Rio Grande do Norte.");
        bonusImage();
        fa("Seu super-herói ganhou um presente./" +
                "Agora ele tem uma câmera para fotografar os corais e acompanhar a saúde desse lindo ecossistema!" +
                "/E você recebeu uma estrela!");
        displayImage(robios, btn, media, "");
        bonus[1] = 2;
        log();
        tabelaII1();
    }

    // Fiz uma imagem para colocar aqui enquanto o robô fala toda essa fala.
    // Não sei se isso fica bom, porque vai ficar uma imagem grande lá enquanto o
    // robô fala. Talvez deixar o rosto dele maior e centralizado.
    // Imagem com o nome da tabela no diretório de imagens.
    public static void tabelaII3D5() throws Exception { // fase 2 da aplicação - MENU 3: Manguezais
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/fc04a67e-d3ff-464c-a58f-2bfd970e9864_tabelaII3D5.png";
        String fala = ("Os manguezais são áreas especiais que ficam na junção entre a terra e o mar. " +
                "Lá, a água é salgada e tem muita lama." +
                "/As árvores que crescem nesses lugares têm raízes longas e tortas, chamadas de \"raízes respiratórias\""
                +
                "/FELIZSão raízes que ajudam as árvores a respirar." +
                "/Os manguezais são muito importantes porque são verdadeiros berçários da natureza." +
                "Muitos animais, como peixes, caranguejos e aves, vivem nesses lugares." +
                "/Eles encontram comida, abrigo e segurança para ter seus filhotes." +
                "No Brasil, podemos encontrá-los principalmente na região Norte e na região Nordeste");
        displayImageFala(robios, media, fala);
        tabelaII1();
    }

    public static void tabelaII3D6() throws Exception { // fase 2 da aplicação - MENU 3: Marismas
        String resp;
        int cond = 0;
        fa("Os marismas, ou pântanos salgados são lugares especiais entre o mar e a terra, onde crescem plantas resistentes à água salgada, como gramas e ervas."
                +
                "/Eles são feitos de um monte de coisas que vêm do mar e dos rios, como areia e lama. " +
                "/Essas coisas se juntam e formam um solo bem fértil, cheio de nutrientes que ajudam as plantas e animais a viverem lá.");
        do {
            resp = ask("Você sabe o que significa \"nutrientes\"?");
            resp = recebeConfirmacao(resp);
            if (Objects.equals(resp, "sim")) {
                robios.setExpression("happy");
                fa("Você está estudando bastante então. Parabéns!");
                robios.setExpression("normal");
                cond = 1;
            } else if (Objects.equals(resp, "nao")) {
                fa("Nutrientes são coisas que estão nos alimentos e nos ajudam a crescer e a ficar saudável. " +
                        "/As plantas, assim como os animais, também precisam de nutrientes. " +
                        "/Elas conseguem o nutrientes delas usando as suas raízes, que estão no solo.");
                cond = 1;
            }
        } while (cond == 0);
        tabelaII1();
    }

    public static void tabelaII3D7() throws Exception { // fase 2 da aplicação - MENU 3: Praias arenosas
        fa("A praia é um ambiente formado por areia ou cascalho." +
                " Ela pode estar entre a terra e o mar, ou até mesmo perto de rios e lagos." +
                "/Os materiais que formam a praia são trazidos pelas ondas, marés e ventos." +
                "/As praias são muito importantes porque elas ajudam a proteger a costa dos movimentos do mar." +
                "/A areia e a vegetação são como uma grande barreira natural contra as forças do mar." +
                "/Além disso, elas são lar para muitos animais e plantas. E para os seres humanos, são lugares de descanso e muita diversão!");
        tabelaII1();
    }

    public static void tabelaII4A() throws Exception { // fase 2 da aplicação - MENU 2 (importância): Turismo: para onde
                                                       // viajar.
        completude();
        String[] opt = { "Pegar seu mapa!" };
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/604bbad0-db1e-4778-99ca-70e593358e87_mapa 2.png";
        fa("Fazer turismo na Amazônia azul é viajar entre maravilhas. /" +
                "Além das lindas praias espalhadas por todo nosso litoral, a Amazônia Azul também tem algumas ilhas especiais que ficam no meio do oceano./"
                +
                "São ilhas chamadas de arquipélagos, porque são várias ilhas que ficam bem pertinho uma das outras./" +
                "É um pouco difícil chegar até elas, mas elas são muito legais para conhecer!/" +
                "As principais ilhas são:/" +
                "Fernando de Noronha, que fica em Pernambuco,/Atol das Rocas, no Rio Grande do Norte,/" +
                "o Arquipélago de São Pedro e São Paulo também em Pernambuco,/" +
                "a Ilha da Trindade e o Arquipélago de Martim Vaz no Espírito Santo.");
        bonusImage();
        fa("Seu super-herói ganhou um presente e você recebeu uma estrela!/" +
                "/Ele ganhou um mapa para ajudá-lo a se locomover na Amazônia Azul e saber exatamente onde estão os arquipélagos!");
        displayImage(robios, opt, media, "");
        bonus[2] = 1;
        log();
        retiraVetor("Turismo: para onde viajar.", 2);
        tabelaII2();
    }

    public static void tabelaII4B() throws Exception { // fase 2 da aplicação - MENU 2 (importância): Esporte: que
                                                       // legal!
        completude();
        String resp;
        String[] btn = { "Trator", "Cilindro de ar", "Computador", "Jet Ski", "Barco a vela" };
        fa("Na Amazônia Azul podemos praticar vários tipos de esporte, e o esporte gera o turismo de aventura./" +
                "Você deve imaginar que muitas pessoas gostam de ir para o litoral para praticar esportes./" +
                "Lá, podemos praticar esportes chamados esportes aquáticos como natação,/ mergulho livre, quando alguém entra na água, prende a respiração e mergulha bem fundo,/"
                +
                "e o mergulho autônomo, quando a pessoa mergulha com roupas especiais e com um cilindro com ar, para ajudar a respirar embaixo d'água./"
                +
                "/Além disso, existem os esportes chamados náuticos," +
                " como: remo, surfe, windsurf, kite surf, esqui aquático e wakeboard, vela, caiaque e a canoagem.");
        fa("O que o seu super-herói vai usar para proteger as pessoas que estão praticando esportes na Amazônia Azul?");
        resp = displayImage(robios, btn, mediaP, "");
        switch (resp) {
            case "Trator" -> escolhas[0] = 1;
            case "Cilindro de ar" -> escolhas[0] = 2; // alterei arqui para cilindro DE AR
            case "Jet Ski" -> escolhas[0] = 3;
            case "Computador" -> escolhas[0] = 4;
            case "Barco a vela" -> escolhas[0] = 5;
        }
        fa("Legal, agora seu super-herói tem uma nova ferramenta de trabalho! ");

        retiraVetor("Esporte: que legal!", 2);
        log();
        tabelaII2();
    }

    public static void tabelaII5() throws Exception { // fase 2 da aplicação - MENU 1: Os mundos que existem na Amazônia
                                                      // Azul"
        completude();
        fa("A Amazônia Azul é um lugar muito importante para a vida marinha do nosso país.");
        robios.setExpression("sad");
        fa("Mas infelizmente enfrenta muitos problemas, como: muitas pessoas e empresas pescando e tirando muitos peixes do mar,"
                +
                "/muitas casas e outras coisas sendo construídas na beira do mar,");
        robios.setExpression("sad");
        fa("muitas coisas sujando a água e também prejudicando o ar," +
                "/lugares que são a casa de muitos animais sendo destruídos, " +
                "/a construção de usinas de energia sem cuidados especiais e as mudanças que estão ocorrendo no clima.");
        robios.setExpression("normal");
        fa("Para cuidar dos bichinhos e das plantas do mar, é preciso fazer áreas especiais onde eles possam viver em segurança. "
                +
                "/Esses lugares são como casas para eles e incluem os manguezais, os recifes de corais e os caminhos por onde eles nadam no mar."
                +
                "/Cuidar de muitos tipos diferentes de plantas e animais no oceano é importante, porque isso ajuda a controlar o clima do nosso planeta direitinho."
                +
                "/Isso acontece porque gases importantes, como o ar que a gente respira, se movimentam de um jeito muito importante na região do oceano.");
        retiraVetor("Amazônia Azul em perigo", 1);
        tabelaII1();
    }

    public static void tabelaII6() throws Exception { // fase 2 da aplicação - MENU 1: Quem cuida da Amazônia Azul
        completude();
        fa("O governo tem regras que dizem o que pode e não pode ser feito na Amazônia Azul. " +
                "/Mas não é só o governo que precisa cuidar da Amazônia Azul. /Pessoas que estudam os seres vivos do mar,"
                +
                " empresas que cuidam de barcos e portos /e aquelas fazem mergulhos também precisam se preocupar com a Amazônia Azul. "
                +
                "/Todos precisam trabalhar juntos para proteger esse importante lugar da nossa costa.");
        String resp;
        int cond = 0;
        retiraVetor("Quem cuida da Amazônia Azul", 1);
        do {
            resp = ask("Quer saber mais?");
            resp = recebeConfirmacao(resp);
            if (Objects.equals(resp, "sim")) {
                tabelaII6A();
                cond = 1;
            } else if (Objects.equals(resp, "nao")) {
                tabelaII1();
                cond = 1;
            }
        } while (cond == 0);

    }

    public static void tabelaII6A() throws Exception { // fase 2 da aplicação - ESCOLHA DE SABER MAIS (GOVERNO)
        completude();
        bonus[0] = 1;
        String resp;
        String[] opt = { "Pegar seu radar!" };
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/a7704538-238c-4bf1-b22d-9b6cea5a1b69_Radarr.png";

        fa("No oceano, em todo o mundo, existem regiões chamadas \"Zonas Econômicas Exclusivas\"." +
                "/É um nome complicado para regiões especiais no mar que pertencem a um país, /como se fossem partes do oceano só para esse país."
                +
                "/Nesses lugares, o país pode pegar peixes, procurar por riquezas e fazer outras coisas para ajudar as pessoas."
                +
                "/É como se fosse uma parte especial do mar que um país cuida e protege." +
                "/Para proteger essa região no Brasil, os marinheiros e pilotos de avião brasileiros trabalham vigiando tudo com seus navios e aviões.");
        bonusImage();
        fa("Você recebeu uma estrela e seu super-herói ganhou um radar para monitorar a Amazônia azul." +
                "/Agora ele pode acompanhar com mais cuidado tudo que é feito na nossa linda Amazônia Azul!");
        resp = displayImage(robios, opt, media, "");

        if (Objects.equals(resp, "Pegar seu radar!")) {
            bonus[0] = 1;
            log();
            int cond = 0;
            do {
                resp = ask("Quer saber mais sobre zonas econômicas exclusivas?");
                resp = recebeConfirmacao(resp);
                if (Objects.equals(resp, "sim")) {
                    tabelaII6B();
                    cond = 1;
                } else if (Objects.equals(resp, "nao")) {
                    tabelaII1();
                    cond = 1;
                }
            } while (cond == 0);

        }
    }

    // Fiz uma imagem para colocar aqui enquanto o robô fala toda essa fala.
    // Não sei se isso fica bom, porque vai ficar uma imagem grande lá enquanto o
    // robô fala. Talvez deixar o rosto dele maior e centralizado.
    // Imagem com o nome da tabela no diretório de imagens.
    public static void tabelaII6B() throws Exception { // fase 2 da aplicação - ESCOLHA DE SABER MAIS (ZONAS ECONÔMICAS
                                                       // EXCLUSIVAS)
        completude();
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/4051fb42-67cd-4085-9a94-b8f2d222810d/5a65d56b-72a2-43cf-a208-9258bf5a2b30/11f6da5d-93f7-40e4-b40c-a2d043c30d61_tabelaII6B.png";
        String fala = ("A Zona Econômica Exclusiva é uma área que fica longe da costa do Brasil, no meio do mar. " +
                "/A Zona Econômica Exclusiva do Brasil é uma das maiores do mundo. " +
                "/Mas o Brasil quer que ela fique ainda maior, para que seja possível procurar" +
                " o petróleo que está escondido bem no fundo do mar / e para que possamos proteger mais animais e plantas que vivem mais longe da praia.");
        displayImageFala(robios, media, fala);
        tabelaII1();
    }

    // Esse menu pode vir com uma imagem nova. Sugeri uma. Está no diretório com o
    // nome da tabela.
    public static void tabelaII8() throws Exception { // fase 2 da aplicação - MENU 2 (importância): Geração de energia
                                                      // no mar
        completude();
        String resp;
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/e4605dd5-5241-4030-a034-2c6fb798289f/5a65d56b-72a2-43cf-a208-9258bf5a2b30/c24c5846-ca12-4b54-a8f0-07705f9afa6e_tabelaII8.png";
        String[] btn = { "Ventos", "Ondas", "Marés", "Petróleo" };
        fa("A Amazônia Azul pode gerar energia de várias formas. O Brasil usa muita energia produzida lá./" +
                "Por exemplo, alguns carros usam gasolina como energia, e a gasolina é feita do petróleo que pode ser encontrado no fundo do mar./"
                +
                "As ondas do mar, as marés e até o vento que sopra no mar podem ser usados para gerar a energia elétrica que chega "
                +
                "até as casas das pessoas./As pessoas que mais usam essa energia são aquelas que moram nas cidades da costa, as cidades que têm praia.");
        fa("Seu super-herói precisa de muita energia para trabalhar./" +
                "Escolha uma fonte de energia que pode ser encontrada no mar para que seu super-herói sempre possa recarregar suas forças.");
        resp = displayImage(robios, btn, media, "");
        if (Objects.equals(resp, "Ventos")) {
            escolhas[1] = 1;
        } else if (Objects.equals(resp, "Ondas")) {
            escolhas[1] = 2;
        } else if (Objects.equals(resp, "Marés")) {
            escolhas[1] = 3;
        } else if (Objects.equals(resp, "Petróleo")) {
            escolhas[1] = 4;
        }
        if (Objects.equals(resp, "Plutônio")) {
            fa("Escolha feita, vamos continuar!");
        } else {
            fa("Boa!/Agora seu herói tem como gerar energia.");
        }
        retiraVetor("Geração de energia no mar", 2);
        log();
        tabelaII2();
    }

    public static void tabelaII7() throws Exception {
        robios.setExpression("sad");
        fa("Ahh, você já vai?");
        robios.setExpression("normal");
        fa("Não tem problema, volte sempre que quiser." +
                "/Até mais!");
    }

    public static void tabelaII9() throws Exception { // fase 2 da aplicação - MENU 2 (importância): Transporte e
                                                      // navegação na Amazônia Azul
        completude();
        fa("O Brasil sempre usou o navios para levar coisas para outros países e também para receber coisas dos outros países./"
                +
                "O transporte pelo mar, chamado de transporte marítimo, é muito importante para levar, e trazer, matérias-primas "
                +
                "para as fábricas fazerem os produtos que nós usamos./" +
                "A parte mais legal é que esse transporte é mais barato porque os navios são muito grandes" +
                " e cabe muitas coisas neles de uma só vez!/" +
                "Ah, já estava me esquecendo de dizer que pessoas também podem fazer viagens pelo mar.");
        retiraVetor("Transporte e navegação na Amazônia Azul", 2);
        tabelaII2();
    }

    // a interação pode vir acompanhada de uma imagem que vc já tinha feito. Vamos
    // ver se fica bom. A imagem está com o nome da tabela.
    public static void tabelaII10A() throws Exception { // fase 2 da aplicação - MENU 2 (importância): Como é a pesca na
                                                        // Amazônia Azul?"
        completude();
        String resp;
        String[] btn = {};
        String media = "https://robots.humanrobotics.ai/cdn/get?fileName=cdn/e4605dd5-5241-4030-a034-2c6fb798289f/5a65d56b-72a2-43cf-a208-9258bf5a2b30/1cd9ec45-8833-41ee-84d1-9e1d795104a4_tabelaII10A.png";
        String fala = ("Pesca é quando as pessoas pegam peixes e outros bichinhos que vivem na água,/" +
                "como se estivessem caçando debaixo d'água./Existem dois jeitos de fazer isso:/o jeito mais simples é "
                +
                "feito por pescadores que usam barquinhos e pescam como aprenderam com seus pais;/" +
                "o outro jeito é feito por muitas pessoas e máquinas para pegar muitos peixes./" +
                "O primeiro jeito ajuda as pessoas que moram pertinho do mar,/e o segundo jeito é para levar os peixes "
                +
                "e outros bichinhos para as pessoas que moram longe do mar.");
        resp = displayImage(robios, btn, mediaP, "");
        int cond = 0;
        do {
            resp = ask("Você já viu um barquinho de pesca?");
            resp = recebeConfirmacao(resp);
            if (Objects.equals(resp, "sim")) {
                fa("Poxa, que bacana! Eu ainda não vi um. Espero poder conhecer um barquinho de pesca logo.");
                cond = 1;
            } else if (Objects.equals(resp, "nao")) {
                fa("Eu já vi alguns e são bem legais. Você pode procurar algumas fotos na internet.");
                cond = 1;
            }
        } while (cond == 0);

        retiraVetor("Como é a pesca na Amazônia Azul?", 2);
        tabelaII2();
    }

    public static void tabelaII10B() throws Exception { // fase 2 da aplicação - MENU 2 (importância): O que é
                                                        // aquicultura?
        completude();
        fa("Aquicultura é como cuidar e criar animais e plantas que vivem na água, como peixes, caranguejos, conchinhas e algas./"
                +
                "As pessoas fazem isso para depois vender ou até mesmo para ter comida./Elas podem cuidar desses animais e plantas em "
                +
                "piscinas na terra ou na própria água, perto da praia ou mais longe no meio do mar./" +
                "Agora que você aprendeu como cultivar seres vivos no mar, vai ser ótimo se você continuar aprendendo sobre outras coisas.");
        retiraVetor("O que é aquicultura?", 2);
        tabelaII2();
    }

    public static String textualizaFem(int x) {
        String texto = "";
        switch (x) {
            case 0 -> texto = "zero";
            case 1 -> texto = "uma";
            case 2 -> texto = "duas";
            case 3 -> texto = "três";
            case 4 -> texto = "quatro";
            case 5 -> texto = "cinco";
            case 6 -> texto = "seis";
            case 7 -> texto = "sete";
            case 8 -> texto = "oito";
            case 9 -> texto = "nove";
            case 10 -> texto = "dez";
        }
        return texto;
    }

    public static String textualizaMasc(int x) {
        String texto = "";
        switch (x) {
            case 0 -> texto = "zero";
            case 1 -> texto = "um";
            case 2 -> texto = "dois";
            case 3 -> texto = "três";
            case 4 -> texto = "quatro";
            case 5 -> texto = "cinco";
            case 6 -> texto = "seis";
            case 7 -> texto = "sete";
            case 8 -> texto = "oito";
            case 9 -> texto = "nove";
            case 10 -> texto = "dez";
        }
        return texto;
    }

    // ******************** Fase 3 - avaliação do herói e do desempenho do usuário
    // **************************
    // ******************************************************************************************************

    public static void tabelaIII() throws Exception {
        int estrelasP1 = 0;
        int estrelasP2 = 0;
        int estrelasTotal = 0;
        float porc = (completude / 22) * 100;
        int porcentagem = (int) porc; // aqui nunca vai dar zero porque a completude é no mínimo 6, correto? Por que
                                      // ela é no mínimo 6?
        int quanEsc = 0;
        int quanBon = 0;

        // caso de teste *******************************
        /*
         * porc = 22;
         * porcentagem = 20;
         * escolhas[0] = 4; // 1, 2, 3, 4, 5
         * escolhas[1] = 2; // 1, 2, 3, 4
         * escolhas[2] = 1; // 1, 2, 3, 4, 5
         * bonus[0] = 1;
         * bonus[1] = 1;
         * bonus[2] = 1;
         */
        // *********************************************

        // calcula a porcentagem de menus por onde o usuário navegou e atribui estrelas
        // de acordo com a porcentagem.
        fa("Você viu " + porcentagem + "% de tudo que eu sei sobre a Amazônia Azul!");
        if (porc <= 35) {
            robios.setExpression("afraid");
            fa("Você poderia conhecer muito mais sobre esse lindo lugar se você jogasse comigo por mais tempo.");
            robios.setExpression("happy");
            fa("Da próxima vez, fique mais tempo comigo. Vai ser legal!");
            robios.setExpression("normal");
        } else if (porc > 35 && porc < 70) {
            fa("Por isso você ganhou uma nova estrela! /Para ganhar mais estrelas, na próxima vez que vier participar do desafio, veja mais conteúdos.");
            estrelasTotal++;
        } else if (porc >= 70 && porc < 90) {
            fa("Por isso você ganhou duas novas estrelas!");
            robios.setExpression("scared");
            fa("Você aprendeu muito sobre a Amazônia Azul!");
            robios.setExpression("normal");
            fa("Parabéns!");
            estrelasTotal = estrelasTotal + 2;
        } else if (porc >= 90) {
            fa("Por isso você ganhou três novas estrelas! /Você já sabe tantas coisas que já pode ensinar tudo sobre a Amazônia Azul para outras pessoas. /Que demais. Muito bom mesmo!");
            estrelasTotal = estrelasTotal + 3;
        }

        // verifica em quantas atividades de escolha o usuário atuou
        for (int escolha : escolhas) {
            if (escolha != 0) {
                quanEsc++;
            }
        }
        // verifica quantos bônus o usuário conseguiu acessar
        for (int j : bonus) {
            if (j != 0) {
                quanBon++;
            }
        }

        // if nenhuma escolha foi feita nada deve acontecer aqui!
        String resp = textualizaMasc(quanEsc);

        // if (escolhas[0] != 0 || escolhas[1] != 0 || escolhas[2] != 0){
        if (quanEsc == 1) {
            robios.setExpression("afraid");
            fa("Você teve a chance de escolher apenas " + resp + " equipamento ou acessório para o seu herói!");
            robios.setExpression("normal");
            fa("Vamos analisar o que seu super-herói tem.");
        } else if (quanEsc > 1) {
            fa("Você teve a chance de escolher um total de " + resp
                    + " esquipamentos ou acessórios para o seu herói! /Vamos analisar as suas escolhas.");
        }

        if (escolhas[0] != 0) {
            fa("A super ferramenta que você escolheu para seu herói foi:");
            switch (escolhas[0]) {
                case 1 -> fa("Trator./Essa escolha não foi boa./" +
                        "O seu super-herói não pode fazer nada com um trator no meio do oceano." +
                        "/Por isso você não ganhou estrelas nessa escolha. Da próxima vez, tente escolher outra ferramenta. ");
                case 2 -> {
                    fa("Cilindro de ar./Essa foi uma boa escolha./" +
                            "Seu super-herói pode mergulhar por mais tempo com esse cilindro de ar. Assim ele pode vigiar o que está acontecendo no fundo do mar."
                            +
                            "/Então, você ganhou uma nova estrela. Parabéns!");
                    estrelasP1++;
                }
                case 3 -> {
                    fa("Jet Ski./A qualidade da sua escolha foi muito boa." +
                            "/Show! Seu super-herói pode se locomover com muita rapidez." +
                            "/Então, você ganhou duas novas estrelas. Parabéns!");
                    estrelasP1 = estrelasP1 + 2;
                }
                case 4 -> fa("Computador./Essa escolha não foi boa." +
                        "/Que pena, é muito difícil usar um computador no meio do oceano." +
                        "/Então, você não ganhou estrelas nessa escolha. Da próxima vez, tente escolher outra ferramenta. ");
                case 5 -> {
                    fa("Barco a vela. /A qualidade da sua escolha foi ótima." +
                            "/Que maneiro! Com o barco a vela, seu super-herói vai poder navegar a favor do vento e alcançar grandes distâncias!"
                            +
                            "/Então, você ganhou três novas estrelas. Estou muito feliz por você.");
                    estrelasP1 = estrelasP1 + 3;
                }
            }
            estrelasTotal += estrelasP1;
        }

        if (escolhas[1] != 0) {
            fa("Você conseguiu uma fonte de energia para o seu herói. /A fonte de energia que você escolheu foi:");
            switch (escolhas[1]) {
                case 1 -> {
                    fa("Ventos. /A qualidade da sua escolha foi boa." +
                            "/Porém, para usar os ventos como fonte de energia você vai precisar construir algumas máquinas."
                            +
                            " Então, você ganhou apenas uma nova estrela.");
                    estrelasP2++;
                }
                case 2 -> {
                    fa("Ondas. /A qualidade da sua escolha foi boa." +
                            "/Só que a construção das máquinas para capturar a energia das ondas é um pouco cara. Precisaremos de alguma ajuda."
                            +
                            "/Então, você ganhou apenas uma nova estrela.");
                    estrelasP2++;
                }
                case 3 -> {
                    fa("Marés. /A qualidade da sua escolha foi ótima." +
                            "/Essa fonte de energia é uma das mais potentes." +
                            "Então, você ganhou duas novas estrelas");
                    estrelasP2 += 2;
                }
                case 4 -> fa("Petróleo. /A qualidade da sua escolha não foi muito boa." +
                        "/O petróleo é uma das fontes de energia mais poluentes. Na próxima vez, escolha uma fonte de energia mais legal."
                        +
                        "/Então, você não ganhou novas estrelas.");
            }
            estrelasTotal += estrelasP2;
        }

        // nova escolha
        // *****************************************************************************************************************************
        if (escolhas[2] != 0) {
            fa("Você conseguiu um equipamento novo para o seu herói. /O equipamento que você conseguiu para seu herói foi:");
            switch (escolhas[2]) {
                case 1 -> {
                    fa("Máscara de mergulho. /A qualidade da sua escolha foi ótima." +
                            "/Com essa máscara, o seu herói poderá mergulhar sem que seus olhos fiquem irritados." +
                            "/Então, você ganhou duas novas estrelas.");
                    estrelasP2++;
                }
                case 2 -> {
                    fa("Protetor solar. /A qualidade da sua escolha foi ótima." +
                            "/Todo mundo precisa se proteger quando está no sol. O seu herói fica muito tempo sob o sol."
                            +
                            "/Então, você ganhou duas novas estrelas.");
                    estrelasP2++;
                }
                case 3 -> {
                    fa("Cordas. /A qualidade da sua escolha foi boa." +
                            "/As cordas podem ser úteis se o seu herói precisar retirar algum lixo grande de dentro do oceano."
                            +
                            "/Então, você ganhou uma nova estrela.");
                    estrelasP2 += 2;
                }
                case 4 -> fa("Boné. /A qualidade da sua escolha não foi boa." +
                        "/O boné pode ajudar a proteger contra o sol, mas o seu super-herói precisa mergulhar, nadar e velejar. /Acho que ele vai perder o boné!"
                        +
                        "/Então, você não ganhou novas estrelas.");
                case 5 -> fa("Martelo. /A qualidade da sua escolha não foi boa." +
                        "/Eu não sei para quê o seu herói usaria um martelo. Isso não será útil para ele. /Da próxima vez, tente escolher outro acessório."
                        +
                        "/Infelizmente, você não ganhou novas estrelas.");
            }
            estrelasTotal += estrelasP2;
        }
        // nova escolha
        // *************************************************************************************************************************

        resp = textualizaMasc(quanBon);
        if (quanBon != 0) {
            fa("Você encontrou um total de " + resp + " bônus.");
        }

        resp = textualizaFem(quanBon);
        if (quanBon == 1) {
            fa("O que te deu mais " + resp
                    + " estrela. /Veja como é bom explorar o conhecimento! /Você achou o bonus porque foi persistente.");
        } else if (quanBon > 1) {
            fa("O que te deu mais " + resp
                    + " estrelas. /Você explorou o conhecimento muito bem. /Ganhou vários bonus porque foi persistente!");
        }
        estrelasTotal += quanBon;

        fa("Agora vamos para o mais importante! /Vamos saber o quão poderoso é o seu herói. /Quanto mais estrelas você ganhou, mais poderoso é o seu herói.");
        resp = textualizaFem(estrelasTotal);
        if (estrelasTotal == 0) {
            fa("Verifiquei que você não ganhou estrelas. /O seu super-herói ainda não está preparado para proteger a Amazônia Azul."); // não
                                                                                                                                       // ocorre
                                                                                                                                       // dele
                                                                                                                                       // não
                                                                                                                                       // ter
                                                                                                                                       // nenhuma
                                                                                                                                       // estrela?
        } else if (estrelasTotal == 1) {
            fa("Sua pontuação final foi um total de uma estrela. /Isso foi legal, mas você pode construir um super-herói mais poderoso da próxima vez. /Basta você explorar mais sobre a Amazônia Azul.");
        } else {
            fa("Sua pontuação final foi um total de " + resp
                    + " estrelas. /O seu super-herói já pode começar a trabalhar porque ele tem várias habilidades.");
        }

        fa("Foi muito bom jogar com você!/Espero que você tenha aprendido bastante sobre a Amazônia Azul./" +
                "Até a próxima!");

    }

    private static String displayImageFala(Robios robios, String media, String fala) throws Exception {
        userInput = "";

        AlertDialog dialog = new AlertDialog("", "");
        dialog.setDialogType(AlertDialog.TYPE_OPTIONS);
        // image data
        dialog.setMediaType(AlertDialog.MEDIA_TYPE_IMAGE);
        if (!Objects.equals(media, "")) {
            dialog.setMediaUrl(media);
        }

        String[] btnOptions = { "Legal!!" };
        AlertDialogOption[] buttons = new AlertDialogOption[btnOptions.length];
        for (int i = 0; i < btnOptions.length; i++) {
            buttons[i] = new AlertDialogOption(btnOptions[i], btnOptions[i]);
        }
        dialog.setOptions(buttons);
        // how long the image is on
        dialog.setTimeout(0);

        dialog.setSpeakDescription(true);
        dialog.setSpeakTitle(true);

        dialog.setDisplayDescription(false);
        dialog.setDisplayTitle(false);

        dialog.setFaceDisplay(new FaceDisplaySettings(FaceDisplaySettings.MODE_RESIZED,
                FaceDisplaySettings.POSITION_TOP_LEFT, 0.30f));

        System.out.println(new Gson().toJson(dialog));

        robios.alertDialog(new Gson().toJson(dialog));

        fa(fala);
        while (userInput.isEmpty()) {
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty()) {
                Thread.sleep(2500);
                fa(fala);
            }
        }
        return userInput;

    }

    private static String displayImage(Robios robios, String[] btnOptions, String media, String fala) throws Exception {
        userInput = "";

        AlertDialog dialog = new AlertDialog("", "");
        dialog.setDialogType(AlertDialog.TYPE_OPTIONS);
        // image data
        dialog.setMediaType(AlertDialog.MEDIA_TYPE_IMAGE);
        if (!Objects.equals(media, "")) {
            dialog.setMediaUrl(media);
        }

        AlertDialogOption[] buttons = new AlertDialogOption[btnOptions.length];
        for (int i = 0; i < btnOptions.length; i++) {
            buttons[i] = new AlertDialogOption(btnOptions[i], btnOptions[i]);
        }
        dialog.setOptions(buttons);
        // how long the image is on
        dialog.setTimeout(0);

        dialog.setSpeakDescription(true);
        dialog.setSpeakTitle(true);

        dialog.setDisplayDescription(false);
        dialog.setDisplayTitle(false);

        dialog.setFaceDisplay(new FaceDisplaySettings(FaceDisplaySettings.MODE_RESIZED,
                FaceDisplaySettings.POSITION_TOP_LEFT, 0.30f));

        System.out.println(new Gson().toJson(dialog));

        robios.alertDialog(new Gson().toJson(dialog));

        fa(fala);
        while (userInput.isEmpty()) {
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty())
                Thread.sleep(2500);
            if (userInput.isEmpty()) {
                Thread.sleep(2500);
                fa(fala);
            }
        }
        return userInput;

    }

    public static void onResultReceived(AlertDialogResult result) {
        String currentDate = LocalDateTime.now(ZoneId.of("America/Sao_Paulo"))
                .format(DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss"));
        System.out.printf("[%s] [AlertDialog]: \"%s\"\n", currentDate, result.getContent());

        userInput = result.getContent();
    }

    public static void onUserTextReceived(String userAnswer) {
        String currentDate = LocalDateTime.now(ZoneId.of("America/Sao_Paulo"))
                .format(DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss"));
        System.out.printf("[%s] [VoiceRecognition]: \"%s\"\n", currentDate, userAnswer);

        userInput = userAnswer;
    }

    public static String ask(String texto) throws Exception {
        fa(texto);
        return listen();
    }

    public static String listen(String[] inputOptions) throws Exception {
        userInput = "";
        while (true) {
            robios.listen();
            Thread.sleep(delayFalas);

            for (String inputOption : inputOptions) {
                if (inputOption.equals(userInput)) {
                    return userInput;
                }
            }
            robios.say(errorMsg);
        }
    }

    public static String listen() throws Exception {
        userInput = "";
        while (userInput.isEmpty()) {
            robios.listen();
            Thread.sleep(delayFalas);
        }
        return userInput;
    }

    public static void main(String[] args) throws Exception {
        robios.addAlertDialogCallback(Blabinho1::onResultReceived);
        robios.addVoiceRecognitionCallback(Blabinho1::onUserTextReceived);
        robios.useNativeDialogs(false);

        List<String> tex = robios.getAllFaceExpressions();
        System.out.println(tex);
        robios.centerHead();

        fa("Conexão estabelecida");

        tabelaI1(); // para testar desde o início
        // tabelaII1(); // para testar a partir do MENU 1 da fase 2
        // tabelaII2(); // para testar apenas a partir da IMPORTANCIA DA AMAZONIA AZUL -
        // vai para MENU 2 depois da fala
        // tabelaII3(); // para testar a parte de FAUNA, FLORA e MICROORGANISMOS
        // tabelaII3D(); // para testar o menu 3
        // tabelaII5(); // para testar Amazonia Azul em perigo
        // tabelaII6(); // para testar quem cuida da Amazonia Azul
        // tabelaIII(); // para testar a fase 3 - avaliação

        robios.close();
    }

}
