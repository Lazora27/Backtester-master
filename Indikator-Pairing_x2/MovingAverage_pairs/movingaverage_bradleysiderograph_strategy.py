import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'BradleySiderograph': 1.0
        })
    )
