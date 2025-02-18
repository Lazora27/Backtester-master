import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
