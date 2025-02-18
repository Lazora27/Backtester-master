import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'EhlersDecycler': 1.0
        })
    )
