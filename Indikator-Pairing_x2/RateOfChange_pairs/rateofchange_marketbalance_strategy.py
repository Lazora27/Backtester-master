import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MarketBalance
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MarketBalance': 1.0
        })
    )
