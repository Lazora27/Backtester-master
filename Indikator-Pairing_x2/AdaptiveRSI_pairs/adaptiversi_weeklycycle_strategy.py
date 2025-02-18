import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'WeeklyCycle': 1.0
        })
    )
