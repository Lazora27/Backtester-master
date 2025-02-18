import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TickActivityIndex': 1.0
        })
    )
