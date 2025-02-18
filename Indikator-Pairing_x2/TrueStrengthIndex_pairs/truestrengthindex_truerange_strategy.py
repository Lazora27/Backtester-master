import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'TrueRange': 1.0
        })
    )
