import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'EhlersDecycler': 1.0
        })
    )
