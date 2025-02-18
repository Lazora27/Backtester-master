import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
