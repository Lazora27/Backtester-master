import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'HilbertSinewave': 1.0
        })
    )
