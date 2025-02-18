import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
