import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
