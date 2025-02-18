import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
