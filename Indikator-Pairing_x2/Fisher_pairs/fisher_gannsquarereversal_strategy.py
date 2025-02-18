import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'GannSquareReversal': 1.0
        })
    )
