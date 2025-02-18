import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'EaseOfMovement': 1.0
        })
    )
