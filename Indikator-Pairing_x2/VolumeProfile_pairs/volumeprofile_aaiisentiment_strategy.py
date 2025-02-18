import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AAIISentiment': 1.0
        })
    )
