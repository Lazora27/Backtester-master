import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und GannAngles
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'GannAngles': 1.0
        })
    )
