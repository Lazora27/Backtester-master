import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'TimeCycle': 1.0
        })
    )
