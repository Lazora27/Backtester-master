import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'TRIXIndicator': 1.0
        })
    )
