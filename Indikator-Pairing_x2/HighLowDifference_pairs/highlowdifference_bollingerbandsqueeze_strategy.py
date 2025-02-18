import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
