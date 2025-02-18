import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
