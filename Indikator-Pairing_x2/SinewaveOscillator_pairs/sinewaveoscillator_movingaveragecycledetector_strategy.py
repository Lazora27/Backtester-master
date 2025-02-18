import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SinewaveOscillator_MovingAverageCycleDetector_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SinewaveOscillator und MovingAverageCycleDetector
    """
    
    params = (
        ('indicators', {
            'SinewaveOscillator': {
                'class': SinewaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SinewaveOscillator'>
            },
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            }
        }),
        ('weights', {
            'SinewaveOscillator': 1.0,
            'MovingAverageCycleDetector': 1.0
        })
    )
