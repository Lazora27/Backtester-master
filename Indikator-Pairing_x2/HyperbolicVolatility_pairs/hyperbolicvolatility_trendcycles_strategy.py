import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'TrendCycles': 1.0
        })
    )
