import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
