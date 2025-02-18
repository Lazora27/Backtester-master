import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_HighLowDifference_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und HighLowDifference
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'HighLowDifference': 1.0
        })
    )
