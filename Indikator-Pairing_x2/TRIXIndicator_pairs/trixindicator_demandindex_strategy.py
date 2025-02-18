import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'DemandIndex': 1.0
        })
    )
