import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
