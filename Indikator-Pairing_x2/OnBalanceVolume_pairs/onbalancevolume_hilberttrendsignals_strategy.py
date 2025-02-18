import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
