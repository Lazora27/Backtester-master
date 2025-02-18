import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'EhlersDecycler': 1.0
        })
    )
