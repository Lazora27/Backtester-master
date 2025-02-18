import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
