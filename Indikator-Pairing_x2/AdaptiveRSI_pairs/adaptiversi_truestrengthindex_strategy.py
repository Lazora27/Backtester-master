import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
