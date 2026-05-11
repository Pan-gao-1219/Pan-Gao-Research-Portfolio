from pathlib import Path

import streamlit as st


ROOT = Path(__file__).parent
AWARD_DIR = ROOT / "assets" / "awards"
RESEARCH_DIR = ROOT / "assets" / "research"
PROJECT_DIR = ROOT / "assets" / "project"


PROFILE = {
    "name": "潘高",
    "school": "中国海洋大学",
    "major": "勘查技术与工程",
    "teacher": "陆文凯老师",
    "direction": "人工智能与地球物理反演",
}


KEY_POINTS = [
    ("申请意向", "硕士研究生", "希望跟随陆文凯老师从事人工智能与地球物理反演方向科研"),
    ("方向契合", "CycleGAN + 地球物理反演", "已在相关研究基础上完成复现，并开展结构与约束改进"),
    ("入组承诺", "暑假起提前进组", "若获认可，将不再参加其他院校夏令营考核，愿全程留京跟进科研"),
    ("综合支撑", "连续两年国家奖学金", "专业基础、竞赛荣誉、工程封装与科研项目共同支撑申请"),
]


APPLICATION_BLOCKS = [
    {
        "title": "为什么申请",
        "body": (
            "我的科研兴趣主要聚焦于地震正演与反演、地震资料处理与解释、人工智能地球物理，"
            "以及深度学习/机器学习驱动的智能反演方法。尤其希望探索物理机理约束与数据驱动模型"
            "相结合的地震反演新方法。"
        ),
    },
    {
        "title": "为什么匹配陆老师方向",
        "body": (
            "我重点关注到陆老师基于 CycleGAN 及神经网络开展的地球物理反演相关工作，"
            "这也是我目前科研工作的起点：我已在相关研究成果基础上完成模型复现，"
            "并在此之上开展了自己的创新与改进工作。"
        ),
    },
    {
        "title": "若能进组，我能做什么",
        "body": (
            "我愿意服从课题组整体安排，参与横向项目、应用类任务和新的前沿研究方向；"
            "同时，我已有较完整的研究思路，可继续围绕物理约束、稀疏井、多尺度多频段生成结构"
            "做长期深挖。"
        ),
    },
]


CAPABILITIES = [
    ("专业基础", "地震勘探相关课程均分 92.3，专业成绩与综合测评均位列班级第二。"),
    ("专业软件", "担任地源地震资料处理实验室助理，熟悉 GeoEast、Jason 等处理与反演软件。"),
    ("科研工程化", "熟练使用 Streamlit、Qt 搭建标准化工作流，能封装算法、批量实验和结果展示流程。"),
    ("复现体系", "自建“AI + 文献论文 + GitHub 源码”的闭环学习复现体系，能快速研读、部署和迭代实验。"),
    ("成果固化", "熟悉软件著作权材料整理与申报流程，可协助横向项目结题和科研成果转化。"),
    ("表达支持", "具备 PPT 制作、项目汇报答辩和摄影记录能力，可支持组内汇报与活动材料制作。"),
]


APPLICATION_AWARD_SUMMARY = [
    {
        "group": "学业与综合荣誉",
        "items": [
            "2024 年国家奖学金",
            "2025 年国家奖学金",
            "2024、2025 年中国海洋大学学习优秀一等奖学金",
            "2024、2025 年中国海洋大学“优秀学生”荣誉称号",
            "2024、2025 年中国海洋大学“优秀学生干部”荣誉称号",
        ],
    },
    {
        "group": "学科竞赛与创新创业",
        "items": [
            "2024 年中国海洋大学大学生地质技能及地学知识竞赛二等奖",
            "2024 年第三届全国大学生数据分析科普竞赛一等奖",
            "2026 年“挑战杯”中国大学生创业计划竞赛校级金奖，并已推省",
            "2025 年海洋地球科学学院青春榜样人物创新创业榜样",
        ],
    },
    {
        "group": "社会实践与志愿服务",
        "items": [
            "2024 年山东省“三下乡”社会实践优秀学生",
            "2024 年中国海洋大学优秀实践个人",
            "2025 年枣庄市大学生暑期社会实践优秀调研报告三等奖",
            "2026 年中国海洋大学“杰出志愿者”“优秀青年志愿者”“优秀共青团干部”等荣誉",
        ],
    },
    {
        "group": "科研经历及成果",
        "items": [
            "2025 年 8 月立项山东省大学生创新创业训练计划项目",
            "项目名称：基于 CycleGAN 与物理约束的地震反演方法研究",
            "目前围绕该方向形成网络结构、初步实验结果与工程封装系统",
        ],
    },
]


RESEARCH_STORY = [
    {
        "title": "核心研究问题",
        "tag": "地震反演非唯一性 / 低频缺失 / 地质合理性",
        "body": (
            "本科阶段牵头省级大学生创新创业训练计划项目《基于 CycleGAN 与物理约束的地震反演方法研究》。"
            "项目面向地震数据到阻抗模型反演中的非唯一性、低频信息缺失和深度学习结果物理一致性不足等问题。"
        ),
    },
    {
        "title": "主要创新思路",
        "tag": "固定正演算子 / PINN 约束 / 多尺度输入",
        "body": (
            "在复现经典双生成器、双判别器 CycleGAN 架构的基础上，将其中一个生成器替换为确定性地球物理"
            "正演模型，把物理正演先验作为强约束嵌入网络结构，并引入稀疏井约束与低频先验。"
        ),
    },
    {
        "title": "后续可延伸方向",
        "tag": "Diffusion / 多频段生成 / 不确定性评价",
        "body": (
            "该路线具备较好的物理可解释性，后续可继续嵌入鲁棒性更强的生成模型，如 diffusion 模型，"
            "并围绕多尺度、多频段反演和不确定性评价进一步拓展。"
        ),
    },
]


PROJECT_FIGURES = [
    ("网络结构与物理闭环", "network_structure.png", "三通道地震特征、稀疏井低频先验、固定 Ricker 正演闭环。"),
    ("稀疏井低频先验", "lowfreq_prior.png", "利用约 0.8% 稀疏井道构建低频背景，辅助宏观趋势恢复。"),
    ("测试区域反演结果", "inversion_result.png", "参考阻抗、预测阻抗与低频先验同色标对比。"),
    ("残差与绝对误差剖面", "residual_error.png", "从空间分布角度观察预测误差，辅助判断地质结构连续性。"),
    ("指标统计与模型选择", "metric_statistics.png", "测试区域 R2=0.9731、RMSE=0.0783、MAE=0.0533、Bias=-0.0082。"),
]


QT_FIGURES = [
    ("Qt 预处理系统：数据增强与物理参数配置", "qt_preprocess_augment.png"),
    ("Qt 预处理系统：功能总览与脚本调用流程", "qt_workflow.png"),
]


AWARDS = [
    ("2024年国家奖学金", "奖学金", "国家级", "2024年国家奖学金.jpg"),
    ("2025年国家奖学金公示证明", "奖学金", "国家级", "2025年国家奖学金公示证明.jpg"),
    ("2024年中国海洋大学学习优秀一等奖学金", "奖学金", "校级", "2024年中国海洋大学学习优秀一等奖学金.jpg"),
    ("2025年中国海洋大学学习优秀一等奖学金", "奖学金", "校级", "2025年中国海洋大学学习优秀一等奖学金.jpg"),
    ("中国海洋大学大学生地质技能及地学知识竞赛二等奖", "学科竞赛", "校级", "2024年中国海洋大学大学生地质技能及地学知识竞赛二等奖.jpg"),
    ("第三届全国大学生数据分析科普竞赛一等奖", "学科竞赛", "全国", "2024年第三届全国大学生数据分析科普竞赛一等奖.jpg"),
    ("全国大学生英语翻译大赛省级三等奖", "学科竞赛", "省级", "2024年全国大学生英语翻译大赛省级三等奖.jpg"),
    ("UNESCO 世界地质公园科普志愿者训练营最佳媒体奖", "社会实践", "国际平台", "2025年UNESCO世界地质公园科普志愿者训练营最佳媒体奖.jpg"),
    ("海洋地球科学学院青春榜样人物创新创业榜样", "荣誉", "院级", "2025年海洋地球科学学院青春榜样人物创新创业榜样名单.jpg"),
    ("山东省三下乡社会实践优秀学生", "社会实践", "省级", "2024年山东省三下乡社会实践优秀学生名单.jpg"),
    ("枣庄市大学生暑期社会实践优秀调研报告三等奖", "社会实践", "市级", "2025年枣庄市大学生暑期社会实践优秀调研报告三等奖.jpg"),
]


def inject_css() -> None:
    st.markdown(
        """
        <style>
        :root {
            --ink: #17211f;
            --muted: #5e6d68;
            --line: #dce4de;
            --paper: #f7f8f4;
            --teal: #0f766e;
            --clay: #9f5132;
            --gold: #a66d18;
        }
        .stApp {
            background: linear-gradient(180deg, #f7f8f4 0%, #eef4ef 100%);
            color: var(--ink);
        }
        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }
        [data-testid="stHeader"] { background: transparent; }
        h1, h2, h3 { letter-spacing: 0; color: var(--ink); }
        .hero {
            display: grid;
            grid-template-columns: minmax(0, 1.4fr) minmax(280px, .75fr);
            gap: 1.4rem;
            align-items: stretch;
            margin-bottom: 1.2rem;
        }
        .hero-main {
            border-left: 6px solid var(--teal);
            padding: 1.1rem 1.3rem;
            background: rgba(255,255,255,.64);
            border-radius: 8px;
        }
        .hero-side {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: rgba(255,255,255,.82);
            padding: 1rem;
        }
        .eyebrow {
            color: var(--teal);
            font-size: .92rem;
            font-weight: 800;
            margin-bottom: .35rem;
        }
        .hero h1 {
            font-size: clamp(2rem, 4.8vw, 4.2rem);
            line-height: 1.02;
            margin: 0 0 .65rem 0;
        }
        .hero p, .letter p {
            color: #34413d;
            font-size: 1.02rem;
            line-height: 1.78;
        }
        .side-item {
            border-bottom: 1px solid var(--line);
            padding: .6rem 0;
        }
        .side-item:last-child { border-bottom: 0; }
        .side-item span {
            display: block;
            color: var(--muted);
            font-size: .82rem;
            margin-bottom: .2rem;
        }
        .side-item strong {
            display: block;
            color: var(--teal);
            font-size: 1.08rem;
        }
        .section-title {
            margin: 2rem 0 .85rem 0;
            padding-top: .4rem;
            border-top: 1px solid var(--line);
        }
        .section-title h2 { margin-bottom: .2rem; }
        .section-title p { color: var(--muted); margin-top: 0; }
        .letter {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: rgba(255,255,255,.78);
            padding: 1.1rem 1.25rem;
        }
        .quote {
            border-left: 4px solid var(--gold);
            padding: .45rem 0 .45rem 1rem;
            margin: .85rem 0;
            color: #4d4030;
            background: #fff9eb;
        }
        .support-card, .research-card {
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1rem;
            background: rgba(255,255,255,.78);
            height: 100%;
        }
        .support-card h3, .research-card h3 { margin-top: 0; font-size: 1.08rem; }
        .support-card p, .research-card p, .research-card li {
            color: #4e5d58;
            line-height: 1.62;
        }
        .tag {
            display: inline-block;
            color: var(--clay);
            font-weight: 800;
            font-size: .84rem;
            margin-bottom: .45rem;
        }
        .pill {
            display: inline-block;
            padding: .15rem .48rem;
            border: 1px solid #cfd9d3;
            border-radius: 999px;
            color: #36534d;
            background: #f5f7f2;
            font-size: .78rem;
            margin-right: .25rem;
        }
        .note {
            border: 1px solid #dfd4bd;
            border-radius: 8px;
            padding: .9rem 1rem;
            background: #fff9ea;
            color: #67532a;
            line-height: 1.65;
        }
        div[data-testid="stImage"] img {
            border: 1px solid var(--line);
            border-radius: 8px;
        }
        @media (max-width: 820px) {
            .hero { grid-template-columns: 1fr; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def section_title(title: str, desc: str) -> None:
    st.markdown(
        f"""
        <div class="section-title">
          <h2>{title}</h2>
          <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def image_or_notice(path: Path, caption: str = "") -> None:
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.info(f"图片暂缺：{path.name}")


def render_hero() -> None:
    items = "".join(
        f"""
        <div class="side-item">
          <span>{label}</span>
          <strong>{value}</strong>
          <p>{desc}</p>
        </div>
        """
        for label, value, desc in KEY_POINTS
    )
    st.markdown(
        f"""
        <div class="hero">
          <div class="hero-main">
            <div class="eyebrow">{PROFILE["school"]} · {PROFILE["major"]}</div>
            <h1>致{PROFILE["teacher"]}的硕士研究生申请展示</h1>
            <p>
              我是{PROFILE["name"]}，诚挚申请攻读您的硕士研究生，希望跟随您从事
              <b>{PROFILE["direction"]}</b>方向的科研工作。本页面以申请信为主线，
              将我的研究兴趣、方向匹配、入组承诺、已有工作与支撑材料集中呈现，方便老师快速审阅。
            </p>
          </div>
          <div class="hero-side">{items}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_application_letter() -> None:
    section_title("申请信主线", "先呈现最需要老师看到的部分：申请动机、方向契合、明确承诺与入组价值。")
    left, right = st.columns([1.35, .8])
    with left:
        st.markdown(
            """
            <div class="letter">
              <p><b>尊敬的陆文凯老师：</b></p>
              <p>
              您好！我是中国海洋大学勘查技术与工程专业学生潘高。此次致信，诚挚申请希望能有机会攻读您的硕士研究生，
              跟随您从事人工智能与地球物理反演方向的科研工作。
              </p>
              <p>
              我的科研兴趣主要聚焦于地震正演与反演、地震资料处理与解释、人工智能地球物理，以及深度学习/机器学习驱动的智能反演方法，
              重点探索物理机理约束与数据驱动模型相结合的地震反演新方法。
              </p>
              <div class="quote">
              我重点关注到您基于 CycleGAN 及神经网络开展的地球物理反演相关工作，这也是我目前科研工作的重要起点：
              我已在您相关研究成果基础上完成模型复现，并在此之上开展了自己的创新与改进工作。
              </div>
              <p>
              若能有幸得到您的认可与接纳，我将不再参加其他任何院校的夏令营考核；愿意从这个暑假开始，直至大四整个学年，
              全程留在北京跟进课题组科研任务，随时听从老师和组里安排，提前进组适应节奏、投入科研工作。
              </p>
              <p>
              入组后，我完全服从课题组整体安排。若有横向项目或工程类任务需要协助，我会踏实跟进、认真完成；
              若老师有新的前沿研究思路，我也会积极学习并落地实现；同时，我已有较成熟的研究思路与完整创新 idea，
              可自主开展既定方向研究，做到既能配合组里任务，也有可持续深耕的科研内容。
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown("### 支撑材料速览")
        for title, text in CAPABILITIES:
            st.markdown(
                f"""
                <div class="support-card">
                  <h3>{title}</h3>
                  <p>{text}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_research_story() -> None:
    section_title("核心研究 idea", "把申请信中最关键的科研想法独立展开，避免老师只看到奖项而看不到研究潜力。")
    cols = st.columns(3)
    for col, item in zip(cols, RESEARCH_STORY):
        with col:
            st.markdown(
                f"""
                <div class="research-card">
                  <span class="tag">{item["tag"]}</span>
                  <h3>{item["title"]}</h3>
                  <p>{item["body"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_project_figures() -> None:
    section_title("网络结构与初步成果", "这些图作为申请信中科研叙事的佐证：模型结构、低频先验、反演结果与误差指标。")
    for start in range(0, len(PROJECT_FIGURES), 2):
        cols = st.columns(2)
        for col, (title, filename, desc) in zip(cols, PROJECT_FIGURES[start : start + 2]):
            with col:
                st.markdown(f"**{title}**")
                st.caption(desc)
                image_or_notice(PROJECT_DIR / filename)


def render_qt_workflow() -> None:
    section_title("Qt 封装的 CycleGAN 预处理系统", "展示我不是只会调模型，也能把科研流程封装成可复用工具。")
    st.markdown(
        """
        <div class="letter">
        该系统围绕 CycleGAN 矩形训练流水线封装，覆盖 SEGY 重采样、正演模拟、传统反演接入、
        数据增强、矩形切割、模型推理、结果合并以及日志状态管理等模块。它的作用是把原本分散在多个脚本和命令行中的处理步骤
        整合为可视化流程，减少路径、参数和脚本顺序错误带来的返工成本。
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(2)
    for col, (title, filename) in zip(cols, QT_FIGURES):
        with col:
            st.markdown(f"**{title}**")
            image_or_notice(PROJECT_DIR / filename)


def render_research_images() -> None:
    section_title("科研与成果证明", "专利受理、创新项目等材料作为补充证明，不喧宾夺主。")
    image_cards = [
        ("一种立体式型材存取库", "专利受理证明", "c64e68a0c8a14cc07a8392f526b93c17.jpg"),
        ("一种立体式板材存放架", "专利受理证明", "c953f46a69869bc630e740cf7725bbe8.jpg"),
        ("创新项目 / 科研证明", "项目与成果材料", "图片2.png"),
    ]
    cols = st.columns(3)
    for col, (title, caption, filename) in zip(cols, image_cards):
        with col:
            st.markdown(f"**{title}**")
            image_or_notice(RESEARCH_DIR / filename, caption)


def render_application_award_summary() -> None:
    section_title("申请表中的奖项与成果摘要", "申请表包含完整个人信息，不适合公开展示原图；这里仅整理其中与申请相关的奖项、经历和科研成果。")
    cols = st.columns(4)
    for col, block in zip(cols, APPLICATION_AWARD_SUMMARY):
        items = "".join(f"<li>{item}</li>" for item in block["items"])
        with col:
            st.markdown(
                f"""
                <div class="support-card">
                  <h3>{block["group"]}</h3>
                  <ul>{items}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown(
        """
        <div class="note">
        说明：申请表原件中含身份证号、联系电话、邮箱、住址、照片等敏感信息，因此公开网页不展示原图。
        如老师需要核验，可在正式申请材料附件中查看原表及证书扫描件。
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_awards() -> None:
    section_title("奖项与荣誉证明", "作为侧翼材料展示综合素质，页面默认精简，可按需筛选。")
    categories = ["全部"] + sorted({item[1] for item in AWARDS})
    levels = ["全部"] + sorted({item[2] for item in AWARDS})
    col_a, col_b = st.columns([1, 1])
    category = col_a.selectbox("类别", categories)
    level = col_b.selectbox("级别", levels)
    filtered = [
        item
        for item in AWARDS
        if (category == "全部" or item[1] == category)
        and (level == "全部" or item[2] == level)
    ]
    st.caption(f"当前展示 {len(filtered)} 项公开证明材料")

    for row_start in range(0, len(filtered), 3):
        cols = st.columns(3)
        for col, (title, cat, lvl, filename) in zip(cols, filtered[row_start : row_start + 3]):
            with col:
                st.markdown(f'<span class="pill">{cat}</span><span class="pill">{lvl}</span>', unsafe_allow_html=True)
                st.markdown(f"**{title}**")
                image_or_notice(AWARD_DIR / filename)


def render_footer() -> None:
    st.markdown("---")
    st.markdown(
        """
        <div class="note">
        <b>公开边界</b>：本网页只展示适合公开的科研、工程封装、奖项、荣誉与专利材料；
        身份证、学生证、完整成绩单、四六级证明等敏感材料不放入公开仓库，应作为私下附件提交。
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="潘高 · 致陆文凯老师的硕士申请展示",
        page_icon="PG",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    inject_css()
    render_hero()
    render_application_letter()
    render_research_story()
    render_project_figures()
    render_qt_workflow()
    render_research_images()
    render_application_award_summary()
    render_awards()
    render_footer()


if __name__ == "__main__":
    main()
