import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
