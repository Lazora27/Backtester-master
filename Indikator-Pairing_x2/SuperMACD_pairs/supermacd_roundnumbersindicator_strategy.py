import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
