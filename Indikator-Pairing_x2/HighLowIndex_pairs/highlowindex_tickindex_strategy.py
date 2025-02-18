import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TickIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TickIndex': 1.0
        })
    )
