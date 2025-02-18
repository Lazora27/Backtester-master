import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
