import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'WeeklyCycle': 1.0
        })
    )
