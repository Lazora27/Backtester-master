import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TrueRange
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TrueRange': 1.0
        })
    )
