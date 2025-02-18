import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'Fisher': 1.0
        })
    )
