import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'EhlersDecycler': 1.0
        })
    )
