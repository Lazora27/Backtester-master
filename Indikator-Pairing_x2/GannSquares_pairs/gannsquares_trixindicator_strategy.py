import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'TRIXIndicator': 1.0
        })
    )
