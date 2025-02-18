import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'GannSquareReversal': 1.0
        })
    )
