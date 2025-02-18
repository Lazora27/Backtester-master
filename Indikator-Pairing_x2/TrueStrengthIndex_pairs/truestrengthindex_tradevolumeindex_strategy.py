import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
