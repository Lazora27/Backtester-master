import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'ProjectionBands': 1.0
        })
    )
