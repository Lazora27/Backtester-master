import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
