import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'GannSquareReversal': 1.0
        })
    )
