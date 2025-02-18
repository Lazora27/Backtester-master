import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'HilbertSinewave': 1.0
        })
    )
