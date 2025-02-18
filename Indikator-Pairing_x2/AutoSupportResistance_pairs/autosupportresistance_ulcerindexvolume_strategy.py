import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
