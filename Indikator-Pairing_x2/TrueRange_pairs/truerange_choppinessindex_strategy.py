import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
