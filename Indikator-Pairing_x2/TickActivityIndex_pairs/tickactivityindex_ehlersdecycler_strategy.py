import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
