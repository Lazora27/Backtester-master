import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und MassIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'MassIndex': 1.0
        })
    )
