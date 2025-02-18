import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und MarketBalance
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'MarketBalance': 1.0
        })
    )
