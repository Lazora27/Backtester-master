import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
