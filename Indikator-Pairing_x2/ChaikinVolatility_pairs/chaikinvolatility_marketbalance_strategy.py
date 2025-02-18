import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'MarketBalance': 1.0
        })
    )
