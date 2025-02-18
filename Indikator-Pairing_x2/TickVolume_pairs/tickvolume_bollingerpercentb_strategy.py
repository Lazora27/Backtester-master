import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BollingerPercentB': 1.0
        })
    )
