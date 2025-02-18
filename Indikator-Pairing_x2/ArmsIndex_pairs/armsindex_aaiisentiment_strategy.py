import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
