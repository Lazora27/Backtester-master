import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
