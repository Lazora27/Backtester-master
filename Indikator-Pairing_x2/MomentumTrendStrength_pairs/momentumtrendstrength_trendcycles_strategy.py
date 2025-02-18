import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'TrendCycles': 1.0
        })
    )
