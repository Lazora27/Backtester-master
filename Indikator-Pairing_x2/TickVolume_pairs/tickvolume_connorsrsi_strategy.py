import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ConnorsRSI': 1.0
        })
    )
