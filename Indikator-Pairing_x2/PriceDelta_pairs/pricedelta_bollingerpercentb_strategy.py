import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'BollingerPercentB': 1.0
        })
    )
