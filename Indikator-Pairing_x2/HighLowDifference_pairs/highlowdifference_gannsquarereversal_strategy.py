import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'GannSquareReversal': 1.0
        })
    )
