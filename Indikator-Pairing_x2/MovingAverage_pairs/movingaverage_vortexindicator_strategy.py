import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'VortexIndicator': 1.0
        })
    )
