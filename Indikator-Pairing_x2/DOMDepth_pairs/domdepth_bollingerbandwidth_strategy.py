import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
