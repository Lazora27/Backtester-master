import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
