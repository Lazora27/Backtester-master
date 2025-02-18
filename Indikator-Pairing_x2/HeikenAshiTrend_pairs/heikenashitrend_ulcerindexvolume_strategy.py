import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
