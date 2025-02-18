import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'EhlersDecycler': 1.0
        })
    )
