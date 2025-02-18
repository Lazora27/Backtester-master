import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
