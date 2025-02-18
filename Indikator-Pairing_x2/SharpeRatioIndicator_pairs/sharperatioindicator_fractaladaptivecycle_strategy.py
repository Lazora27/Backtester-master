import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_FractalAdaptiveCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und FractalAdaptiveCycle
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'FractalAdaptiveCycle': 1.0
        })
    )
