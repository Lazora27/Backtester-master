import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'TrueRange': 1.0
        })
    )
