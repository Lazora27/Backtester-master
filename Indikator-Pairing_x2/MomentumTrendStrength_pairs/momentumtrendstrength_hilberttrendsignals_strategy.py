import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
