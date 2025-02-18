import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
