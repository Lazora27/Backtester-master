import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
