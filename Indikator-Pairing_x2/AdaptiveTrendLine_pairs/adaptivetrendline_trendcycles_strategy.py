import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'TrendCycles': 1.0
        })
    )
