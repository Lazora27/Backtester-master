import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'HilbertSinewave': 1.0
        })
    )
