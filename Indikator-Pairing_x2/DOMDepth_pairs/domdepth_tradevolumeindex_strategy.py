import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
