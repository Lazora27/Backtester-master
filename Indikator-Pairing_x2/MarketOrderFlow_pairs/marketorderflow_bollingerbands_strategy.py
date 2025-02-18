import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'BollingerBands': 1.0
        })
    )
