import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AverageTrueRange': 1.0
        })
    )
