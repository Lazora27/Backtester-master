import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und TrueRange
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'TrueRange': 1.0
        })
    )
