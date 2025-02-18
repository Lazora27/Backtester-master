import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'BradleySiderograph': 1.0
        })
    )
