import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverageCycleDetector_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverageCycleDetector und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MovingAverageCycleDetector': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
