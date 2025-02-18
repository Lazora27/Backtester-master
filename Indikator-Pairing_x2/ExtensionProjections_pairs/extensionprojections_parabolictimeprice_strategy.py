import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
