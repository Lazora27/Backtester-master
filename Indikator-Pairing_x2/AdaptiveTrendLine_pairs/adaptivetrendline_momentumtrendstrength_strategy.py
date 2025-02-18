import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
