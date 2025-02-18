import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und PriceDelta
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'PriceDelta': 1.0
        })
    )
