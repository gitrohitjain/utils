        import matplotlib.pyplot as plt
        
        images = [orig, mask]
        fig, axs = plt.subplots(len(images), 1, figsize=(10, 10), tight_layout=True)
        
        for ax in axs:
            ax.axis('off')

        for i, image in enumerate(images):
            axs[i].imshow(image, cmap='gray')
      
        plt.savefig(f'DIR/{savename}', pad_inches=0)
