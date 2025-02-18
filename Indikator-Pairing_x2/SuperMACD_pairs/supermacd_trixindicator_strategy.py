import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TRIXIndicator': 1.0
        })
    )
