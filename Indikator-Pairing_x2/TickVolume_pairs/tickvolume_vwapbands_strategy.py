import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und VWAPBands
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'VWAPBands': 1.0
        })
    )
