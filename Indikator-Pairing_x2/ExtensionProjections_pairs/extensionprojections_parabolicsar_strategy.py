import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ParabolicSAR': 1.0
        })
    )
