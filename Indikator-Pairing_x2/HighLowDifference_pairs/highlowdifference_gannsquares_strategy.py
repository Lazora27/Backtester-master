import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und GannSquares
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'GannSquares': 1.0
        })
    )
