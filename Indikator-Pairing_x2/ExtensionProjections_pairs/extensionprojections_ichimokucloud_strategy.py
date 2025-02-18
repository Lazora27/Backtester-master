import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'IchimokuCloud': 1.0
        })
    )
