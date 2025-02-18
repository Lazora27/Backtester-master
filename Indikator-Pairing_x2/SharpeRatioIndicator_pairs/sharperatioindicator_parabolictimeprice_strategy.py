import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
