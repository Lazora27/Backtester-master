import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SuperTrend
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SuperTrend': 1.0
        })
    )
