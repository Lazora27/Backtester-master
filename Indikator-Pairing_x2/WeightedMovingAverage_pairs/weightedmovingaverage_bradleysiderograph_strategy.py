import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'BradleySiderograph': 1.0
        })
    )
