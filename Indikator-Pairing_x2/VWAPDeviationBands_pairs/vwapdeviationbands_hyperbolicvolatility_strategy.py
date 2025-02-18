import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
