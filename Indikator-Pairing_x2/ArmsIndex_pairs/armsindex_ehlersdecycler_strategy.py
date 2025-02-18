import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
