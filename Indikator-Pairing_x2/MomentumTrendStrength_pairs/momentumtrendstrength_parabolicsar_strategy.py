import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'ParabolicSAR': 1.0
        })
    )
