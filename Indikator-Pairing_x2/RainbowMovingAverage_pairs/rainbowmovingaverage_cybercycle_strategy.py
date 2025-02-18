import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und CyberCycle
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'CyberCycle': 1.0
        })
    )
