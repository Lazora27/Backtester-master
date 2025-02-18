import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'BalanceMomentum': 1.0
        })
    )
