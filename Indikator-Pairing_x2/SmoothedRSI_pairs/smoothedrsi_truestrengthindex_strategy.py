import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
