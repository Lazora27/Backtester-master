import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TimeCycle': 1.0
        })
    )
