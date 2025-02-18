import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
