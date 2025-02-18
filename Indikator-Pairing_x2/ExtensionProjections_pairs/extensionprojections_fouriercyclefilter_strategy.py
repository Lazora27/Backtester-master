import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
