import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und TrueRange
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'TrueRange': 1.0
        })
    )
