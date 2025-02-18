import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'ExtensionProjections': 1.0
        })
    )
