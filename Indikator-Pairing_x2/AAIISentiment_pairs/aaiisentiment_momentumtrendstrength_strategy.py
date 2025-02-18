import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
