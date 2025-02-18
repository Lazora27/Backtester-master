import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'AverageLogRange': 1.0
        })
    )
