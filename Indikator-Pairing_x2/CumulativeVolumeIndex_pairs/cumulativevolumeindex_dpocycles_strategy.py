import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeVolumeIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeVolumeIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CumulativeVolumeIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
