import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'CenterOfGravity': 1.0
        })
    )
