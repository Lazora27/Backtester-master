import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
