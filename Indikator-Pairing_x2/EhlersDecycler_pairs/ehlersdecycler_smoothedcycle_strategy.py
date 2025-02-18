import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'SmoothedCycle': 1.0
        })
    )
