import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
