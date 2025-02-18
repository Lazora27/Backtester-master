import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AccelerationBands': 1.0
        })
    )
