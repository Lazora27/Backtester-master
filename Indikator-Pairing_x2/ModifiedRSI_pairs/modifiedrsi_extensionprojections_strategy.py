import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ExtensionProjections': 1.0
        })
    )
