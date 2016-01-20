import json


testbed = json.loads('{"type":"test-vpx-4esx-virtual-fullInstall-vcva-8gbmem","name":"vit_esx_path_pol-standalone-f89146891-0","podname":"sc-prd-vc034","vc":[{"name":"huralikoppia-vit_esx_path_pol-standalone-f89146891-0.vc.0","ip":"10.162.33.196","ip4":"10.162.33.196","ip6":null,"username":"root","password":"vmware","givenName":"vc.0","vimUsername":"administrator@vsphere.local","vimPassword":"Admin!23","vimPort":null,"deploymentType":"embedded","systemPNID":"sc-rdops-vm18-dhcp-33-196.eng.vmware.com"}],"esx":[{"name":"huralikoppia-vit_esx_path_pol-standalone-f89146891-0.esx.0","ip":"10.162.57.69","ip4":"10.162.57.69","ip6":null,"username":"root","password":"ca$hc0w","givenName":"esx.0","vimUsername":"root","vimPassword":"ca$hc0w","systemPNID":null},{"name":"huralikoppia-vit_esx_path_pol-standalone-f89146891-0.esx.1","ip":"10.162.33.200","ip4":"10.162.33.200","ip6":null,"username":"root","password":"ca$hc0w","givenName":"esx.1","vimUsername":"root","vimPassword":"ca$hc0w","systemPNID":null},{"name":"huralikoppia-vit_esx_path_pol-standalone-f89146891-0.esx.2","ip":"10.162.43.153","ip4":"10.162.43.153","ip6":null,"username":"root","password":"ca$hc0w","givenName":"esx.2","vimUsername":"root","vimPassword":"ca$hc0w","systemPNID":null},{"name":"huralikoppia-vit_esx_path_pol-standalone-f89146891-0.esx.3","ip":"10.162.34.152","ip4":"10.162.34.152","ip6":null,"username":"root","password":"ca$hc0w","givenName":"esx.3","vimUsername":"root","vimPassword":"ca$hc0w","systemPNID":null}],"iscsi":[],"nfs":[{"name":"huralikoppia-vit_esx_path_pol-standalone-f89146891-0.nfs.0","ip":"10.162.55.66","ip4":"10.162.55.66","ip6":null,"username":"root","password":"ca$hc0w","givenName":"nfs.0","systemPNID":null}],"hostdSim":[],"mobAgent":[],"vcg":[],"genericVm":[],"pdpVm":[],"ovfVm":[],"vsm":[],"vcd":[],"vcBench":[],"psa":[],"vrops":[],"vraCafe":[],"vraSso":[],"logInsight":[],"network":[],"sampleVm":[],"nsxm":[],"nsxc":[],"vnimbus":[]}')

esxs = [x['ip'] for x in testbed['esx']]

print(' '.join(esxs))