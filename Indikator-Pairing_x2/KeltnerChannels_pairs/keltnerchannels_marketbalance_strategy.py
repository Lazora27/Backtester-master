import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und MarketBalance
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'MarketBalance': 1.0
        })
    )
