import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
