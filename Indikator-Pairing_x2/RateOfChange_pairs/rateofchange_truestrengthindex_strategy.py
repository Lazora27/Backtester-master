import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
