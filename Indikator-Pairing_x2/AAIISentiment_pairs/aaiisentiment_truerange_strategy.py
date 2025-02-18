import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und TrueRange
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'TrueRange': 1.0
        })
    )
