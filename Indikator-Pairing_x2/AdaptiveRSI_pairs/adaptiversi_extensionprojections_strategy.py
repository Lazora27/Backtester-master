import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ExtensionProjections': 1.0
        })
    )
