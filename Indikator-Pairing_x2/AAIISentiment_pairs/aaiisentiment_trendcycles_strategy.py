import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'TrendCycles': 1.0
        })
    )
