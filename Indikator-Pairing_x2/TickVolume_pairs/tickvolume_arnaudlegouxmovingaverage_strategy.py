import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ArnaudLegouxMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ArnaudLegouxMovingAverage
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ArnaudLegouxMovingAverage': 1.0
        })
    )
