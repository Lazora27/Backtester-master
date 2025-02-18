import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'VortexIndicator': 1.0
        })
    )
