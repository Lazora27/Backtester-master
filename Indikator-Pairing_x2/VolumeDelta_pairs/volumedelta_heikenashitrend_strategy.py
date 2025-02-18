import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
