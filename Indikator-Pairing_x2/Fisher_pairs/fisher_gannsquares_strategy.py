import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und GannSquares
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'GannSquares': 1.0
        })
    )
