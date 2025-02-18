import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'AverageLogRange': 1.0
        })
    )
