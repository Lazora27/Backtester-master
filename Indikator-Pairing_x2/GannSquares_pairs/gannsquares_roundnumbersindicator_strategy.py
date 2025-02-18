import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
