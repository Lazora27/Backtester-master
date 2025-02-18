import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
