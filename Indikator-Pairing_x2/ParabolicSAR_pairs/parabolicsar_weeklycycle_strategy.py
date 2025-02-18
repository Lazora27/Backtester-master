import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'WeeklyCycle': 1.0
        })
    )
