import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
