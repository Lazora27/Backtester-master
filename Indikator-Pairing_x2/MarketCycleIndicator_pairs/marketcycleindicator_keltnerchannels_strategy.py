import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'KeltnerChannels': 1.0
        })
    )
