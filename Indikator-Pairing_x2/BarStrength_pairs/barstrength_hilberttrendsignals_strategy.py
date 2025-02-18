import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
