import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
