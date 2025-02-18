import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
