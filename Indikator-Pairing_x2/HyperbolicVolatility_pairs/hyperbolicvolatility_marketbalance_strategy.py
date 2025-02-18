import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und MarketBalance
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'MarketBalance': 1.0
        })
    )
