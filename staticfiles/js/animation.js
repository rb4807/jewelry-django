const contentSections = document.querySelectorAll('.content-section');
        const scrollFactor = 0.1;

        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset;

            contentSections.forEach((section, index) => {
                const offset = section.offsetTop;
                const scrollOffset = scrollTop + window.innerHeight * scrollFactor;

                if (offset < scrollOffset) {
                    section.classList.add('active');
                } else {
                    section.classList.remove('active');
                }
            });
        });