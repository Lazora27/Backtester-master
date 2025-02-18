import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
