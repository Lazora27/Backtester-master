import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedVolatilityIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedVolatilityIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'NormalizedVolatilityIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
