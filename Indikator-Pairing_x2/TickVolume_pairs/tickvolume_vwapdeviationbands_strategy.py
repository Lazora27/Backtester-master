import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
