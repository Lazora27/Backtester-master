import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
