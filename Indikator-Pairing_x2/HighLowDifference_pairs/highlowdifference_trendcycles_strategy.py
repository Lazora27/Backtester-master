import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TrendCycles': 1.0
        })
    )
