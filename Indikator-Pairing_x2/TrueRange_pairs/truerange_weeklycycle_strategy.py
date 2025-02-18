import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'WeeklyCycle': 1.0
        })
    )
