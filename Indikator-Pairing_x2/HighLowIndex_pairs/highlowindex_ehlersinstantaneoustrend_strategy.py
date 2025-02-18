import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_EhlersInstantaneousTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und EhlersInstantaneousTrend
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'EhlersInstantaneousTrend': 1.0
        })
    )
