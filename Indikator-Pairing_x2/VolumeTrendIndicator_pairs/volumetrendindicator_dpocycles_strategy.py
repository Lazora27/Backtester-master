import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
