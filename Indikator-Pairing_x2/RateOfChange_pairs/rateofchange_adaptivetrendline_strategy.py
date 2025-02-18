import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
