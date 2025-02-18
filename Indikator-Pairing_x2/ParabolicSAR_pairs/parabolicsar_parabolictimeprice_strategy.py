import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
