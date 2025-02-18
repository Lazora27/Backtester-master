import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
