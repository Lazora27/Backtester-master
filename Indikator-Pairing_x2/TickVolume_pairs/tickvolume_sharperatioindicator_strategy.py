import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
