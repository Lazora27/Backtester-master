import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ConnorsRSIMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ConnorsRSIMomentum
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ConnorsRSIMomentum': 1.0
        })
    )
