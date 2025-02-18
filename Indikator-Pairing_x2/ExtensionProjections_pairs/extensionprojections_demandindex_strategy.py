import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'DemandIndex': 1.0
        })
    )
