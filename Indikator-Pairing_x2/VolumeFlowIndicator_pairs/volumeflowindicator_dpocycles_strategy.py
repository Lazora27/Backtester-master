import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
