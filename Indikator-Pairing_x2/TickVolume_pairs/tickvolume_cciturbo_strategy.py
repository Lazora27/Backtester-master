import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CCITurbo': 1.0
        })
    )
