import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'EhlersDecycler': 1.0
        })
    )
