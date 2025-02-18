import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
