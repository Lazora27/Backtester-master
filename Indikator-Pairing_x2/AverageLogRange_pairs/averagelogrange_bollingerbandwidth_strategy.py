import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
