import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
