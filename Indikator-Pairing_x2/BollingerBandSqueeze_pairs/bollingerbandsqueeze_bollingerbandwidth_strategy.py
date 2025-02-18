import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
