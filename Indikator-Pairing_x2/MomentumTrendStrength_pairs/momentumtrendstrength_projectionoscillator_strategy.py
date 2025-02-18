import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
