from pathlib import Path

import streamlit as st


ROOT = Path(__file__).parent
AWARD_DIR = ROOT / "assets" / "awards"
RESEARCH_DIR = ROOT / "assets" / "research"


PROFILE = {
    "name": "潘高",
    "school": "中国海洋大学",
    "major": "勘查技术与工程",
    "target": "人工智能与地球物理反演方向",
    "focus": "物理约束深度学习、地震正演与反演、稀疏井约束智能反演",
}


METRICS = [
    ("专业成绩", "班级第 2", "地震勘探方向课程均分 92.3"),
    ("科研主线", "CycleGAN + 物理约束", "固定 Ricker 正演闭环与稀疏井监督"),
    ("代表结果", "R2 = 0.9731", "测试区域 normalized-domain 指标"),
    ("工程封装", "Qt + Streamlit", "预处理、推理、评价与展示流程"),
]


RESEARCH_ITEMS = [
    {
        "title": "稀疏井约束的物理驱动声波阻抗反演",
        "tag": "省级大创 / 第一负责人",
        "body": (
            "围绕地震数据与波阻抗模型之间的非唯一性、低频信息缺失和深度学习结果地质合理性不足问题，"
            "构建从数据准备、正演模拟、剖面切块、训练、拼接到定量评价的完整实验流程。"
        ),
        "points": [
            "以固定 Ricker 子波正演算子替代可训练反向生成器，形成地震域物理闭环。",
            "利用约 0.8% 稀疏井道构建低频先验，减少对完整阻抗标签的依赖。",
            "建立 RMSE、NRMSE、相关系数、R2、低频分量 R2 等评价流程。",
        ],
    },
    {
        "title": "CycleGAN 预处理与实验工作流封装",
        "tag": "工程实现 / 科研效率",
        "body": (
            "将 SEGY 重采样、正演模拟、传统反演接入、数据增强、矩形切割、模型推理、结果合并和日志管理"
            "整理为可复用流程，降低重复调参与路径错误带来的成本。"
        ),
        "points": [
            "Qt 端适合本地数据处理与脚本调用。",
            "Streamlit 端适合网页演示、学术交流和项目汇报。",
            "支持参数固化、批量实验、结果出图和阶段性报告生成。",
        ],
    },
    {
        "title": "实用新型专利申请受理",
        "tag": "成果转化 / 工程应用",
        "body": (
            "参与申报两项立体式仓储结构相关实用新型专利，并形成从实际需求、结构设计到材料提交的成果转化经验。"
        ),
        "points": [
            "一种立体式型材存取库，申请号：202522002910.X。",
            "一种立体式板材存放架，申请号：202522002911.4。",
            "经历强化了算法设计、软件实现、实验验证和实际需求之间的闭环意识。",
        ],
    },
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
            --muted: #65736f;
            --line: #dbe4de;
            --paper: #f7f8f4;
            --teal: #0f766e;
            --gold: #b7791f;
            --clay: #9f5132;
            --green: #3f7f50;
        }
        .stApp {
            background:
              linear-gradient(180deg, rgba(247,248,244,0.98), rgba(242,246,241,0.98));
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
            border-left: 6px solid var(--teal);
            padding: 1.2rem 0 1.2rem 1.4rem;
            margin-bottom: 1.2rem;
        }
        .hero .eyebrow {
            color: var(--teal);
            font-size: .92rem;
            font-weight: 800;
            margin-bottom: .35rem;
        }
        .hero h1 {
            font-size: clamp(2.2rem, 5vw, 4.6rem);
            line-height: 1.02;
            margin: 0 0 .7rem 0;
        }
        .hero p {
            max-width: 880px;
            color: #33413d;
            font-size: 1.05rem;
            line-height: 1.75;
        }
        .metric {
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1rem;
            min-height: 130px;
            background: rgba(255,255,255,.68);
        }
        .metric span {
            display: block;
            color: var(--muted);
            font-size: .86rem;
            margin-bottom: .35rem;
        }
        .metric strong {
            display: block;
            font-size: 1.38rem;
            color: var(--teal);
            margin-bottom: .45rem;
        }
        .metric p { margin: 0; color: #52615c; font-size: .92rem; line-height: 1.55; }
        .section-title {
            margin: 2rem 0 .75rem 0;
            padding-top: .4rem;
            border-top: 1px solid var(--line);
        }
        .section-title h2 { margin-bottom: .2rem; }
        .section-title p { color: var(--muted); margin-top: 0; }
        .research-card {
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1.05rem 1.05rem .9rem;
            background: rgba(255,255,255,.76);
            height: 100%;
        }
        .research-card .tag {
            color: var(--clay);
            font-weight: 800;
            font-size: .86rem;
            margin-bottom: .4rem;
        }
        .research-card h3 { margin: 0 0 .45rem 0; font-size: 1.15rem; }
        .research-card p, .research-card li { color: #4c5b56; line-height: 1.62; }
        .award-meta {
            display: inline-flex;
            gap: .45rem;
            align-items: center;
            color: var(--muted);
            font-size: .86rem;
            margin-bottom: .35rem;
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


def render_hero() -> None:
    st.markdown(
        f"""
        <div class="hero">
          <div class="eyebrow">{PROFILE["school"]} · {PROFILE["major"]}</div>
          <h1>{PROFILE["name"]}</h1>
          <p>
            面向 {PROFILE["target"]} 的研究型申请展示网站。核心主线是
            <b>{PROFILE["focus"]}</b>：把地震波传播机理、稀疏井先验、固定正演算子和生成式网络结合起来，
            让深度学习反演结果回到可解释、可验证、可复现的地球物理语境中。
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metrics() -> None:
    cols = st.columns(4)
    for col, (label, value, desc) in zip(cols, METRICS):
        with col:
            st.markdown(
                f"""
                <div class="metric">
                    <span>{label}</span>
                    <strong>{value}</strong>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_research() -> None:
    section_title("研究与工程主线", "用少量关键项目讲清能力结构：科研问题、方法创新、工程落地。")
    cols = st.columns(3)
    for col, item in zip(cols, RESEARCH_ITEMS):
        points = "".join(f"<li>{point}</li>" for point in item["points"])
        with col:
            st.markdown(
                f"""
                <div class="research-card">
                    <div class="tag">{item["tag"]}</div>
                    <h3>{item["title"]}</h3>
                    <p>{item["body"]}</p>
                    <ul>{points}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_plan() -> None:
    section_title("申请定位", "从申请信中抽取出的导师匹配逻辑与进组后可贡献方向。")
    left, right = st.columns([1.08, 0.92])
    with left:
        st.markdown(
            """
            - 研究兴趣聚焦地震正演与反演、地震资料处理与解释、人工智能地球物理、深度学习/机器学习驱动的智能反演方法。
            - 重点探索物理机理约束与数据驱动模型结合的地震反演新方法，强调低频趋势合理性、地质结构连续性和传统流程可衔接。
            - 已完成基于 CycleGAN 的模型复现与创新改进，后续希望继续围绕物理约束、稀疏井监督、多尺度多频段生成模型和不确定性评价深挖。
            - 入组后可参与横向项目、工程化任务、软件封装、实验流程自动化、汇报材料与成果固化。
            """
        )
    with right:
        st.markdown(
            """
            <div class="note">
            <b>展示建议</b><br>
            这个网站适合放在 GitHub 仓库首页或 Streamlit Community Cloud。
            公开版本建议只展示科研、竞赛、荣誉与专利材料；身份证、学生证、完整成绩单、四六级证明等隐私材料应通过私下附件提交。
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_research_images() -> None:
    section_title("科研证明", "专利受理与创新项目相关证明，可作为成果转化和工程意识的补充材料。")
    image_cards = [
        ("一种立体式型材存取库", "专利受理证明", "c64e68a0c8a14cc07a8392f526b93c17.jpg"),
        ("一种立体式板材存放架", "专利受理证明", "c953f46a69869bc630e740cf7725bbe8.jpg"),
        ("创新项目 / 科研证明", "项目与成果材料", "图片2.png"),
    ]
    cols = st.columns(3)
    for col, (title, caption, filename) in zip(cols, image_cards):
        path = RESEARCH_DIR / filename
        with col:
            st.markdown(f"**{title}**")
            if path.exists():
                st.image(str(path), caption=caption, use_container_width=True)
            else:
                st.info(f"未找到：{filename}")


def render_awards() -> None:
    section_title("证据库", "按类别筛选奖项、竞赛、荣誉与社会实践证明。")
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
            path = AWARD_DIR / filename
            with col:
                st.markdown(
                    f"""
                    <div class="award-meta">
                        <span class="pill">{cat}</span>
                        <span class="pill">{lvl}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(f"**{title}**")
                if path.exists():
                    st.image(str(path), use_container_width=True)
                else:
                    st.warning(f"图片缺失：{filename}")


def render_footer() -> None:
    st.markdown("---")
    st.markdown(
        """
        **公开边界**：本仓库版本不放置身份证、学生证、完整成绩单等敏感材料。  
        **材料来源**：根据申请信、个人陈述、奖项证明、专利受理材料整理生成。
        """
    )


def main() -> None:
    st.set_page_config(
        page_title="潘高 · 研究型申请作品集",
        page_icon="PG",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    inject_css()
    render_hero()
    render_metrics()
    render_research()
    render_plan()
    render_research_images()
    render_awards()
    render_footer()


if __name__ == "__main__":
    main()
