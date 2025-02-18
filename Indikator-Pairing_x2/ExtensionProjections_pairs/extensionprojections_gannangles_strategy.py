import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und GannAngles
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'GannAngles': 1.0
        })
    )
