import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'BuyingPressure': 1.0
        })
    )
