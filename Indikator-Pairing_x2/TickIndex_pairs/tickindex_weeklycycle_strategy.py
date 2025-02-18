import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
