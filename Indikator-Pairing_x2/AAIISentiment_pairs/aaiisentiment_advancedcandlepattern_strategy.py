import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
