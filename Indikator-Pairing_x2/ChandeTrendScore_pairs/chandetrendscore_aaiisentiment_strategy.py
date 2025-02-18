import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AAIISentiment': 1.0
        })
    )
