import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'SmoothedRSI': 1.0
        })
    )
