import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'LiquidityIndex': 1.0
        })
    )
