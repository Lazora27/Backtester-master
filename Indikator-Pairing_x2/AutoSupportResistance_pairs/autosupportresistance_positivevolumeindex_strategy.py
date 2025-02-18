import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
