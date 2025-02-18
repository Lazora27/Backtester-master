import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
