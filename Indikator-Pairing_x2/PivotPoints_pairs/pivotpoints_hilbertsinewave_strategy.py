import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HilbertSinewave': 1.0
        })
    )
