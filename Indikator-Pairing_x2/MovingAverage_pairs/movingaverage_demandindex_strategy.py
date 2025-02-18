import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und DemandIndex
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'DemandIndex': 1.0
        })
    )
