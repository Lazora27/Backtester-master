import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
