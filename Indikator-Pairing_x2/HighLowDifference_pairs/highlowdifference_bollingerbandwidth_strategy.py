import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
