import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'KeltnerChannels': 1.0
        })
    )
