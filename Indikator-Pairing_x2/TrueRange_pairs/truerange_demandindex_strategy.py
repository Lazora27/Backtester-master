import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'DemandIndex': 1.0
        })
    )
