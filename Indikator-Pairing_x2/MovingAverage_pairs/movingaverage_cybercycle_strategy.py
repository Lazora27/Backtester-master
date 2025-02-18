import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'CyberCycle': 1.0
        })
    )
