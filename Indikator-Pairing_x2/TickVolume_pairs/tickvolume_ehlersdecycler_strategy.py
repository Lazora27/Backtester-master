import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'EhlersDecycler': 1.0
        })
    )
