import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
