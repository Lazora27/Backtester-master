import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'HilbertSinewave': 1.0
        })
    )
