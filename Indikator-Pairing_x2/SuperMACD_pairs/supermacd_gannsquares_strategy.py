import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und GannSquares
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'GannSquares': 1.0
        })
    )
