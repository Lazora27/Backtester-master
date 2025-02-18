import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TickVolume
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TickVolume': 1.0
        })
    )
