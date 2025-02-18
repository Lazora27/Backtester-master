import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'EhlersDecycler': 1.0
        })
    )
