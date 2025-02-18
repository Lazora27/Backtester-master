import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'WolfeWaves': 1.0
        })
    )
