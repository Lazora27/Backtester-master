import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
