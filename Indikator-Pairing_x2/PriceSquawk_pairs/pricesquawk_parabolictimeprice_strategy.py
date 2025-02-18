import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
