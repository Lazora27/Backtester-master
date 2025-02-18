import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
