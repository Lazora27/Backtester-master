import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und CyberCycle
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'CyberCycle': 1.0
        })
    )
