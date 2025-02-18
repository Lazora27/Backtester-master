import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BollingerBands': 1.0
        })
    )
