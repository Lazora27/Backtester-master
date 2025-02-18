import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'VortexIndicator': 1.0
        })
    )
