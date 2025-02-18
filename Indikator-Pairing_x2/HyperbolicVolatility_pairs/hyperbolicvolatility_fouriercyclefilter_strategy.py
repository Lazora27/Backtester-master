import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
