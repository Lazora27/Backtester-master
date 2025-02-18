import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
