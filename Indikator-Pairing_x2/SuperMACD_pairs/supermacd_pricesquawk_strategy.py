import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'PriceSquawk': 1.0
        })
    )
