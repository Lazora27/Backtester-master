import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und MassIndex
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'MassIndex': 1.0
        })
    )
