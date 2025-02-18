import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
