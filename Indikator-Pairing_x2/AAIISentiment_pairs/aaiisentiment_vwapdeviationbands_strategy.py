import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
