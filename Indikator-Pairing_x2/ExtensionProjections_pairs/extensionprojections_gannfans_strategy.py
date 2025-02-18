import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und GannFans
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'GannFans': 1.0
        })
    )
