import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'VortexIndicator': 1.0
        })
    )
