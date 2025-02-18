import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
