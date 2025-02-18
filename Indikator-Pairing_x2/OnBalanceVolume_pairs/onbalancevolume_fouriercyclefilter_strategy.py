import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
