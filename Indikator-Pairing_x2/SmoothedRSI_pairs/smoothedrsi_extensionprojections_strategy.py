import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ExtensionProjections': 1.0
        })
    )
