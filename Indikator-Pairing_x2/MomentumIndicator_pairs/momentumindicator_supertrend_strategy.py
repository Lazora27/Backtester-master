import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'SuperTrend': 1.0
        })
    )
