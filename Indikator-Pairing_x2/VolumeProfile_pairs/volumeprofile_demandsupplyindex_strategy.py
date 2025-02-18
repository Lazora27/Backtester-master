import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
