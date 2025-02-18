import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
