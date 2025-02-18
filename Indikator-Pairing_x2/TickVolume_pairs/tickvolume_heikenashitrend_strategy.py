import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
