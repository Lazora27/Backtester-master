import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'BalanceMomentum': 1.0
        })
    )
