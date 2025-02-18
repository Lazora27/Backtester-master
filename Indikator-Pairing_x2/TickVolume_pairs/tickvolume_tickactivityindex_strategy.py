import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TickActivityIndex': 1.0
        })
    )
