import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'MassIndex': 1.0
        })
    )
