import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'WeeklyCycle': 1.0
        })
    )
