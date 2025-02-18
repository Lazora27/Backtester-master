import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und MassIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'MassIndex': 1.0
        })
    )
