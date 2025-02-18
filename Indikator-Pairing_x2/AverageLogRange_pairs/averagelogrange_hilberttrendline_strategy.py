import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'HilbertTrendline': 1.0
        })
    )
