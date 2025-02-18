import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und DemandIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'DemandIndex': 1.0
        })
    )
