import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'AAIISentiment': 1.0
        })
    )
