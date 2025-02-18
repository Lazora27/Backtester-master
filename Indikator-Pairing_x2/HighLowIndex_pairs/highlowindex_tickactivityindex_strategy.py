import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TickActivityIndex': 1.0
        })
    )
