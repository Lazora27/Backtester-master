import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BalanceMomentum': 1.0
        })
    )
