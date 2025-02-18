import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
