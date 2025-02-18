import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und GannSquares
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'GannSquares': 1.0
        })
    )
