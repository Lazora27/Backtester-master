import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
