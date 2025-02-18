import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'AdaptiveATR': 1.0
        })
    )
