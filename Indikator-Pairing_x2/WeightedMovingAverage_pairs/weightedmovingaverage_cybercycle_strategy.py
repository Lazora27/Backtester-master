import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und CyberCycle
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'CyberCycle': 1.0
        })
    )
