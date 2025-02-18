import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'DemandIndex': 1.0
        })
    )
