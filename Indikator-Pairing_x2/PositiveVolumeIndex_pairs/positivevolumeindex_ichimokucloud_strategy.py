import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
