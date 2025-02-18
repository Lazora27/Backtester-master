import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und DemandIndex
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'DemandIndex': 1.0
        })
    )
