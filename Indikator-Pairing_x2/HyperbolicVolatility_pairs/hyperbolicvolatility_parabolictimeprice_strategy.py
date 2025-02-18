import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
