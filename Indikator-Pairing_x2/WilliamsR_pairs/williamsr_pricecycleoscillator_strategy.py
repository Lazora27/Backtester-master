import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
