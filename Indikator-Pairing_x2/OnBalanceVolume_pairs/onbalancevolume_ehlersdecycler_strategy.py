import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'EhlersDecycler': 1.0
        })
    )
