import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'UlcerIndex': 1.0
        })
    )
