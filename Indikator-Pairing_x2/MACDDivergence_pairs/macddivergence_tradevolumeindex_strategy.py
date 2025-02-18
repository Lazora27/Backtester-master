import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
