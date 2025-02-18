import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
