import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und MarketBalance
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'MarketBalance': 1.0
        })
    )
