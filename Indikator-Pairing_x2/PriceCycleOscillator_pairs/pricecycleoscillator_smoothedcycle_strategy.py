import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceCycleOscillator_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceCycleOscillator und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PriceCycleOscillator': 1.0,
            'SmoothedCycle': 1.0
        })
    )
