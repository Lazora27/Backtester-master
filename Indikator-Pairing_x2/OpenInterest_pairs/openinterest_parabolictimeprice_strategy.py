import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
