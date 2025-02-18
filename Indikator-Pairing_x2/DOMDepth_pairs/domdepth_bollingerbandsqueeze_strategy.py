import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
