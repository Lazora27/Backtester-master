import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TrendCycles': 1.0
        })
    )
