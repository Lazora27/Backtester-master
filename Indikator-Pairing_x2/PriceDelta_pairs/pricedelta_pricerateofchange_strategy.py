import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
