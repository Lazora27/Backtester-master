import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ExtensionProjections': 1.0
        })
    )
