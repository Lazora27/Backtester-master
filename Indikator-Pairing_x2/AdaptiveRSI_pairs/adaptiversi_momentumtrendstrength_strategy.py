import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
