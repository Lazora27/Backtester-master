import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
