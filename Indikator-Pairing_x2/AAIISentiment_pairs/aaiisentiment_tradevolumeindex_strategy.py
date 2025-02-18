import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
