import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
