import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
