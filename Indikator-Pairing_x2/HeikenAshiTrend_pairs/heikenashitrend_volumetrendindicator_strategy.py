import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
