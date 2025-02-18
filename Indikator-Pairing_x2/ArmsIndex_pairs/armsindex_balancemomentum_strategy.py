import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'BalanceMomentum': 1.0
        })
    )
