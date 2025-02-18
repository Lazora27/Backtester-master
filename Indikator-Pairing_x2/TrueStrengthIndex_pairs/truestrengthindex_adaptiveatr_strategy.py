import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
