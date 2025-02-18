import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und CyberCycle
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'CyberCycle': 1.0
        })
    )
