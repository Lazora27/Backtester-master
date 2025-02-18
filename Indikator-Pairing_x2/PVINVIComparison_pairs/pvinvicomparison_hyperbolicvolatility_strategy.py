import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
