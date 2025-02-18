import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AroonIndicator': 1.0
        })
    )
