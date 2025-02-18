import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'ProjectionBands': 1.0
        })
    )
