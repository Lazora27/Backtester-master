import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
