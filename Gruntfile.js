module.exports = function (grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        meta: {
        },
        jshint: {
            files: [
                'Gruntfile.js',
                '<%= pkg.name %>/assets/js/spa/*.js',
                '<%= pkg.name %>/assets/js/custom.js'
            ],
            options: {
                globals: {
                    jQuery: true
                }
            }
        },
        copy: {
            customjs: {
                expand: true,
                cwd: '<%= pkg.name %>/assets/js',
                src: [
                    '**',
                ],
                dest: '<%= pkg.name %>/static/js'
            },
            customcss: {
                expand: true,
                cwd: '<%= pkg.name %>/assets/css',
                src: [
                    '**',
                ],
                dest: '<%= pkg.name %>/static/css'
            },
            customimg: {
                expand: true,
                cwd: '<%= pkg.name %>/assets/img',
                src: [
                    '**',
                ],
                dest: '<%= pkg.name %>/static/img'
            },
            js: {
                expand: true,
                flatten: true,
                src: [
                    'bower_components/angular/angular.js',
                    'bower_components/angular/angular.min.js',
                    'bower_components/angular-route/angular-route.js',
                    'bower_components/angular-route/angular-route.min.js',
                    'bower_components/jquery/dist/jquery.js',
                    'bower_components/jquery/dist/jquery.min.js',
                    'bower_components/bootstrap/dist/js/bootstrap.js',
                    'bower_components/bootstrap/dist/js/bootstrap.min.js'
                ],
                dest: '<%= pkg.name %>/static/js'
            },
            css: {
                expand: true,
                flatten: true,
                src: [
                    'bower_components/bootstrap/dist/css/*'
                ],
                dest: '<%= pkg.name %>/static/css'
            },
            fonts: {
                expand: true,
                flatten: true,
                src: [
                    'bower_components/bootstrap/dist/fonts/*'
                ],
                dest: '<%= pkg.name %>/static/fonts'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
                        '<%= grunt.template.today("yyyy-mm-dd") %> */\n'
            },
            build: {
                src: [
                    '<%= pkg.name %>/assets/js/custom.js'
                ],
                dest: '<%= pkg.name %>/assets/js/custom.min.js'
            }
        },
        watch: {
            files: ['<%= jshint.files %>'],
            tasks: ['jshint']
        }
    });

    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['jshint']);
    grunt.registerTask('def', ['jshint', 'uglify', 'copy']);
};
