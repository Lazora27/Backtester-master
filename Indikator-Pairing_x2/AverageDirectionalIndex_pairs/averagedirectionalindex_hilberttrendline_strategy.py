import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
