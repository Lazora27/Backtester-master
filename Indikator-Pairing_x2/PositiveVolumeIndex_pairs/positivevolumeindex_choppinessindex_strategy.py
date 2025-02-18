import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
