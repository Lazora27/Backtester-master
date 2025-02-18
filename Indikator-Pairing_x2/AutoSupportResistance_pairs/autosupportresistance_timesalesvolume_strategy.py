import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
