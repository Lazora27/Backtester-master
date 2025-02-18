import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'WeeklyCycle': 1.0
        })
    )
