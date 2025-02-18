import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
