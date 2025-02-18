import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AAIISentiment': 1.0
        })
    )
