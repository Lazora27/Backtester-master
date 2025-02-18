import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BarStrength
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BarStrength': 1.0
        })
    )
