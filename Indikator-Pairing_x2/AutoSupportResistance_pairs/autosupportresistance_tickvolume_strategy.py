import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und TickVolume
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'TickVolume': 1.0
        })
    )
