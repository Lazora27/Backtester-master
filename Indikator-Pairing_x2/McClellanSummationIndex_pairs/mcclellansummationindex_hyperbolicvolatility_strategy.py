import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
