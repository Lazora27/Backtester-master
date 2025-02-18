import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und CycleFinder
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'CycleFinder': 1.0
        })
    )
