import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'AverageLogRange': 1.0
        })
    )
