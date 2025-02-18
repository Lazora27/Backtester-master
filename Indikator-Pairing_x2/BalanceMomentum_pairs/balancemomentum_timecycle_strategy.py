import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TimeCycle
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TimeCycle': 1.0
        })
    )
