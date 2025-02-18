import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
