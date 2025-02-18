import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
