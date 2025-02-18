import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
