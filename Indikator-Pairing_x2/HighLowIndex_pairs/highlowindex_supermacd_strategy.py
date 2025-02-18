import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und SuperMACD
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'SuperMACD': 1.0
        })
    )
