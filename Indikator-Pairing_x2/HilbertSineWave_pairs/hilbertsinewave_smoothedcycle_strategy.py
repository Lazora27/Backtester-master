import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'SmoothedCycle': 1.0
        })
    )
