import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'HilbertSinewave': 1.0
        })
    )
