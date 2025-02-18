import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
