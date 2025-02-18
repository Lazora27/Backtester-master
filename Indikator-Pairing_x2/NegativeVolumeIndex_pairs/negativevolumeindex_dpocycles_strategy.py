import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
