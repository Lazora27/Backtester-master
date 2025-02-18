import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'VolumeDelta': 1.0
        })
    )
