import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'EhlersDecycler': 1.0
        })
    )
