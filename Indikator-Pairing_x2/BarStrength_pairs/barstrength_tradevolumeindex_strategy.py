import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
