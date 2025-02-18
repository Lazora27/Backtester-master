import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
