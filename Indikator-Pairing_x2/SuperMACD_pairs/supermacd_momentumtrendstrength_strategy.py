import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
