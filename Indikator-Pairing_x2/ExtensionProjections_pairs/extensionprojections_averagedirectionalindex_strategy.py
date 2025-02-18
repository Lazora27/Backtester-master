import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
