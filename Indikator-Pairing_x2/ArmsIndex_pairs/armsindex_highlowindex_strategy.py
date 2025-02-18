import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_HighLowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und HighLowIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'HighLowIndex': 1.0
        })
    )
