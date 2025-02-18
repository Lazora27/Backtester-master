import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
