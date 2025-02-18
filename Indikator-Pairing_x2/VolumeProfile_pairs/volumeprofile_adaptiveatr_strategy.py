import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AdaptiveATR': 1.0
        })
    )
