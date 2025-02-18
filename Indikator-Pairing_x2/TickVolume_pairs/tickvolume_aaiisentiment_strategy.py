import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AAIISentiment': 1.0
        })
    )
