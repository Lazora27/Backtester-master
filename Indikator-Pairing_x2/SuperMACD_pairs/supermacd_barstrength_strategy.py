import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und BarStrength
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'BarStrength': 1.0
        })
    )
