import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
