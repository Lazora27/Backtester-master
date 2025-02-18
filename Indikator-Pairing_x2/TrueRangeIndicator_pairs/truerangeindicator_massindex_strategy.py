import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und MassIndex
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'MassIndex': 1.0
        })
    )
