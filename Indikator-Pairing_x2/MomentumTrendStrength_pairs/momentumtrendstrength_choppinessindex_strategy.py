import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
