import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'AccelerationBands': 1.0
        })
    )
