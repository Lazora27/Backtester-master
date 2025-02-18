import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'EhlersDecycler': 1.0
        })
    )
