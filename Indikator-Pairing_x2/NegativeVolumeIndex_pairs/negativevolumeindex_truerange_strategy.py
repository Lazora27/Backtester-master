import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'TrueRange': 1.0
        })
    )
