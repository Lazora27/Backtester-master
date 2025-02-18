import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
