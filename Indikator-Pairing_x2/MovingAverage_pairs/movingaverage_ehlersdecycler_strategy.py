import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'EhlersDecycler': 1.0
        })
    )
