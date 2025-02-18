import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'GannSquareReversal': 1.0
        })
    )
