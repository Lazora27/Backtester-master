import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'ExtensionProjections': 1.0
        })
    )
