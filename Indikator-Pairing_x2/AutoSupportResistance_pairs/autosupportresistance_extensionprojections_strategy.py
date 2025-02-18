import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ExtensionProjections': 1.0
        })
    )
