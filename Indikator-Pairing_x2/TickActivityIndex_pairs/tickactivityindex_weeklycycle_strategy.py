import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
