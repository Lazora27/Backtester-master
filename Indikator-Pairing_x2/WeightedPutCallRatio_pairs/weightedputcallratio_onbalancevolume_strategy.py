import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
