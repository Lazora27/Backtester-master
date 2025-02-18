import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
