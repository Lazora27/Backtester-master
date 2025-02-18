import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'KeltnerChannels': 1.0
        })
    )
