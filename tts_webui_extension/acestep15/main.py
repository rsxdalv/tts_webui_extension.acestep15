import gradio as gr


def acestep15_ui():
    gr.Markdown(
        """
        ## AceStep 1.5
        
        Click on the "?" buttons to see hints.
        
        Current issues:

        The default installation currently does not setup nano-vllm thus the performance is decreased. Manually installing nano-vllm will work with the UI automatically.

        Examples via "🎲 Click Me" do not work currently.

        The checkpoints (10GB) are downladed to site-packages, e.g., installer_files/env/lib/site-packages/checkpoints/
        
        This extension will be updated periodically, because the official Ace-Step repository is still being actively modified.
"""
    )

    from acestep.ui.gradio import create_gradio_interface
    from acestep.handler import AceStepHandler
    from acestep.llm_inference import LLMHandler
    from acestep.dataset_handler import DatasetHandler

    dit_handler = AceStepHandler()
    llm_handler = LLMHandler()
    dataset_handler = DatasetHandler()
    create_gradio_interface(
        dit_handler,
        llm_handler,
        dataset_handler,
        init_params={"pre_initialized": False},
        language="en",
    )


def extension__tts_generation_webui():
    acestep15_ui()

    return {
        "package_name": "tts_webui_extension.acestep15",
        "name": "Acestep15",
        "requirements": "git+https://github.com/rsxdalv/tts_webui_extension.acestep15@main",
        "description": "A template extension for TTS Generation WebUI",
        "extension_type": "interface",
        "extension_class": "text-to-speech",
        "author": "Your Name",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/rsxdalv/tts_webui_extension.acestep15",
        "extension_website": "https://github.com/rsxdalv/tts_webui_extension.acestep15",
        "extension_platform_version": "0.0.1",
    }


if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        with gr.Tab("Acestep15", id="acestep15"):
            acestep15_ui()

    demo.launch(
        server_port=7772,  # Change this port if needed
    )
