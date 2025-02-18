import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'HilbertSinewave': 1.0
        })
    )
