import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
