import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'EhlersDecycler': 1.0
        })
    )
