import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'EhlersDecycler': 1.0
        })
    )
