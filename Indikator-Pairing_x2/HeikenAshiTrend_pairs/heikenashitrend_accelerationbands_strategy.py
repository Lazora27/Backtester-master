import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'AccelerationBands': 1.0
        })
    )
