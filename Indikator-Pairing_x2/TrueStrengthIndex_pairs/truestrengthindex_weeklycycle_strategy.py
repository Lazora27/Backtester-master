import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
