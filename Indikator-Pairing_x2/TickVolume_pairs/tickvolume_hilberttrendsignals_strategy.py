import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
