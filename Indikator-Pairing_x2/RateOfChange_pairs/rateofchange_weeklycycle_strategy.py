import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'WeeklyCycle': 1.0
        })
    )
