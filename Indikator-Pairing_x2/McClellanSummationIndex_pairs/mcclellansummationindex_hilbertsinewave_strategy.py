import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
