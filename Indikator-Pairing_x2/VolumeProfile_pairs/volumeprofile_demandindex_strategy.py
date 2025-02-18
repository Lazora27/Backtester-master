import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und DemandIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'DemandIndex': 1.0
        })
    )
