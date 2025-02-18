import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und WilliamsR
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'WilliamsR': 1.0
        })
    )
