import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und VWAPBands
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'VWAPBands': 1.0
        })
    )
