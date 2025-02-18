import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
