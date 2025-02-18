import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
