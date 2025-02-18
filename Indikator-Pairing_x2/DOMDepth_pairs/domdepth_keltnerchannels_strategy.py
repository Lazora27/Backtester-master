import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'KeltnerChannels': 1.0
        })
    )
