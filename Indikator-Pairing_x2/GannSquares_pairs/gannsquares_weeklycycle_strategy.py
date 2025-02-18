import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'WeeklyCycle': 1.0
        })
    )
