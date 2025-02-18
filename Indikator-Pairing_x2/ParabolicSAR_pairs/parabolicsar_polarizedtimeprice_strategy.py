import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
