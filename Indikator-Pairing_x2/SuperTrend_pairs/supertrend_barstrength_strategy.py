import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und BarStrength
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'BarStrength': 1.0
        })
    )
