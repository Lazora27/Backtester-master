import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'WeeklyCycle': 1.0
        })
    )
