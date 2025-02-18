import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
