import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
