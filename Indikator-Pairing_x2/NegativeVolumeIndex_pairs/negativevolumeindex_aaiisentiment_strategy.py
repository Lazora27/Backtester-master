import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
