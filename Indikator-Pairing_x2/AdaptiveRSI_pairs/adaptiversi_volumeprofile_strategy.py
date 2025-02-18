import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'VolumeProfile': 1.0
        })
    )
