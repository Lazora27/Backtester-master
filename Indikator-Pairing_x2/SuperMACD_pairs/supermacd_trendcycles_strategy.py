import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TrendCycles': 1.0
        })
    )
