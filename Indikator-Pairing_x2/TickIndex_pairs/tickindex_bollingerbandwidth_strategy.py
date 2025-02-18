import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
