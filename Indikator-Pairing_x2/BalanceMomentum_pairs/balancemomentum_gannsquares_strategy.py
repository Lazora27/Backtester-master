import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und GannSquares
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'GannSquares': 1.0
        })
    )
