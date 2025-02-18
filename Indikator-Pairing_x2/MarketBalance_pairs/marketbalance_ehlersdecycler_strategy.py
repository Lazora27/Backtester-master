import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'EhlersDecycler': 1.0
        })
    )
