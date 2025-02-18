import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'AdaptiveATR': 1.0
        })
    )
