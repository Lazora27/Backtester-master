import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
