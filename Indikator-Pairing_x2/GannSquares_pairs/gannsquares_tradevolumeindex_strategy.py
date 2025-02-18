import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
