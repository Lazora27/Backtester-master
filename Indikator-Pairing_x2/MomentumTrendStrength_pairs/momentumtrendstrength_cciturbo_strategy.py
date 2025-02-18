import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'CCITurbo': 1.0
        })
    )
