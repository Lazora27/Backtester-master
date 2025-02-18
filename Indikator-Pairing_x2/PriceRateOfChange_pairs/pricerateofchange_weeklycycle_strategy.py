import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'WeeklyCycle': 1.0
        })
    )
