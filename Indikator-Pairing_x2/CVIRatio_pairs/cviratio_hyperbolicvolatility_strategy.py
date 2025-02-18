import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
