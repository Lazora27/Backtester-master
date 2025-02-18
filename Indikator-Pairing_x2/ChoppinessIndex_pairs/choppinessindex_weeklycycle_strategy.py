import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
