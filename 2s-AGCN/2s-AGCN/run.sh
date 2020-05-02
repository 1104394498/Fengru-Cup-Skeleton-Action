python3 -u data_gen/ntu_gendata.py
python3 -u python data_gen/gen_bone_data.py
python3 -u run.py --config ./config/nturgbd-cross-view/train_joint.yaml
python3 -u run.py --config ./config/nturgbd-cross-view/train_bone.yaml
python3 -u predict.py --config ./config/nturgbd-cross-view/test_joint.yaml --save-score true
python3 -u predict.py --config ./config/nturgbd-cross-view/test_bone.yaml --save-score true
python3 -u predict.py --config ./config/nturgbd-cross-subject/test_joint.yaml --save-score true
python3 -u predict.py --config ./config/nturgbd-cross-subject/test_bone.yaml --save-score true
python3 -u ensemble.py --datasets ntu/xview
python3 -u ensemble.py --datasets ntu/xsub

