import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
