import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'TrueRange': 1.0
        })
    )
