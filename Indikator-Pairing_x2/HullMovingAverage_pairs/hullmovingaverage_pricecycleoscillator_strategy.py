import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
