import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
