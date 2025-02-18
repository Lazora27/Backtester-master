import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'WeeklyCycle': 1.0
        })
    )
