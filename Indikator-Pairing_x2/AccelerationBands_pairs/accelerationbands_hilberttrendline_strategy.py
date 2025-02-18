import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'HilbertTrendline': 1.0
        })
    )
