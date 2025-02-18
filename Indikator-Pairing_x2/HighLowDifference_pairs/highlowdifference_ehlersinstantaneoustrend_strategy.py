import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_EhlersInstantaneousTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und EhlersInstantaneousTrend
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'EhlersInstantaneousTrend': 1.0
        })
    )
