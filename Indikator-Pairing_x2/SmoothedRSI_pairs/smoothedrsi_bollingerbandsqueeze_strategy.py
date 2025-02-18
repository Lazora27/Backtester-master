import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
