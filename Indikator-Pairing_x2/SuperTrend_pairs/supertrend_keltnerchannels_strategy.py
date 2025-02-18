import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'KeltnerChannels': 1.0
        })
    )
