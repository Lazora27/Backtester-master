import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
