import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MassIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MassIndex': 1.0
        })
    )
