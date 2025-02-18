import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeCycle_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeCycle und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TimeCycle': 1.0,
            'WeeklyCycle': 1.0
        })
    )
